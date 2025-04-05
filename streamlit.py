import pandas as pd
import pickle
import streamlit as st
import numpy as np

# Set the page title and description
st.title("Customer Segmentation App")
st.write("""
This app groups customers into different clusters based on their 
age, annual income, and spending score using an Unsupervised Clustering Model.
""")

# Load the pre-trained clustering model
model_pickle = open("models/kmodel.pkl", "rb")
clustering_model = pickle.load(model_pickle)
model_pickle.close()

# Prepare the form to collect user inputs
with st.form("user_inputs"):
    st.subheader("Customer Details")

    # Gender input
    Gender = st.selectbox("Gender", options=["Male", "Female"])

    # Age
    Age = st.number_input("Age", min_value=18, max_value=100, step=1)

    # Annual Income
    Annual_Income = st.number_input("Annual Income (10-200)", min_value=10, max_value=200, step=1)

    # Spending Score
    Spending_Score = st.number_input("Spending Score (1-100)", min_value=1, max_value=100, step=1)

    # Submit button
    submitted = st.form_submit_button("Find My Cluster")

# Process input and perform clustering prediction
if submitted:
    # Convert categorical inputs into numerical features
    Gender_Male = 1 if Gender == "Male" else 0
    Gender_Female = 1 if Gender == "Female" else 0

    # Prepare the input for clustering prediction
    clustering_input = [[Annual_Income, Spending_Score]]

    # Perform clustering prediction
    cluster_number = clustering_model.predict(clustering_input)[0]

    # Display result
    st.subheader("Customer Segment Result:")
    st.write(f"You have been assigned to **Cluster {cluster_number}** based on your profile.")

st.write(
    """We used an **Unsupervised Clustering Model** to segment customers. 
    The clusters represent different customer groups based on income, age, and spending behavior."""
)
st.image("visualize_clusters.png")
