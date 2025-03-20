# Data Folder

This folder contains all the datasets and data-related files required for the **Training and Test Splitting Project**. Each file is essential for data preprocessing, model training, and evaluation. Below is an overview of the contents of this folder, including details on each file's purpose and usage.

## Folder Structure
```
/data
│
├── Ames_Housing_Sales.csv
├── encoded_data.csv
├── raw_data/               # Original unprocessed data
├── processed_data/         # Cleaned and transformed data
├── train_test_splits/      # Data splits for model evaluation
└── data_description.md     # Detailed description of data features
```

## File Descriptions

### `Ames_Housing_Sales.csv`
- **Description:** This is the primary dataset for the project. It contains information about property sales in Ames, Iowa, with features such as house characteristics, location details, and sale price.
- **Source:** [Ames Housing Dataset](http://jse.amstat.org/v19n3/decock.pdf)
- **Usage:** Utilized for preprocessing, encoding, and modeling throughout the project.

### `encoded_data.csv`
- **Description:** This file contains the Ames Housing dataset after categorical encoding and other preprocessing steps.
- **Usage:** Used as the transformed dataset for streamlined modeling and feature engineering.

### `/raw_data/`
- **Description:** Contains original data files in their unaltered state. These files should remain untouched to ensure reproducibility.
- **Recommended Files:** Store backups of downloaded datasets here.

### `/processed_data/`
- **Description:** Includes cleaned and transformed data files ready for model development and analysis.
- **Contents:**
  - Files like `data_cleaned.csv` or `data_transformed.csv` may be stored here after outlier handling, skew transformation, and scaling.

### `train_test_splits`
- **Description:** Contains the train and test data files generated during data splitting procedures.
- **Recommended Naming Convention:** `train_data.csv`, `test_data.csv`, etc.

### `data_description.md`
- **Description:** Provides detailed documentation of each feature, its data type, and its role in modeling.
- **Recommended Content:** Include information on categorical variables, encoded values, and any transformations applied.
