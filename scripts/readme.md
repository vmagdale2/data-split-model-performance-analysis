# Scripts Directory

This folder contains Python scripts that handle various stages of data preparation, model training, and visualization for the **Training and Test Splitting Project**. Each script is modularized to maintain a clean and structured workflow.

## Folder Structure
```
/scripts
│
├── data_preprocessing.py        # Data cleaning and encoding
├── train_test_split.py          # Train/test data splitting
├── scaling_and_modeling.py      # Scaling data and building models
├── fine_tuning.py               # Model fine-tuning and optimization
├── visualization.py             # Visualizing model performance
└── utils.py                     # Utility functions for common tasks
```

## Script Descriptions

### `data_preprocessing.py`
- **Purpose:** Data cleaning, handling missing values, and encoding categorical features.
- **Key Functions:**
  - `load_data()` – Loads the Ames Housing dataset.
  - `handle_missing_values()` – Handles missing data using median, mean, or mode.
  - `one_hot_encode()` – Encodes categorical data for machine learning models.
- **Output:** Saves the processed data as `encoded_data.csv`.

### `train_test_split.py`
- **Purpose:** Splits the dataset into training and testing sets.
- **Key Functions:**
  - `create_train_test_splits()` – Splits data with specified proportions.
- **Output:** Saves train/test splits as `X_train.csv`, `X_test.csv`, `y_train.csv`, and `y_test.csv`.

### `scaling_and_modeling.py`
- **Purpose:** Scales data, implements Ridge Regression, and performs hyperparameter tuning.
- **Key Steps:**
  - Uses `RobustScaler` for scaling
  - Applies `GridSearchCV` for optimal Ridge model selection
  - Performs error analysis (MSE, MAE, R²)
- **Output:** Saves the best model as `best_ridge_model.pkl`.

### `fine_tuning.py`
- **Purpose:** Fine-tunes model performance using advanced scaling techniques.
- **Key Functions:**
  - `scale_data()` – Standardizes key numerical features to improve model performance.
- **Output:** Saves the scaled data as `scaled_data.csv`.

### `visualization.py`
- **Purpose:** Visualizes model performance to assess prediction accuracy.
- **Key Functions:**
  - `plot_predictions()` – Plots predicted vs actual values.

### `utils.py`
- **Purpose:** Contains reusable utility functions to streamline data loading, cleaning, and visualization tasks.
- **Key Functions:**
  - `authenticate_and_load_env()` – Authenticates and loads environment variables.
  - `load_data_from_drive()` – Loads data directly from Google Drive.
  - `handle_missing_values()` – Fills missing data using multiple strategies.
  - `one_hot_encode()` – Encodes categorical data.
  - `create_train_test_splits()` – Splits data into train/test sets.
  - `scale_data()` – Scales data using different scaler types.
  - `calculate_mse()` – Calculates mean squared error.
  - `plot_predictions()` – Visualizes model performance.

## Best Practices
✅ Follow the recommended sequence for running these scripts to ensure accurate results.  
✅ Each script relies on shared utilities in `utils.py`; ensure it is imported where required.  
✅ Document key insights or issues directly within your code comments to enhance clarity.

---
For additional guidance on using these scripts in the workflow, refer to the `/notebooks/` directory.

