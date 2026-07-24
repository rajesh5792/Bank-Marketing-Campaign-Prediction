from flask import Flask, render_template, request, redirect, session, url_for
import joblib
import pandas as pd

app = Flask(__name__)
app.secret_key = "bank_marketing_secret_key"
model = joblib.load("models/bank_marketing_model.pkl")
model_columns = joblib.load("models/model_columns.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/step1", methods=["GET", "POST"])
def step1():

    if request.method == "POST":

        age = request.form.get("age")
        job = request.form.get("job")
        marital = request.form.get("marital")
        education = request.form.get("education")

        # Validation
        if not all([age, job, marital, education]):
            return redirect("/step1")

        # Save to session
        session["age"] = age
        session["job"] = job
        session["marital"] = marital
        session["education"] = education

        return redirect("/step2")

    return render_template("step1_customer.html")

@app.route("/step2", methods=["GET", "POST"])
def step2():

    if request.method == "POST":

        housing = request.form.get("housing")
        loan = request.form.get("loan")
        default = request.form.get("default")

        # Validation
        if not all([housing, loan, default]):
            return redirect("/step2")

        # Save to session
        session["housing"] = housing
        session["loan"] = loan
        session["default"] = default

        return redirect("/step3")

    return render_template("step2_financial.html")

@app.route("/step3", methods=["GET", "POST"])
def step3():

    if request.method == "POST":

        contact = request.form.get("contact")
        month = request.form.get("month")
        day_of_week = request.form.get("day_of_week")
        campaign = request.form.get("campaign")
        previous = request.form.get("previous")
        poutcome = request.form.get("poutcome")

        # Validation
        if not all([contact, month, day_of_week, campaign, previous, poutcome]):
            return redirect("/step3")

        # Save to session
        session["contact"] = contact
        session["month"] = month
        session["day_of_week"] = day_of_week
        session["campaign"] = campaign
        session["previous"] = previous
        session["poutcome"] = poutcome

        return redirect("/step4")

    return render_template("step3_campaign.html")

@app.route("/step4", methods=["GET", "POST"])
def step4():

    if request.method == "POST":

        emp_var_rate = request.form.get("emp_var_rate")
        cons_price_idx = request.form.get("cons_price_idx")
        cons_conf_idx = request.form.get("cons_conf_idx")
        euribor3m = request.form.get("euribor3m")
        nr_employed = request.form.get("nr_employed")
        pdays = request.form.get("pdays")

        # Validation
        if not all([
            emp_var_rate,
            cons_price_idx,
            cons_conf_idx,
            euribor3m,
            nr_employed,
            pdays
        ]):
            return redirect("/step4")

        # Save to session
        session["emp_var_rate"] = emp_var_rate
        session["cons_price_idx"] = cons_price_idx
        session["cons_conf_idx"] = cons_conf_idx
        session["euribor3m"] = euribor3m
        session["nr_employed"] = nr_employed
        session["pdays"] = pdays

        return redirect("/review")

    return render_template("step4_economic.html")

@app.route("/review")
def review():

    return render_template(
        "review.html",

        age=session.get("age"),
        job=session.get("job"),
        marital=session.get("marital"),
        education=session.get("education"),

        housing=session.get("housing"),
        loan=session.get("loan"),
        default=session.get("default"),

        contact=session.get("contact"),
        month=session.get("month"),
        day_of_week=session.get("day_of_week"),
        campaign=session.get("campaign"),
        previous=session.get("previous"),
        poutcome=session.get("poutcome"),

        emp_var_rate=session.get("emp_var_rate"),
        cons_price_idx=session.get("cons_price_idx"),
        cons_conf_idx=session.get("cons_conf_idx"),
        euribor3m=session.get("euribor3m"),
        nr_employed=session.get("nr_employed"),
        pdays=session.get("pdays")
    )


@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "age": float(session["age"]),
        "campaign": int(session["campaign"]),
        "pdays": int(session["pdays"]),
        "previous": int(session["previous"]),

        "emp.var.rate": float(session["emp_var_rate"]),
        "cons.price.idx": float(session["cons_price_idx"]),
        "cons.conf.idx": float(session["cons_conf_idx"]),
        "euribor3m": float(session["euribor3m"]),
        "nr.employed": float(session["nr_employed"]),

        "job": session["job"],
        "marital": session["marital"],
        "education": session["education"],
        "default": session["default"],
        "housing": session["housing"],
        "loan": session["loan"],
        "contact": session["contact"],
        "month": session["month"],
        "day_of_week": session["day_of_week"],
        "poutcome": session["poutcome"]
    }

    df = pd.DataFrame([data])

    # Create dummy variables exactly like training
    df = pd.get_dummies(df, drop_first=True)

    # Match training columns
    df = df.reindex(columns=model_columns, fill_value=0)
    # Prediction
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0]

    predicted_class = "Likely to Subscribe" if prediction == 1 else "Not Likely to Subscribe"

    confidence = round(max(probability) * 100, 2)

    return render_template(
        "result.html",
        prediction=prediction,
        predicted_class=predicted_class,
        confidence=confidence,
        probability_yes=round(probability[1] * 100, 2),
        probability_no=round(probability[0] * 100, 2)
    )

@app.route("/new_prediction")
def new_prediction():
    session.clear()
    return redirect(url_for("step1"))

if __name__== "__main__":
    app.run(debug = True)

