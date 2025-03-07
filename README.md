# Car Power Prediction Model 🚗⚡

A **Machine Learning** model to predict **car horsepower** based on features such as **engine size**, **fuel type**, **transmission**, and other car attributes. This predictive model can be used for estimating a car's power, enabling users to make data-driven decisions in car purchases or evaluations.

## Project Overview

This project utilizes **Linear Regression** to predict a car's horsepower based on a dataset of cars. The model uses a wide range of car features, including but not limited to **Kilometers Driven**, **Engine Size**, **Fuel Type**, **Mileage**, and **Seats**.

The model achieves an impressive **85.16% accuracy** in predicting the horsepower, showing strong potential for real-world applications in the automotive industry, car sales platforms, and vehicle analysis.

## Dataset

The model is trained using the **cars_eda_Analysis.csv** dataset, which includes the following features:

- **Location**: Car's location (not used for prediction)
- **Year**: Year of manufacture
- **Kilometers Driven**: Total kilometers driven by the car
- **Fuel Type**: Type of fuel (e.g., Petrol, Diesel)
- **Transmission**: Type of transmission (e.g., Manual, Automatic)
- **Owner Type**: Type of ownership
- **Mileage**: Fuel efficiency (km/l)
- **Engine**: Engine size (liters)
- **Power**: Horsepower (target variable)
- **Seats**: Number of seats
- **Brand**: Manufacturer brand
- **Model**: Specific model of the car

## Model Overview

The model is trained using **Linear Regression**, a statistical technique for modeling the relationship between a dependent variable (horsepower) and independent variables (car features).

### Performance Metrics:

- **R² Score**: **0.85** – The model explains 85% of the variance in horsepower predictions.
- **Mean Absolute Error (MAE)**: **12.74 HP** – On average, the model's predictions are off by 12.74 horsepower.
- **Mean Squared Error (MSE)**: **442.47 HP** – The squared difference between predicted and actual horsepower values.
- **Accuracy Percentage**: **85.16%** – The model achieves an impressive 85.16% prediction accuracy.

### Conclusion:

The model is **highly accurate**, with strong predictive power, making it ideal for users seeking insights on car power based on key attributes.

## Features for Prediction:

- **Year**
- **Kilometers Driven**
- **Fuel Type**
- **Transmission**
- **Engine Size**
- **Mileage**
- **Seats**
- **Brand**

## Installation and Setup

To run this project locally, follow the steps below:

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/Car-Power-Prediction.git
cd Car-Power-Prediction
```

### 2. Install required libraries:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app:

```bash
streamlit run app.py
```

### 4. Enter car details into the Streamlit interface:

The app will allow you to input various features such as car year, mileage, fuel type, etc. After clicking "Predict", the app will display the estimated horsepower for the selected car.

## Deployment

The model is deployed using **Streamlit**, which provides a clean, interactive web interface. Users can input real-time car features and obtain horsepower predictions on the fly.

## Potential Applications

- **Car dealerships** can use this model to assess car power for their inventory.
- **Automotive websites** can integrate the model for users to predict horsepower based on vehicle specifications.
- **Car buyers** can use this tool to analyze and compare the power of cars they're interested in.

## Future Work

- Extend the model to incorporate more features (e.g., price, car condition, etc.)
- Implement alternative machine learning algorithms (e.g., Random Forest, Gradient Boosting) for improved performance.
- Explore **hyperparameter tuning** to optimize model accuracy.

## Conclusion

This **Car Power Prediction Model** provides valuable insights into predicting horsepower based on various car features. With **85.16% accuracy**, the model offers practical utility for the automotive industry, from car evaluation to consumer decision-making.
