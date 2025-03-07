import joblib
import pandas as pd
import streamlit as st

model = joblib.load('car_models.pkl')
features = joblib.load('car_columns.pkl')

data = pd.read_csv('cars_eda_Analysis.csv')

year_options = data['Year'].unique().tolist()
brand_options = data['brand'].unique().tolist()
fuel_options = data['Fuel_Type'].unique().tolist()
transmission_options = data['Transmission'].unique().tolist()

def predict(new_data):
    pred = model.predict(new_data)
    return pred

st.title("Car Power Prediction")

car_brand = st.selectbox("Select Brand", options=brand_options)
car_fuel = st.selectbox("Select Fuel Type", options=fuel_options)
car_transmission = st.selectbox("Select Transmission Type", options=transmission_options)

car_year = st.number_input("Enter year:", min_value=2000, max_value=2025, step=1, format="%d")  # for year (integer)
car_kilometer = st.number_input("Enter kilometers driven:", min_value=0, max_value=500000, step=1000, format="%d")  # for kilometers (float)
car_engine = st.number_input("Enter engine size (in liters):", min_value=0.5, max_value=10.0, step=0.1, format="%.1f")  # for engine size (float)
car_mileage = st.number_input("Enter mileage (km/l):", min_value=0.0, max_value=50.0, step=0.1, format="%.1f")  # for mileage (float)
car_seats = st.number_input("Enter seats:", min_value=1, max_value=10, step=1, format="%d")  # for seats (integer)


if st.button("Predict"):
    car_year = int(car_year)
    car_kilometer = int(car_kilometer)
    car_engine = float(car_engine)
    car_mileage = float(car_mileage)
    car_seats = int(car_seats)
    input_data = {
        'Year': [car_year],
        'Kilometers_Driven': [car_kilometer],
        'Mileage': [car_mileage],
        'Engine': [car_engine],
        'Seats': [car_seats],
        'Fuel_Type': [car_fuel],
        'Transmission': [car_transmission],
        'brand': [car_brand]
    }

    new_data = pd.DataFrame(input_data)
    new_data = pd.get_dummies(data=new_data)

    for feature in features:
        if feature not in new_data.columns:
            new_data[feature] = 0
    
    prediction = predict(new_data[features])
    car_details = {
    "Feature": ["Year", "Brand", "Fuel Type", "Transmission", "Kilometers Driven", "Engine Size", "Mileage", "Seats"],
    "Value": [car_year, car_brand, car_fuel, car_transmission, f"{car_kilometer} km", f"{car_engine} L", f"{car_mileage} km/l", car_seats]
}
    car_df = pd.DataFrame(car_details)

    if prediction[0] <= 0:
        st.error("The predicted horsepower is less than or equal to 0. Please check your input values.")
    else:
                st.subheader("🚗 Car Power Prediction Report")
                st.write(f"The predicted power is: {prediction[0]}")
                st.markdown(f"### **Selected Car Features**")
                st.table(car_df)
