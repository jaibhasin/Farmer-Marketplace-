import pandas as pd
import pickle  # For loading saved models
import numpy as np
from collections import Counter  # For majority voting

# Nitrogen content (N): 0 to 200 (mg/kg)
# Phosphorus content (P): 0 to 200 (mg/kg)
# Potassium content (K): 0 to 300 (mg/kg)
# Temperature (°C): 10 to 50
# Humidity (%): 10 to 100
# pH level: 3.5 to 9.0
# Rainfall (mm): 0 to 500 (can be higher in some regions)


# Function to take user input
def get_user_input( N ,  P ,  K ,  temperature ,  humidity , pH , rainfall):
    # Taking input for features (N, P, K, etc.)
    # N = float(input("Enter Nitrogen content (N): "))
    # P = float(input("Enter Phosphorus content (P): "))
    # K = float(input("Enter Potassium content (K): "))
    # temperature = float(input("Enter Temperature (°C): "))
    # humidity = float(input("Enter Humidity (%): "))
    # pH = float(input("Enter pH level: "))
    # rainfall = float(input("Enter Rainfall (mm): "))
    
    # Convert the input data to a DataFrame
    user_input = pd.DataFrame([[N, P, K, temperature, humidity, pH, rainfall]], 
                              columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    
    return user_input

# Function to predict using models
def predict_crop(user_input):
    # Load the trained models, scaler, and label encoder from the 'ok13' folder
    logreg = pickle.load(open('./pkl_files/logreg_model.pkl', 'rb'))
    rf = pickle.load(open('./pkl_files/rf_model.pkl', 'rb'))
    xgb_model = pickle.load(open('./pkl_files/xgb_model.pkl', 'rb'))
    scaler = pickle.load(open('./pkl_files/scaler.pkl', 'rb'))
    label_encoder = pickle.load(open('./pkl_files/label_encoder.pkl', 'rb'))

    # Preprocess the input data
    user_input_scaled = scaler.transform(user_input)

    # Predictions using different models
    y_pred_logreg = logreg.predict(user_input_scaled)[0]
    y_pred_rf = rf.predict(user_input)[0]
    y_pred_xgb = xgb_model.predict(user_input_scaled)[0]

    # Majority voting for the final prediction
    predictions = [y_pred_logreg, y_pred_rf, y_pred_xgb]
    final_prediction = Counter(predictions).most_common(1)[0][0]

    # Convert the final numerical prediction back to the crop name
    predicted_crop = label_encoder.inverse_transform([final_prediction])[0]

    # Print the final prediction
    print(f"The most accurate predicted crop is: {predicted_crop}")

# Get user input and predict
user_input = get_user_input(100.0,100.0,100.0,30,30,5,200)
predict_crop(user_input)
