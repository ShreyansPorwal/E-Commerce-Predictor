# Importing Packages
import streamlit as st
import pandas as pd
import pickle

#Setting the website title and description
st.title("E-Commerce Predictor 📊📈")
st.text("We use machine learning models to predict whether products from an international e-commerce company will reach customers on time by analyzing various factors. ")

st.write("Enter the package details below to check if it will arrive on time.")

#User Inputted Values to be used in the AI Model to create a prediction
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
product_category_name = st.selectbox("Product Category", ['Home and Living',
    'Fashion and Accessories',
    'Toys and Baby Products',
    'Health and Beauty',
    'Electronics and Gadgets',
    'Sports and Leisure',
    'Food and Beverages',
    'Arts and Crafts',
    'Gifts and Celebrations',
    'Pets and Animals',
    'Office and Stationery',
    'Industry and Commerce',
    'Media and Entertainment',
    'Miscellaneous',])
payment_method = st.selectbox("Payment Method", ["Credit Card", "Wallet", "Voucher", "Debit Card"])
payment_installment = st.number_input("Payment Installment", step=1)
shipping_charges = st.number_input("Shipping Charges", step=.01)

# Translates the user input(Destination and Payment Method) into numerical value for the AI Model to read
customer_state = {
    'São Paulo (SP)': 0,
    'Rio de Janeiro (RJ)': 1,
    'Minas Gerais (MG)': 2,
    'Santa Catarina (SC)': 3,
    'Espírito Santo (ES)': 4,
    'Rio Grande do Norte (RN)': 5,
    'Bahia (BA)': 6,
    'Distrito Federal (DF)': 7,
    'Rio Grande do Sul (RS)': 8,
    'Pernambuco (PE)': 9,
    'Goiás (GO)': 10,
    'Ceará (CE)': 11,
    'Paraná (PR)': 12,
    'Maranhão (MA)': 13,
    'Piauí (PI)': 14,
    'Mato Grosso (MT)': 15,
    'Mato Grosso do Sul (MS)': 16,
    'Sergipe (SE)': 17,
    'Rondônia (RO)': 18,
    'Tocantins (TO)': 19,
    'Amazonas (AM)': 20,
    'Amapá (AP)': 21,
    'Paraíba (PB)': 22,
    'Pará (PA)': 23,
    'Alagoas (AL)': 24,
    'Acre (AC)': 25,
    'Roraima (RR)': 26
}
x1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
destination_num = customer_state[destination]
x1[destination_num] = 1

prod_cat = {
    'Home and Living': 0,
    'Fashion and Accessories': 1,
    'Toys and Baby Products': 2,
    'Health and Beauty': 3,
    'Electronics and Gadgets': 4,
    'Sports and Leisure': 5,
    'Food and Beverages': 6,
    'Arts and Crafts': 7,
    'Gifts and Celebrations': 8,
    'Pets and Animals': 9,
    'Office and Stationery': 10,
    'Industry and Commerce': 11,
    'Media and Entertainment': 12,
    'Miscellaneous': 13
}
x2 = [0] * 14
product_num = prod_cat[product_category_name]
x2[product_num] = 1

payment_types = {'Credit Card': 0, 'Wallet': 1, 'Voucher': 2, 'Debit Card': 3}
x3 = [0] * 4
payment_num = payment_types[payment_method]
x3[payment_num] = 1

#Create a dataframe  of the users inputs
input = {
    **{f"payment_method_{i}": x3[i] for i in range(4)},
    "payment_installment": payment_installment,
    "shipping_charges": shipping_charges,
    **{f"destination_{i}": x1[i] for i in range(27)},
    **{f"product_category_name_{i}": x2[i] for i in range(14)},
    "weight(g)": weight,
    "volume(cm^3)": length * width * height,
}

user_df = pd.DataFrame([input])

## st.header("Your package details: ")
## st.write(user_df)

# Uploads the dataframe into the AI model
model = pickle.load(open("ecommerce_model.pckl", "rb"))
if st.button("Predict Delivery Time"):
    prediction = model.predict(user_df)
    st.write("### We predict your package will arrive in : ", int(prediction), " days.")