import streamlit as st
import pickle
import numpy as np
import random

# Load the trained model
model = pickle.load(open('rock_vs_mine_model.pkl', 'rb'))

# Streamlit app
st.title("Rock vs Mine Predictor")

# Input features
st.write("Enter the features for prediction:")

# Initialize feature_values with 60 zeros
feature_values = [0.0] * 60

# Generate random button functionality to fill the input fields with random values
if st.button("Generate Random Features"):
    feature_values = [random.uniform(0.0, 100.0) for _ in range(60)]  # Generate 60 random values



# Create 5 columns for a more compact layout
cols = st.columns(5)

# Create input fields in the columns
for i in range(60):
    col = cols[i % 5]  # Assign each input to one of the 3 columns
    feature_values[i] = col.number_input(f'Feature {i + 1}', min_value=0.0, max_value=100.0, step=0.01, value=feature_values[i])

# Prediction button
if st.button("Predict"):
    prediction = model.predict([feature_values])
    result = "Rock" if prediction[0] == 'R' else "Mine"
    st.success(f'The object is predicted to be: {result}')
