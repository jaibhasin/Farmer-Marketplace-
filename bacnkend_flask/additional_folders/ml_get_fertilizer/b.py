import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv("crop_recommendation.csv")
fertilizer_data = pd.read_csv("FertilizerData.csv")

# Encode Crop names
encoder = LabelEncoder()
data['Crop'] = encoder.fit_transform(data['label'])

# Encode 'Crop' column in fertilizer_data
fertilizer_data['Crop'] = encoder.transform(fertilizer_data['Crop'])

# Merge fertilizer data
data = pd.merge(data, fertilizer_data, on='Crop', how='left')

# Ensure 'Fertilizer' column exists
if 'Fertilizer' not in data.columns:
    data['Fertilizer'] = 'Unknown'  # Placeholder value or handle as needed

# Features and target
X = data[['N', 'P', 'K', 'Crop']]
y = data['Fertilizer']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
print("Training Accuracy:", model.score(X_train, y_train))
print("Testing Accuracy:", model.score(X_test, y_test))

# Example input
user_input = {
    'N': 50,
    'P': 30,
    'K': 20,
    'Crop': 'rice'
}

# Encode the crop name
if user_input['Crop'] in encoder.classes_:
    user_input['Crop'] = encoder.transform([user_input['Crop']])[0]
else:
    raise ValueError(f"Crop '{user_input['Crop']}' is not recognized.")

# Convert input to a DataFrame
input_df = pd.DataFrame([user_input])

# Predict
predicted_fertilizer = model.predict(input_df)
print("Recommended Fertilizer:", predicted_fertilizer)


