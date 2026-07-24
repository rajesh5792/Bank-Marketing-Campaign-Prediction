
# Bank Marketing Campaign Prediction System

A Machine Learning web application that predicts whether a customer is likely to subscribe to a bank term deposit using a **Random Forest Classifier**. Built with **Flask**, the application provides a multi-step interface for entering customer information and generating AI-powered predictions.

---

## Overview

Marketing campaigns often involve contacting thousands of customers, resulting in significant costs and time. This project helps banks identify customers who are more likely to subscribe to a term deposit, enabling smarter marketing decisions and better resource allocation.

The application allows users to enter customer details, review the information, and receive a prediction along with confidence scores and recommendations.

---

## Features

- Multi-step customer information form
- Review page before prediction
- Random Forest Machine Learning model
- Prediction confidence score
- Subscription probability
- AI-generated recommendation
- Responsive user interface
- Beginner-friendly workflow

---

## Technology Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- Random Forest Classifier
- Pandas
- NumPy
- Joblib

### Web Development

- Flask
- HTML5
- CSS3
- Bootstrap 5
- Jinja2

---

## Application Screenshots

### Home Page

![Home Page](screenshots/home-page.png)

---

### Customer Information

![Customer Information](screenshots/customer-information.png)

---

### Financial Information

![Financial Information](screenshots/financial-information.png)

---

### Campaign Information

![Campaign Information](screenshots/campaign-information.png)

---

### Economic Indicators

![Economic Indicators](screenshots/economic-indicators.png)

---

### Review Page

![Review Page](screenshots/review-page.png)

---

### Prediction Result – Likely to Subscribe

![Prediction Yes](screenshots/prediction-subscribed.png)

---

### Prediction Result – Not Likely to Subscribe

![Prediction No](screenshots/prediction-not-subscribed.png)

---

## Project Workflow

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
Review Page
      │
      ▼
Machine Learning Prediction
      │
      ▼
Prediction Dashboard
```

---

## Machine Learning Pipeline

```text
Dataset
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
One-Hot Encoding
    │
    ▼
Random Forest Training
    │
    ▼
Model Serialization
    │
    ▼
Flask Deployment
```

---

## Project Structure

```text
Bank-Marketing-Campaign-Prediction/
│
├── dataset/
├── models/
├── notebook/
├── screenshots/
├── static/
├── templates/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Bank-Marketing-Campaign-Prediction.git
```

Navigate to the project directory

```bash
cd Bank-Marketing-Campaign-Prediction
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser and visit

```text
http://127.0.0.1:5000
```

---

## Business Value

This application helps organizations:

- Reduce unnecessary marketing costs
- Improve campaign efficiency
- Prioritize high-potential customers
- Support data-driven decision making
- Increase marketing return on investment

---

## Future Improvements

- User Authentication
- Prediction History
- Database Integration
- Dashboard Analytics
- Cloud Deployment
- Automated Model Retraining

---

## Author

**Rajesh Kannan L**

Computer Science Engineering Student

Aspiring Software Developer with interests in Machine Learning, Data Science, and Software Development.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgement

This project was developed as part of my Machine Learning learning journey and demonstrates the deployment of a classification model using Flask for a real-world business use case.
