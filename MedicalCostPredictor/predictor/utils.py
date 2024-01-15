# utils.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib

def load_and_preprocess_data(file_path='insurance.csv'):
    # Load your data
    data = pd.read_csv(file_path)

    # Preprocess the data
    X = data.drop('charges', axis=1)
    Y = data['charges']

    return X, Y

def train_linear_regression(X_train, Y_train):
    # Train a linear regression model
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)

    return regressor

def save_model(model, model_filename='linear_regression_model.joblib'):
    # Save the trained model
    joblib.dump(model, model_filename)
