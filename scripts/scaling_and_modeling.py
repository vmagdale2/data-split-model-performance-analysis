import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mstats

# ## Objectives
# - Perform advanced hyperparameter tuning to improve model performance.
# - Use GridSearchCV to optimize Ridge Regression parameters.
# - Implement data scaling, outlier management, and feature engineering for improved model stability.
# - Compare tuned Ridge model performance with previous results.

# Load data
df_X_train = pd.read_csv('data/train_test_splits/X_train.csv')
df_X_test = pd.read_csv('data/train_test_splits/X_test.csv')
df_y_train = pd.read_csv('data/train_test_splits/y_train.csv').values.ravel()
df_y_test = pd.read_csv('data/train_test_splits/y_test.csv').values.ravel()

# Feature Engineering: Winsorization for Outlier Management
high_variance_features = df_X_train.columns[np.std(df_X_train, axis=0) > 2]
for feature in high_variance_features:
    df_X_train[feature] = mstats.winsorize(df_X_train[feature], limits=[0.01, 0.01])
    df_X_test[feature] = mstats.winsorize(df_X_test[feature], limits=[0.01, 0.01])

# Feature Engineering: Drop zero-dominant features
zero_dominant_features = ['3SsnPorch', 'LowQualFinSF', 'MiscVal', 'PoolArea', 'ScreenPorch']
df_X_train.drop(zero_dominant_features, axis=1, inplace=True)
df_X_test.drop(zero_dominant_features, axis=1, inplace=True)

# Scale the data using RobustScaler
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(df_X_train)
X_test_scaled = scaler.transform(df_X_test)

# Define hyperparameter grid
param_grid = {
    'alpha': [0.1, 1, 10, 50, 100, 200, 500],
    'solver': ['auto', 'saga', 'lsqr'],
    'fit_intercept': [True, False],
    'max_iter': [20000, 50000]  # Increased max_iter for convergence
}

# Initialize Ridge model
ridge_model = Ridge()

# GridSearchCV for Ridge Tuning
grid_search = GridSearchCV(ridge_model, param_grid, cv=5, scoring='neg_mean_squared_error', verbose=3)
grid_search.fit(X_train_scaled, df_y_train)

# Best Ridge Model
best_ridge_model = grid_search.best_estimator_
print(f"Best Ridge Model: {best_ridge_model}")

# Evaluate model
def evaluate_model(model_name, y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f'{model_name} - MSE: {mse:.2f}, MAE: {mae:.2f}, R² Score: {r2:.2f}')

# Predict using best Ridge model
y_pred_best_ridge = best_ridge_model.predict(X_test_scaled)
evaluate_model('Best Ridge Regression', df_y_test, y_pred_best_ridge)

# Save the best model
joblib.dump(best_ridge_model, 'models/best_ridge_model.pkl')
