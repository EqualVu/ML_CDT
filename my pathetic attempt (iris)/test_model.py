import streamlit as st
import pandas as pd
import pickle
import sys
import os

# Add the directory containing custom_module.py to the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from custom_module import myweight

# Define the path to the model file
model_path = 'd:/Study stuff/Machine Learning/Git_Demo_CDT_01_K27/ML_CDT/Iris_model/iris_model.pkl'

# Initialize model variable
model = None

# Load the model
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    st.success("Model loaded successfully")
except FileNotFoundError:
    st.error(f"The model file was not found at path: {model_path}")
except EOFError:
    st.error("The pickle file is empty or corrupted")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")

st.title("Iris Species Classifier")

# File uploader for user to upload data file
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xls", "xlsx"])

if uploaded_file is not None:
    # Read the uploaded file
    if uploaded_file.name.endswith('.csv'):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    # Display the uploaded data
    st.write("Uploaded Data:")
    st.write(data)

    # Expected feature columns based on the Iris dataset
    expected_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    
    # Check if the necessary columns are present
    if set(expected_columns).issubset(data.columns):
        features = data[expected_columns]
        
        # Check if model is loaded before prediction
        if model is not None:
            try:
                # Ensure features are in the correct order
                features = features[expected_columns]
                
                # Make predictions
                prediction = model.predict(features)
                st.write("Prediction:", prediction)
            except Exception as e:
                st.error(f"Error during prediction: {e}")
        else:
            st.error("Model is not loaded, cannot make predictions.")
    else:
        missing_columns = set(expected_columns) - set(data.columns)
        st.error(f"The uploaded file does not contain the required columns. Missing columns: {', '.join(missing_columns)}")
