import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and label encoder
with open("model.pkl", "rb") as f:
    model, le = pickle.load(f)

st.markdown(
    """
    <style>
    body {
        background-color: #001f3f !important;
        color: white;
    }
    .stApp {
        background-color: #001f3f;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Top image
st.image("C:\\Users\\Muhammad Wahab\\Documents\\NLPproject\\7a74e276-0b84-46b5-b51c-0c8e78f8c1fa.jpeg", width=1000)

# Title
st.title("Well Come To Loan Repayment Prediction App System")

# Create two columns: left for app, right for vertical image
col1 ,col2,col3= st.columns([2, 1,1])   # Adjust ratio as needed

    # Place all your input fields and prediction button here
credit_policy = st.selectbox("Credit Policy (1 = Yes, 0 = No)", [1, 0])
purpose = st.selectbox("Purpose", le.classes_)
int_rate = st.number_input("Interest Rate", min_value=0.0, step=1.0)
installment = st.number_input("Installment", min_value=0.0, step=1.0)
log_annual_inc = st.number_input("Log Annual Income", min_value=0.0)
dti = st.number_input("DTI", min_value=0.0)
fico = st.number_input("FICO Score", min_value=300, max_value=850)
days_with_cr_line = st.number_input("Days with Credit Line", min_value=0.0)
revol_bal = st.number_input("Revolving Balance", min_value=0.0)
revol_util = st.number_input("Revolving Utilization", min_value=0.0)
inq_last_6mths = st.number_input("Inquiries Last 6 Months", min_value=0)
delinq_2yrs = st.number_input("Delinquencies in Last 2 Years", min_value=0)
pub_rec = st.number_input("Public Records", min_value=0)

if st.button("Predict"):
    purpose_encoded = le.transform([purpose])[0]
    input_data = np.array([[credit_policy, purpose_encoded, int_rate, installment,
                            log_annual_inc, dti, fico, days_with_cr_line,
                            revol_bal, revol_util, inq_last_6mths, delinq_2yrs,
                            pub_rec]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🚫 Sorry! Based on the provided details, there's a high risk of loan default.")
    else:
        st.success("🎉 Great news! You're likely to repay the loan successfully!")

with col1:
    st.image(
            "C:\\Users\\Muhammad Wahab\\Documents\\NLPproject\\f746ab6f-f829-4276-9b8c-a36aada944c2.jpeg",width=500,
            use_container_width=True
    )
with col2:
    st.image(
        "C:\\Users\\Muhammad Wahab\\Documents\\NLPproject\\cfbf6fef-7a94-47a5-b833-14fa00886475.jpeg",width=500,
        use_container_width=True
    )
with col3:
    st.image(
        "C:\\Users\\Muhammad Wahab\\Documents\\NLPproject\\images.jpeg",width=500,
        use_container_width=True
    )


st.image("C:\\Users\\Muhammad Wahab\\Documents\\NLPproject\\thankyou.jpg", width=1000)
