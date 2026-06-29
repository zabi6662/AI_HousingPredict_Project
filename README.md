# 💳 Loan Repayment Prediction System
## 📌 Description
The **Loan Repayment Prediction System** is a Machine Learning web application which predicts whether a customer is capable of repaying the loan or will default. This system is developed using **Python, Scikit-learn** and **Streamlit**.
This project can help banks or other financial institutions make appropriate predictions about customers’ financial capabilities.
## 🚀 Features
* Intuitive web interface developed using Streamlit
* Fast prediction of loan repayment status
* Uses trained Random Forest Machine Learning model
* Label Encoding of categorical features
* Great looking interface with pictures
* Shows prediction result with successful and unsuccessful messages
## 🛠 Technologies Used
* Python
* Pandas
* Numpy
* Scikit-learn
* Streamlit
* Pickle
## 📊 Dataset
The dataset includes information about customers' loans including:
* Credit policy
* Loan purpose
* Interest rate
* Monthly Installment
* Annual Income
* Debt-to-income ratio (DTI)
* FICO score
* Months since credit opened
* Total revolving balance
* Revolving utilization of unsecured lines
* Number of credit inquiries
* Delinquency in last 2 years
* Public records### Target Variable
not.fully.paid
* **0 → Loan Repaid Successfully**
* **1 → Loan Default**
## 🤖 Machine Learning Model
The project employs the **Random Forest Classifier**.
```python
RandomForestClassifier(
    n_estimators=600,
    random_state=42
)
```
The model trains on an 80/20 train/test data split and then saved using Pickle.-
## ▶️ Train the Model

This will:
* Load the dataset
* Encode categorical features
* Train the Random Forest classifier
* Save the trained model as:
model.pkl
## ▶️ Run the Streamlit Application
```bash
streamlit run app.py
The application will open in your browser
## 📷 Application Workflow
1. Launch the Streamlit application.
2. Provide loan details for the customer.
3. Press the **Predict** button.
4. The model will analyze the data.
5. Show the prediction output.
## 📌 Prediction Output
### ✅ Loan Repaid
🎉 Good news! The loan will most likely be repaid.
### ❌ Default Risk
🚫 Bad news! There is a high risk of loan default.
## 📈 Model Training Steps
1. Load dataset
2. Encode categorical feature (`purpose`)
3. Split dataset into training and testing sets
4. Train the Random Forest classifier
5. Evaluate accuracy
6. Save model using Pickle
