import streamlit as st
import pickle
import pandas as pd

st.header("Calories Burnt Prediction")
col1, col2 = st.columns(2)
gender = st.selectbox("Gender", ["Male", "Female"])

g = 0 if gender == "Male" else 1

with col2:
    Age = st.number_input("Age")
with col1:
    Height = st.number_input("Height")
with col2:
    Weight = st.number_input("Weight")
with col1:
    Duration = st.number_input("Duration")
with col2:
    Heart_Rate = st.number_input("Heart Rate")
with col1:
    Body_temp = st.number_input("Body Temp")


def feature():
    feature = pd.DataFrame({
        "Gender": g,
        "Age": Age,
        "Height": Height,
        "Weight": Weight,
        "Duration": Duration,
        "Heart_Rate": Heart_Rate,
        "Body_Temp": Body_temp,
    }, index=[0])
    return feature


df = feature()

with open("model (2).pkl", "rb") as f:
    try:
        model = pickle.load(f)
    except EOFError as e:
        print(f"Error: {e}")

if st.button("Calories Burnt Prediction"):
    prediction = model.predict(df)
    st.write("Predicted Calories Burnt:", prediction)



