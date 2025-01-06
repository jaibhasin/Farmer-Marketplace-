import numpy as np
import pandas as pd 

import os
for dirname, _, filenames in os.walk('./kaggle/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

data=pd.read_csv('./kaggle/input1.csv')
print(data)


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

print(data.isnull().sum())  # Check for any missing values

# Encode the 'label' column (crops)
label_encoder = LabelEncoder()
data['label'] = label_encoder.fit_transform(data['label'])

# Define features and target
X = data.drop('label', axis=1)  # Features (N, P, K, etc.)
y = data['label']  # Target (encoded labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Initialize and train the Logistic Regression model
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train_scaled, y_train)

# Predictions
y_pred_logreg = logreg.predict(X_test_scaled)

# Evaluation
print("Logistic Regression Accuracy: ", accuracy_score(y_test, y_pred_logreg))
print(classification_report(y_test, y_pred_logreg))

from sklearn.ensemble import RandomForestClassifier

# Initialize and train Random Forest model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predictions
y_pred_rf = rf.predict(X_test)

# Evaluation
print("Random Forest Accuracy: ", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))
import xgboost as xgb

# Initialize and train XGBoost model
xgb_model = xgb.XGBClassifier(objective='multi:softmax', num_class=len(set(y)), random_state=42)
xgb_model.fit(X_train_scaled, y_train)

# Predictions
y_pred_xgb = xgb_model.predict(X_test_scaled)

# Evaluation
print("XGBoost Accuracy: ", accuracy_score(y_test, y_pred_xgb))
print(classification_report(y_test, y_pred_xgb))

from sklearn.metrics import confusion_matrix, roc_auc_score

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay

# Confusion Matrix for Logistic Regression
cm_logreg = confusion_matrix(y_test, y_pred_logreg)

# Plot confusion matrix using Seaborn
plt.figure(figsize=(12, 4))
sns.heatmap(cm_logreg, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title('Confusion Matrix (Logistic Regression)')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()


cm_rf = confusion_matrix(y_test, y_pred_rf)

# Plot confusion matrix using Seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title('Confusion Matrix (Logistic Regression)')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()



cm_gb = confusion_matrix(y_test, y_pred_xgb)

# Plot confusion matrix using Seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(cm_gb, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title('Confusion Matrix (Logistic Regression)')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()


y_pred_logreg = logreg.predict(X_test_scaled)

# Convert numerical predictions back to crop names using the label encoder
predicted_crops_logreg = label_encoder.inverse_transform(y_pred_logreg)

# Convert actual labels back to crop names
actual_crops = label_encoder.inverse_transform(y_test)

# Create a DataFrame to display predicted vs actual
import pandas as pd

comparison_df = pd.DataFrame({
    'Actual Crop': actual_crops,
    'Predicted Crop': predicted_crops_logreg
})

# Display the first 10 rows of actual vs predicted crops
print(comparison_df.head(10))


y_pred_xgb = xgb_model.predict(X_test_scaled)

# Convert numerical predictions back to crop names using the label encoder
predicted_crops_xgb = label_encoder.inverse_transform(y_pred_xgb)

# Convert actual labels back to crop names
actual_crops = label_encoder.inverse_transform(y_test)

# Create a DataFrame to display predicted vs actual for XGBoost
comparison_df_xgb = pd.DataFrame({
    'Actual Crop': actual_crops,
    'Predicted Crop': predicted_crops_xgb
})

# Display the first 10 rows of actual vs predicted crops
print("XGBoost - Actual vs Predicted Crops:")
print(comparison_df_xgb.head(10))


y_pred_rf = rf.predict(X_test)

# Convert numerical predictions back to crop names using the label encoder
predicted_crops_rf = label_encoder.inverse_transform(y_pred_rf)

# Convert actual labels back to crop names
actual_crops = label_encoder.inverse_transform(y_test)

# Create a DataFrame to display predicted vs actual for Random Forest
comparison_df_rf = pd.DataFrame({
    'Actual Crop': actual_crops,
    'Predicted Crop': predicted_crops_rf
})

# Display the first 10 rows of actual vs predicted crops
print("Random Forest - Actual vs Predicted Crops:")
print(comparison_df_rf.head(10))
