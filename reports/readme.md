# Project Report: Training and Test Splitting Project

## Introduction
This project explores the **Ames Housing Dataset** to develop a robust machine learning model for predicting house prices. The focus is on data preprocessing, effective train/test splitting, and model optimization to improve prediction accuracy. The steps follow best practices in data science, ensuring clarity and reproducibility.

---
## Objectives
- Perform data preprocessing to clean and encode data efficiently.
- Implement a structured train/test split strategy for effective model evaluation.
- Build and fine-tune regression models for optimal performance.
- Visualize model predictions to communicate insights effectively.

---
## Data Preparation
### Dataset Overview
The dataset contains **1379 rows** and **80 features**. The target variable is `SalePrice`, representing the property sale price. Key features include:
- **GrLivArea:** Above-ground living area (in square feet)
- **YearBuilt:** Year the house was constructed
- **OverallQual:** Overall quality rating (scale from 1 to 10)
- **GarageCars:** Number of garage spaces

### Key Preprocessing Steps
✅ Handled missing values using median imputation  
✅ Encoded categorical features via one-hot encoding  
✅ Stored cleaned data as `encoded_data.csv` in the `/data/processed_data/` directory

---
## Train/Test Splitting
### Approach
- Split the data into **70% training** and **30% testing** to ensure sufficient data for both model training and evaluation.
- Ensured randomization consistency by setting `random_state=42`.

✅ Saved splits as `X_train.csv`, `X_test.csv`, `y_train.csv`, and `y_test.csv` in the `/data/train_test_splits/` folder.

---
## Model Development
### Scaling
- Utilized **RobustScaler** for scaling numerical features to improve model stability.
- Applied **Winsorization** to reduce outlier impact.

### Modeling
The following techniques were used to enhance model performance:
- **Ridge Regression:** Chosen for its robustness against multicollinearity.
- **GridSearchCV:** Optimized hyperparameters for improved accuracy.

### Performance Metrics
| Metric             | Value |
|:-------------------|:------:|
| Mean Absolute Error (MAE) | **17,450** |
| Root Mean Square Error (RMSE) | **28,900** |
| R-Squared (R²) | **0.87** |

✅ The tuned Ridge Regression model was saved as `best_ridge_model.pkl` in the `/models/` folder.

---
## Results and Insights
- **GrLivArea**, **OverallQual**, and **GarageCars** emerged as the most influential features.
- Removing zero-dominant features significantly improved model performance.
- Outlier control via Winsorization prevented extreme values from distorting predictions.

---
## Visualizations
Key insights were illustrated through visualizations:
- **Scatter Plots:** Predicted vs Actual Sale Prices
- **Error Distribution:** Visualizing prediction error trends

✅ Visuals are available in `05_visualization.ipynb` for reference.

---
## Conclusion
This project successfully implemented data preprocessing, feature engineering, and model tuning strategies. The final Ridge Regression model achieved an **R² score of 0.87**, indicating strong predictive performance.

### Next Steps
- Explore alternative models like XGBoost or RandomForest for improved performance.
- Test additional feature engineering techniques to uncover deeper insights.
- Integrate advanced visualization techniques to enhance communication of insights.

For further details, please refer to the `/notebooks/` directory for comprehensive code walkthroughs.