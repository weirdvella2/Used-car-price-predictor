import streamlit as st
import pickle
import numpy as np

# Load your model pipeline
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

st.set_page_config(page_title="Car Price Predictor", layout="centered")
st.title("🚗 Used Car Price Predictor")

st.markdown("Enter the details below to get an estimated resale price:")

# 3 categorical features
name = st.selectbox("Car Model", [
    'Audi A3 Cabriolet', 'Audi A4 1.8', 'Audi A4 2.0', 'Audi A6 2.0', 'Audi A8', 'Audi Q3 2.0',
    'Audi Q5 2.0', 'Audi Q7', 'BMW 3 Series', 'BMW 5 Series', 'BMW 7 Series', 'BMW X1',
    'BMW X1 sDrive20d', 'BMW X1 xDrive20d', 'Chevrolet Beat', 'Chevrolet Beat Diesel',
    'Chevrolet Beat LS', 'Chevrolet Beat LT', 'Chevrolet Cruze LTZ', 'Chevrolet Enjoy',
    'Chevrolet Spark', 'Ford EcoSport', 'Honda City', 'Hyundai i10', 'Hyundai Verna',
    'Maruti Alto', 'Maruti Swift', 'Tata Nexon', 'Toyota Innova', 'Volkswagen Vento Konekt',
    'Volvo S80 Summum'
])

company = st.selectbox("Brand", [
    'Audi', 'BMW', 'Chevrolet', 'Datsun', 'Fiat', 'Force', 'Ford',
    'Hindustan', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Land',
    'Mahindra', 'Maruti', 'Mercedes', 'Mini', 'Mitsubishi', 'Nissan',
    'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo'
])

fuel = st.selectbox("Fuel Type", ['Diesel', 'LPG', 'Petrol'])

# 2 numerical inputs (adjust labels if needed)
kms = st.number_input("Kilometers Driven", value=10000)
age = st.number_input("Car Age (in years)", value=5)

# Combine input
input_features = np.array([[name, company, fuel, kms, age]])

if st.button("Predict Price"):
    prediction = model.predict(input_features)[0]
    st.success(f"💰 Estimated Resale Price: ₹ {prediction:,.2f}")

print("Gitttttt Test")