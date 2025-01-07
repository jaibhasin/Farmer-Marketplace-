# Marketplace for Farmers

## 🚀 About the Project

Marketplace for Farmers is a bilingual (English/Hindi) platform connecting farmers directly with buyers while empowering farmers with smart technology. Farmers can list their produce and access AI-powered crop recommendations, fertilizer advice, and real-time Mandi prices. Buyers can easily find crops across different states and connect with transportation services. The platform aims to modernize agricultural trade while keeping it accessible and farmer-friendly.

## 🛠️ Features

### For Farmers:

- **Crop Listing:** Farmers can list their crops along with details like quantity, location, pincode, and price per quintal.
- **Get Crop Recommendation Model:** Suggests the most suitable crop based on soil and environmental factors using machine learning.
- **Fertilizer Recommendation Model:** Recommends optimal fertilizers based on soil nutrient levels and desired crop to grow.
- **Mandi Prices:** Provides the latest market prices using a government API.
- **Crop Timeline:** Offers detailed crop timelines to assist farmers in planning their agricultural activities.
- **Weather Forecast Links:** Directs farmers to trusted weather forecast channels for better planning.

### For Buyers:

- **Crop Selection:** Buyers can select crops and quantities, and the platform lists available farmers along with their prices and locations.
- **Transportation Assistance:** Includes a curated list of transportation companies to ease logistics.

## 📸 Screenshots
<img src="https://github.com/user-attachments/assets/e8be7b07-49ce-4b94-a530-1d7a01b8fa1a" width="700"/>
<img src="https://github.com/user-attachments/assets/5e877077-1566-4d98-baee-3ae637731ac4" width="700"/>
<img src="https://github.com/user-attachments/assets/dea22695-b128-4264-b273-ef1ac298ec56" width="700"/>
<img src="https://github.com/user-attachments/assets/9cf53036-6423-42a6-98f7-b5f06aeb0e1a" width="700"/>

## 💻 Tech Stack

- **Client Side:** Express.js
- **Server Side:** Flask
- **Machine Learning Models:** Logistic Regression, Random Forest, XGBoost

## ⚙️ Machine Learning Models

### 1. **Crop Recommendation Model**

- **Purpose:** Suggests the most suitable crop based on soil and environmental conditions (e.g., Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall).
- **Techniques Used:**
  - Logistic Regression
  - Random Forest Classifier
  - XGBoost Classifier
- **Key Features:**
  - Majority voting mechanism for robust predictions.
  - Data preprocessing with LabelEncoder and StandardScaler.
  - Accuracy and reliability evaluation with metrics like accuracy score and confusion matrices.
  - Deployment with pickle for efficient model reuse.
  - Trained on [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) 
### 2. **Fertilizer Recommendation Model**

- **Purpose:** Suggests the appropriate fertilizers based on soil nutrient levels and crop requirements.
- **Key Features:**
  - Analyzes soil Nitrogen (N), Phosphorus (P), and Potassium (K) levels.
  - Recommends fertilizers to address nutrient deficiencies dynamically.
  - Trained on [Fertilizer Recommendation Dataset](https://github.com/Gladiator07/Harvestify/blob/master/Data-processed/fertilizer.csv)
  


## ⚙️ Installation

### Prerequisites

- Python 3.12+
- Flask
- Node.js
- Required Python libraries (specified in `requirements.txt`)

### Steps to Set Up

1. Clone the repository:
   ```bash
   git clone https://github.com/jaibhasin/Marketplace-for-Farmers.git
2. Navigate to the project directory:
   ```bash
   cd marketplace-for-farmers
3. Run the Flask backend:
   ```bash
   cd Backend
   python app.py
4. Navigate to the frontend directory and install dependencies:
   ```bash
   cd frontend
   npm install
5. Run the frontend server:
   ```bash
   npm run dev

## 🧑‍💻 Usage
- Farmers: Log in to list crops, get crop recommendations, get help regarding which fertilizers to use ,and access latest market prices.

- Buyers: Browse crop listings, select crops, and connect with farmers.

## 🤝 Contributing
Contributions are welcome! Follow these steps:

1. Fork the project.

2. Create a feature branch (git checkout -b feature-name).

3. Commit your changes (git commit -m 'Add feature').

4. Push to the branch (git push origin feature-name).

5. Open a pull request.

## 🛡️ Security
If you discover a security vulnerability, please report it by creating an issue in the repository.

## 🙌 Acknowledgements
- Government API for Mandi Prices

- Datasets: [Fertilizer Recommendation Dataset](https://github.com/Gladiator07/Harvestify/blob/master/Data-processed/fertilizer.csv) [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) 

-  Krish Naik's [YouTube Video](https://www.youtube.com/watch?v=zJcSod-L-Ps) for making Crop Prediction and Fertilizers Recommendation Models
   

## 📧 Contact
Name: Jai Bhasin

Email: bhasinjai@gmail.com

GitHub: jaibhasin


