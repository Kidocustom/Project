import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load the trained model and scaler
with open("car_price_model.pkl", "rb") as model_file:
    rf = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# Define the columns that were scaled during training
numerical_cols = ['km_driven', 'fuel', 'transmission', 'engine', 'max_power', 'seats', 'Car_Age']

# Inputs from the user
Car_age = st.number_input("Enter Car Age btw (5 - 42) :", 5, 42, 5)
km_driven = st.number_input(" Enter Kilometres driven btw (1 -2.3M):", 1, 360000, 10000)
engine = st.number_input("Enter Engine btw (624 - 3604):", 624, 3604, 1200)
seats = st.number_input("Enter No of seats (2-14):", 2, 14, 4)
max_power = st.number_input("Enter Max power btw (0-400):", 0, 400, 10)

# Fuel type (encode as 0, 1, 2)
fuel = st.radio("Select Fuel Type", ["Diesel", "LPG", "Petrol"])

# Transmission type (0 for Auto, 1 for Manual)
transmission = st.radio("Select Transmission:", ["Auto", "Manual"])

# Encode fuel and transmission as numeric values
fuel_map = {"Diesel": 0, "LPG": 1, "Petrol": 2}
fuel_encoded = fuel_map[fuel]

transmission_map = {"Auto": 0, "Manual": 1}
transmission_encoded = transmission_map[transmission]

# Prepare input data for prediction
input_data = pd.DataFrame([[km_driven, fuel_encoded, transmission_encoded, engine, max_power, seats, Car_age]], 
                          columns=['km_driven', 'fuel', 'transmission', 'engine', 'max_power', 'seats', 'Car_Age'])

# Scale the input data
scaled_data = scaler.transform(input_data[numerical_cols])

# Make prediction
if st.button("Car Price Prediction"):
    prediction = rf.predict(scaled_data)
    st.write(f"Predicted Car Price: ₦{prediction[0]:,.2f}")
