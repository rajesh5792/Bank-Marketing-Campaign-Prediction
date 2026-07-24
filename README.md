# 🏦 Bank Marketing Campaign Prediction System

A Machine Learning-powered web application that predicts whether a customer is likely to subscribe to a bank term deposit. The application helps marketing teams identify high-potential customers, optimize campaign strategies, and reduce unnecessary marketing costs.

---

## 📌 Overview

Marketing campaigns often involve contacting thousands of customers, many of whom may not be interested in the offered financial product.

This project uses a **Random Forest Classifier** trained on historical bank marketing data to predict customer subscription outcomes. Users can enter customer information through a multi-step Flask web application, review the entered data, and receive an AI-generated prediction with confidence scores and recommendations.

---

## ✨ Features

- Multi-step customer information form
- Clean and responsive user interface
- Review page before prediction
- Random Forest Machine Learning model
- Prediction confidence score
- Subscription probability
- AI-generated recommendation
- Professional result dashboard
- Easy to use and beginner-friendly

---
## 📸 Application Screenshots

### 🏠 Home Page

![Home Page](screenshots/home-page.png)

---

### 👤 Customer Information

![Customer Information](screenshots/customer-information.png)

---

### 💰 Financial Information

![Financial Information](screenshots/financial-information.png)

---

### 📞 Campaign Information

![Campaign Information](screenshots/campaign-information.png)

---

### 📈 Economic Indicators

![Economic Indicators](screenshots/economic-indicators.png)

---

### ✅ Review Page

![Review Page](screenshots/review-page.png)

---

### ✅ Prediction Result - Likely to Subscribe

![Prediction Result - Yes](screenshots/prediction-subscribed.png)

---

### ❌ Prediction Result - Not Likely to Subscribe

![Prediction Result - No](screenshots/prediction-not-subscribed.png)

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest Classifier
- Pandas
- NumPy
- Joblib

### Web Development
- Flask
- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons
- Jinja2

---

## 📂 Project Structure

```text
Bank-Marketing-Campaign-Prediction/
│
├── model/
│   ├── bank_marketing_model.pkl
│   ├── model_columns.pkl
│   └── scaler.pkl
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 Project Workflow

```text
Home Page
      │
      ▼
Customer Information
      │
      ▼
Financial Information
      │
      ▼
Campaign Information
      │
      ▼
Economic Indicators
      │
      ▼
Review Information
      │
      ▼
Generate Prediction
      │
      ▼
Prediction Dashboard
```

---

## 🧠 Machine Learning Workflow

```text
Dataset

↓

Data Cleaning

↓

Feature Engineering

↓

One-Hot Encoding

↓

Model Training

↓

Random Forest Classifier

↓

Model Saving (Joblib)

↓

Flask Deployment
```

---

## 📊 Input Features

The application uses customer information including:

- Age
- Job
- Marital Status
- Education
- Housing Loan
- Personal Loan
- Contact Type
- Campaign Information
- Previous Campaign Outcome
- Economic Indicators

---

## 📈 Output

The system predicts:

- ✅ Likely to Subscribe
- ❌ Not Likely to Subscribe

It also displays:

- Prediction Confidence
- Subscription Probability
- AI Recommendation

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Bank-Marketing-Campaign-Prediction.git
```

Move into the project folder

```bash
cd Bank-Marketing-Campaign-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```text
http://127.0.0.1:5000
```

---

## 🎯 Business Value

This application helps banks:

- Reduce marketing costs
- Improve campaign efficiency
- Prioritize high-potential customers
- Support data-driven decision making
- Increase marketing ROI

---

## 🔮 Future Improvements

- User Authentication
- Database Integration
- Prediction History
- Dashboard Analytics
- Cloud Deployment
- Automated Model Retraining

---

## 👨‍💻 Author

**Rajesh Kannan L**

Computer Science Engineering Student

- 💼 Aspiring Software Developer
- 🤖 Machine Learning Enthusiast
- 📊 Passionate about Data Science
- 🌐 Exploring Full Stack Development

---

⭐ If you found this project interesting, feel free to fork the repository or give it a star!