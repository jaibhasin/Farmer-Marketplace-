# Farmers App

## Overview

The Farmers App is a comprehensive platform designed to assist farmers and users in managing agricultural activities and sell their produce online. The app provides features such as crop prediction, fertilizer recommendation, and access to market prices. It also supports multiple languages to cater to a diverse user base.

## Project Structure

## Backend

The backend is built using Flask and provides APIs for crop prediction, fertilizer recommendation, and user management.

### Key Files

- `app.py`: Entry point for the Flask application.
- `myproject/ml_model.py`: Contains the `predict_crop` function for crop prediction.
- `myproject/final_model_fertlizer.py`: Contains the `user_input` function for fertilizer recommendation.
- `myproject/models.py`: Defines the database models.
- `migrations/`: Contains migration files for database schema changes.

### Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Set up the database:
    ```sh
    flask db upgrade
    ```

3. Run the application:
    ```sh
    flask run
    ```

## Frontend

The frontend is built using React and Vite, providing a user-friendly interface for interacting with the backend services.

### Key Files

- [App.jsx](http://_vscodecontentref_/10): Main application component.
- [src/Pages/](http://_vscodecontentref_/11): Contains various pages like `UserSignup`, `UserSignin`, [HomePage](http://_vscodecontentref_/12), etc.
- [src/Components/](http://_vscodecontentref_/13): Contains reusable components like [NavBar](http://_vscodecontentref_/14), [User_NavBar](http://_vscodecontentref_/15), etc.
- [src/atoms/](http://_vscodecontentref_/16): Contains Recoil atoms for state management.
- [src/Helping Componjents/](http://_vscodecontentref_/17): Contains helper components and data files.

### Setup

1. Install dependencies:
    ```sh
    npm install
    ```

2. Run the development server:
    ```sh
    npm run dev
    ```

## Features

- **User Authentication**: Sign up and sign in for both farmers and users.
- **Crop Prediction**: Predict the most suitable crop based on soil and weather conditions.
- **Fertilizer Recommendation**: Recommend the best fertilizer based on soil nutrients and crop type.
- **Market Prices**: View the latest market prices for various crops.
- **Multi-language Support**: Switch between English and Hindi.

## API Endpoints

- **Crop Prediction**: `/get_crop`
- **Fertilizer Recommendation**: `/get_fertilizer`

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.
