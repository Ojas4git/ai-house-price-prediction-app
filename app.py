import streamlit as st
import pickle
import numpy as np

# Load model and columns
model = pickle.load(open("house_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict price")

# Example inputs (simplified)
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Living Area (sq ft)", 500, 5000, 1500)
garage_cars = st.number_input("Garage Capacity", 0, 5, 1)
total_bsmt_sf = st.number_input("Basement Area", 0, 3000, 800)

# Predict button
if st.button("Predict Price"):

    # Create input array with all zeros
    input_data = np.zeros(len(columns))

    # Fill selected features
    input_data[list(columns).index("OverallQual")] = overall_qual
    input_data[list(columns).index("GrLivArea")] = gr_liv_area
    input_data[list(columns).index("GarageCars")] = garage_cars
    input_data[list(columns).index("TotalBsmtSF")] = total_bsmt_sf

    # Reshape for prediction
    input_data = input_data.reshape(1, -1)

    prediction = model.predict(input_data)

    st.success(f"Predicted Price: ${prediction[0]:,.2f}")