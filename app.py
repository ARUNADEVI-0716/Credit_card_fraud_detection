import streamlit as st
import pandas as pd
import pickle
import os
from pyngrok import ngrok
ngrok_token = os.environ.get("NGROK_AUTH_TOKEN")
if ngrok_token is None:
    raise ValueError("NGROK_AUTH_TOKEN is not set. Set it in Colab before running the app.")
ngrok.set_auth_token(ngrok_token)


model = pickle.load(open('credit_fraud_model.pkl', 'rb'))

# ----------------------------
# STREAMLIT APP
# ----------------------------
st.title("💳 Credit Card Fraud Detection")

# Features used in training
feature_columns = [
    'Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12',
    'V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24',
    'V25','V26','V27','V28','Amount'
]

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    
    # Keep only the feature columns
    data_for_prediction = data[feature_columns]
    
    # Predict
    predictions = model.predict(data_for_prediction)
    
    # Map predictions to emojis
    data['Prediction'] = predictions
    data['Prediction'] = data['Prediction'].map({0: "0️⃣ Legit", 1: "🚨 Fraud"})
    
    # Show summary counts
    summary = data['Prediction'].value_counts()
    st.write("### Summary")
    st.write(summary)
    
    # Show a sample of rows with fraud highlighted
    sample_size = 1000  # display first 1000 rows only
    sample_data = data.head(sample_size)
    
    def highlight_fraud(row):
        return ['background-color: red' if val == "🚨 Fraud" else '' for val in row]
    
    st.write("### Predictions (sample of first 1000 rows)")
    st.dataframe(sample_data.style.apply(highlight_fraud, subset=['Prediction']))





