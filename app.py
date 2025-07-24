import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title(" Titanic Survival Prediction")
st.write("Enter the details to predict survival.")

# Input fields
pclass = st.selectbox("Passenger Class", [1, 2, 3])
age = st.slider("Age", 0, 100, 25)
sibsp = st.slider("Siblings/Spouses Aboard", 0, 5, 0)
parch = st.slider("Parents/Children Aboard", 0, 5, 0)
fare = st.number_input("Fare Paid")

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([[pclass, age, sibsp, parch, fare]],
                             columns=["Pclass", "Age", "SibSp", "Parch", "Fare"])
    result = model.predict(input_data)[0]
    st.success("Survived" if result == 1 else "Did Not Survive")

