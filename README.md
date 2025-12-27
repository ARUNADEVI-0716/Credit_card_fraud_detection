# 💳 Credit Card Fraud Detection

A Streamlit app to detect credit card fraud. Upload a CSV file of transactions, and the app predicts whether each transaction is **legit (0️⃣)** or **fraud (🚨)**. Fraud rows are highlighted for easy visualization.

**Note:** The trained model file (`credit_fraud_model.pkl`) is not included. Keep your NGROK token secret when running in Colab.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
