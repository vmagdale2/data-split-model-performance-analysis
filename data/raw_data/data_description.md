# Data Description

This document provides detailed information about the features in the dataset, including data types, descriptive statistics, and usage notes.

| Feature | Data Type | Mean | Std Dev | Min | Q1 | Median | Q3 | Max |
|:--------|:-----------|:------|:--------|:----|:--|:-------|:--|:---|
| 1stFlrSF | float64 | 1177.13 | 387.01 | 438.00 | 894.00 | 1098.00 | 1414.00 | 4692.00 |
| 2ndFlrSF | float64 | 353.42 | 439.55 | 0.00 | 0.00 | 0.00 | 738.50 | 2065.00 |
| 3SsnPorch | float64 | 3.61 | 30.15 | 0.00 | 0.00 | 0.00 | 0.00 | 508.00 |
| BedroomAbvGr | int64 | 2.87 | 0.78 | 0.00 | 2.00 | 3.00 | 3.00 | 6.00 |
| BsmtFinSF1 | float64 | 455.58 | 459.69 | 0.00 | 0.00 | 400.00 | 732.00 | 5644.00 |
| BsmtFinSF2 | float64 | 48.10 | 164.32 | 0.00 | 0.00 | 0.00 | 0.00 | 1474.00 |
| BsmtFullBath | int64 | 0.43 | 0.51 | 0.00 | 0.00 | 0.00 | 1.00 | 2.00 |
| BsmtHalfBath | int64 | 0.06 | 0.24 | 0.00 | 0.00 | 0.00 | 0.00 | 2.00 |
| BsmtUnfSF | float64 | 570.77 | 443.68 | 0.00 | 228.00 | 476.00 | 811.00 | 2336.00 |
| EnclosedPorch | float64 | 21.04 | 60.54 | 0.00 | 0.00 | 0.00 | 0.00 | 552.00 |
| Fireplaces | int64 | 0.64 | 0.65 | 0.00 | 0.00 | 1.00 | 1.00 | 3.00 |
| FullBath | int64 | 1.58 | 0.55 | 0.00 | 1.00 | 2.00 | 2.00 | 3.00 |
| GarageArea | float64 | 500.76 | 185.68 | 160.00 | 380.00 | 484.00 | 580.00 | 1418.00 |
| GarageCars | int64 | 1.87 | 0.63 | 1.00 | 1.00 | 2.00 | 2.00 | 4.00 |
| GarageYrBlt | float64 | 1978.51 | 24.69 | 1900.00 | 1961.00 | 1980.00 | 2002.00 | 2010.00 |
| GrLivArea | float64 | 1534.69 | 519.14 | 438.00 | 1154.00 | 1479.00 | 1790.00 | 5642.00 |
| HalfBath | int64 | 0.40 | 0.50 | 0.00 | 0.00 | 0.00 | 1.00 | 2.00 |
| KitchenAbvGr | int64 | 1.04 | 0.20 | 1.00 | 1.00 | 1.00 | 1.00 | 3.00 |
| LotArea | float64 | 10695.81 | 10214.70 | 1300.00 | 7741.00 | 9591.00 | 11708.50 | 215245.00 |
| LotFrontage | float64 | 75.11 | 28.21 | 21.00 | 60.00 | 71.00 | 88.00 | 405.78 |
| OverallQual | int64 | 6.19 | 1.35 | 2.00 | 5.00 | 6.00 | 7.00 | 10.00 |
| SalePrice | float64 | 185479.51 | 79023.89 | 35311.00 | 134000.00 | 167500.00 | 217750.00 | 755000.00 |

## Key Feature Descriptions
- **SalePrice:** Target variable representing the sale price of the house.
- **GrLivArea:** Above-ground living area (in square feet), an important predictor for housing prices.
- **YearBuilt:** Original construction date of the property.
- **OverallQual:** Rates the overall material and finish quality (scale from 1 to 10).
- **GarageCars:** Number of cars that can fit in the garage.

For more detailed data cleaning steps, refer to the `/notebooks/` directory.

