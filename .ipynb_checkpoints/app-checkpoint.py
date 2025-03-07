import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('car_models.pkl')
columns = joblib.load('car_columns.pkl')

data = pd.read_csv('cars_eda_Analysis.csv')

brand_names = data['brand'].unique()

st.title("Car Horsepower Prediction")

brand = st.selectbox("Select the car brand", brand_names)

engine_size = st.number_input("Enter engine size (in liters)", min_value=0.0, max_value=10.0, step=0.1, placeholder="Example: 2.0")
weight = st.number_input("Enter weight (in kg)", min_value=500, max_value=5000, step=10, placeholder="Example: 1500")
fuel_efficiency = st.number_input("Enter fuel efficiency (miles per gallon)", min_value=5.0, max_value=50.0, step=0.1, placeholder="Example: 25.0")

if st.button("Predict"):
    if engine_size < 0.5:
        st.error("Engine size is too low! Minimum value is 0.5 liters.")
    elif engine_size > 10.0:
        st.error("Engine size is too high! Maximum value is 10.0 liters.")
    elif weight < 500:
        st.error("Weight is too low! Minimum value is 500 kg.")
    elif weight > 5000:
        st.error("Weight is too high! Maximum value is 5000 kg.")
    elif fuel_efficiency < 5.0:
        st.error("Fuel efficiency is too low! Minimum value is 5.0 mpg.")
    elif fuel_efficiency > 50.0:
        st.error("Fuel efficiency is too high! Maximum value is 50.0 mpg.")
    else:
        user_input = {
            'Brand': [brand],
            'Engine_Size': [engine_size],
            'Weight': [weight],
            'Fuel_Efficiency': [fuel_efficiency]
        }

        user_input_df = pd.DataFrame(user_input)

        user_input_encoded = pd.get_dummies(user_input_df)

        user_input_encoded = user_input_encoded.reindex(columns=columns, fill_value=0)

        prediction = model.predict(user_input_encoded)

        # Ensure horsepower is not negative
        prediction = max(0, prediction[0])

        st.subheader(f"Predicted Horsepower: {prediction:.2f} HP")

