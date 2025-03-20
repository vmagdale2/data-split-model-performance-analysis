----------
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
X_train = pd.read_csv('/mnt/data/X_train.csv')
X_test = pd.read_csv('/mnt/data/X_test.csv')
y_train = pd.read_csv('/mnt/data/y_train.csv').values.ravel()
y_test = pd.read_csv('/mnt/data/y_test.csv').values.ravel()

# 📌 Scaling the Data (RobustScaler for Outlier Resistance)
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 📌 Ridge Regression with GridSearchCV (Logarithmic Range)
param_grid = {'alpha': np.logspace(-2, 3, 10)}  # From 0.01 to 1000
ridge_grid = GridSearchCV(Ridge(), param_grid, cv=5)
ridge_grid.fit(X_train_scaled, y_train)

# Best Model
best_ridge_model = ridge_grid.best_estimator_
print(f"✅ Best Alpha: {ridge_grid.best_params_['alpha']}")

# 📌 Model Evaluation
y_pred = best_ridge_model.predict(X_test_scaled)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared (R²): {r2:.2f}")

# 📌 Saving the Model and Predictions
y_pred_df = pd.DataFrame(y_pred, columns=['Predicted_Values'])
y_pred_df.to_csv('/mnt/data/y_pred.csv', index=False)

joblib.dump(best_ridge_model, '/mnt/data/best_ridge_model.pkl')
print("✅ Model successfully saved as 'best_ridge_model.pkl'")

