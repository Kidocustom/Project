#Machine Learning Model Deployment
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("Salary_Data.csv")

st.write(data.shape)

st.write(data.head())

st.subheader("Dataset Information")

st.write(data.describe())

x=data['YearsExperience']
st.write(x)

y=data['Salary']
st.write(y)

fig, ax=plt.subplots(figsize=(10,5))
plt.scatter(x,y)
st.pyplot(fig)

x=np.array(x).reshape(-1,1)
y=np.array(y).reshape(-1,1)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x,y)

exp=st.number_input("Experience in Years:",0,42,1)
exp=np.array(exp).reshape(1,-1)
prediction=regressor.predict(exp)[0]

if st.button("Salary Prediction"):
    st.write(f"{prediction}")