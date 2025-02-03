import streamlit as st
import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Title
st.title("Isaac's Car Price Prediction")

# Load Data
data = pd.read_csv("cleaned_car_prediction_project.csv")
st.write("### Data Preview:")
st.write(data.head())

# Feature Selection
X = data.iloc[:, :-1]  # Features (all but last column)
y = data.iloc[:, -1]  # Target (last column)

# Columns to Scale
numerical_cols = ['km_driven', 'fuel', 'transmission', 'engine', 'max_power', 'seats', 'Car_Age']

# Apply MinMaxScaler **before splitting**
scaler = MinMaxScaler()
X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
rf = GradientBoostingRegressor()
rf.fit(X_train.values, y_train.values)

# Predictions
y_pred = rf.predict(X_test)

# Display Predictions
st.write("### Predicted vs Actual Values:")
results = pd.DataFrame({"Predicted": y_pred, "Actual": y_test.values})
st.write(results.head())

# Regression Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

st.write("### Model Performance Metrics:")
st.write(f"📉 Mean Absolute Error (MAE): {mae:.2f}")
st.write(f"📉 Mean Squared Error (MSE): {mse:.2f}")
st.write(f"📈 R² Score: {r2:.2f}")

# Save Model & Scaler
with open("car_price_model.pkl", "wb") as model_file:
    pickle.dump(rf, model_file)

with open("scaler.pkl", "wb") as scaler_file:
    pickle.dump(scaler, scaler_file)

st.write("✅ Model and Scaler saved successfully!")
