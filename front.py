import streamlit as st
import pandas as pd


st.title("E-Commerce Predictor 📊📈")
st.text("We use machine learning models to predict whether products from an international e-commerce company will reach customers on time by analyzing various factors. ")

st.write("Enter the package details below to check if it will arrive on time.")

col1, col2 = st.columns(2)
weight = col1.number_input("Package Weight (g)", min_value=0.1, step=0.1)
length = col1.number_input("Product Length (cm)", min_value=0.1, step=0.1)
width = col2.number_input("Product Width (cm)", min_value=0.1, step=0.1)
height = col2.number_input("Product Height (cm)", min_value=0.1, step=0.1)
destination = st.selectbox("Destination", ['São Paulo (SP)',
    'Rio de Janeiro (RJ)',
    'Minas Gerais (MG)',
    'Santa Catarina (SC)',
    'Espírito Santo (ES)',
    'Rio Grande do Norte (RN)',
    'Bahia (BA)',
    'Distrito Federal (DF)',
    'Rio Grande do Sul (RS)',
    'Pernambuco (PE)',
    'Goiás (GO)',
    'Ceará (CE)',
    'Paraná (PR)',
    'Maranhão (MA)',
    'Piauí (PI)',
    'Mato Grosso (MT)',
    'Mato Grosso do Sul (MS)',
    'Sergipe (SE)',
    'Rondônia (RO)',
    'Tocantins (TO)',
    'Amazonas (AM)',
    'Amapá (AP)',
    'Paraíba (PB)',
    'Pará (PA)',
    'Alagoas (AL)',
    'Acre (AC)',
    'Roraima (RR)',])  
payment_method = st.selectbox("Payment Method", ["Credit Card", "Wallet", "Voucher", "Debit Card"])
payment_installment = st.number_input("Payment Installment", step=1)

input = {
    "weight(g)": weight,
    "volume(cm^3)": length * width * height,
    "destination": destination,
    "payment_method": payment_method,
    "payment_installment": payment_installment,
}

user_df = pd.DataFrame([input])

st.header("Your package details: ")
st.write(user_df)

if st.button("Predict Delivery Time"):
    prediction = model.predict(user_df)
