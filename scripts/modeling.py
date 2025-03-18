from sklearn.linear_model import LinearRegression
from utils import calculate_mse
import pandas as pd

# Load train/test data
X_train = pd.read_csv('data/train_test_splits/X_train.csv')
X_test = pd.read_csv('data/train_test_splits/X_test.csv')
y_train = pd.read_csv('data/train_test_splits/y_train.csv')
y_test = pd.read_csv('data/train_test_splits/y_test.csv')

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Error Calculation
print(f'Training MSE: {calculate_mse(y_train, y_train_pred)}')
print(f'Test MSE: {calculate_mse(y_test, y_test_pred)}')
