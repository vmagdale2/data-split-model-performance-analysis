# utils.py - Utility Functions for Data Processing and Analysis

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

import os
import io
import pandas as pd
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from dotenv import load_dotenv
from google.auth import default

# Authenticate and Load .env Variables
def authenticate_and_load_env():
    auth.authenticate_user()
    load_dotenv("/content/drive/MyDrive/Professional/Portfolio/test_split/.env_drive")
    creds, _ = default()
    service = build('drive', 'v3', credentials=creds)
    print("✅ Google Drive API authenticated successfully!")
    return service

# Load Data from Google Drive
def load_data_from_drive(service, file_id):
    try:
        request = service.files().get_media(fileId=file_id)
        file_content = io.BytesIO()
        downloader = MediaIoBaseDownload(file_content, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()

        file_content.seek(0)

        # Fix: Correct CSV decoding
        decoded_content = file_content.read().decode('utf-8')

        # Fix: Load data as DataFrame directly from string buffer
        df = pd.read_csv(io.StringIO(decoded_content))

        print("✅ Data loaded successfully!")
        return df

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

# Function to handle missing values
def handle_missing_values(df, method='median'):
    """Fill missing values using specified method for numeric columns only."""
    if method == 'median':
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].median(), inplace=True)
    elif method == 'mean':
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].mean(), inplace=True)
    elif method == 'mode':
        for col in df.columns:  # Mode works for both numeric and non-numeric data
            df[col].fillna(df[col].mode().iloc[0], inplace=True)
    else:
        raise ValueError("Invalid method. Choose 'median', 'mean', or 'mode'.")
    return df

# Function to perform one-hot encoding
def one_hot_encode(df, drop_first=True):
    """Perform one-hot encoding for categorical features."""
    categorical_cols = df.select_dtypes(include=['object']).columns
    return pd.get_dummies(df, columns=categorical_cols, drop_first=drop_first)

# Function to create train/test split
def create_train_test_splits(X, y, test_size=0.3, random_state=42):
    """Split data into train and test sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# Function to scale data
def scale_data(df, columns, scaler_type='StandardScaler'):
    """Apply chosen scaler to selected columns."""
    scaler = StandardScaler() if scaler_type == 'StandardScaler' else MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[columns] = scaler.fit_transform(df[columns])
    return df_scaled

# Function to calculate mean squared error
def calculate_mse(y_true, y_pred):
    """Calculate Mean Squared Error."""
    return mean_squared_error(y_true, y_pred)

# Function to visualize predictions vs actual values
def plot_predictions(y_true, y_pred):
    """Plot predicted values against actual values."""
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, y_pred, alpha=0.3)
    plt.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)], color='red', linestyle='--')
    plt.title('Predictions vs Actual Values')
    plt.xlabel('Actual Values')
    plt.ylabel('Predictions')
    plt.show()
