# data-split-model-performance-analysis

## Predictive Modeling Mastery: Splitting, Scaling, and Analysis

### Description

This project demonstrates effective data preprocessing, feature engineering, model training, and evaluation using the **Ames Housing Dataset**. The focus is on implementing best practices for data preparation, train/test splitting, and model fine-tuning to ensure reproducibility and accuracy in machine learning workflows.

## Project Structure
```
├── data/                     # Dataset and processed files
│   ├── raw_data/             # Original unaltered dataset
│   ├── processed_data/       # Cleaned and transformed data
│   ├── train_test_splits/    # Train/test data splits
│   ├── Ames_Housing_Sales.csv # Primary dataset
│   └── data_description.md   # Detailed feature descriptions
│
├── notebooks/                # Jupyter notebooks for analysis and modeling
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_train_test_split.ipynb
│   ├── 03_scaling_and_modeling_analysis.ipynb
│   ├── 04_fine_tuning.ipynb
│   └── 05_visualization.ipynb
│
├── scripts/                  # Python scripts for modularized tasks
│   ├── data_preprocessing.py
│   ├── train_test_split.py
│   ├── scaling_and_modeling.py
│   ├── fine_tuning.py
│   ├── visualization.py
│   └── utils.py
│
├── .env                      # Environment variables for secure access
├── .gitignore                # Files and folders to exclude from version control
├── requirements.txt          # Required dependencies for the project
└── README.md                 # Project documentation
```

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/training-test-split.git
   cd training-test-split
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # For Mac/Linux
   .\venv\Scripts\activate       # For Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file for secure credentials (e.g., Google Drive API keys).

## Usage

### Step 1: Data Preprocessing
Run the following script to clean and encode the dataset:
```bash
python scripts/data_preprocessing.py
```

### Step 2: Train/Test Split
Split the dataset for model training and evaluation:
```bash
python scripts/train_test_split.py
```

### Step 3: Scaling and Modeling
Scale the data and build regression models:
```bash
python scripts/scaling_and_modeling.py
```

### Step 4: Fine-tuning
Optimize model performance using hyperparameter tuning:
```bash
python scripts/fine_tuning.py
```

### Step 5: Visualization
Generate insightful visualizations of predictions:
```bash
python scripts/visualization.py
```

## Key Features
✅ Structured workflow for data cleaning, encoding, and feature engineering  
✅ Efficient train/test splitting for effective model evaluation  
✅ Robust model tuning and error analysis using GridSearchCV  
✅ Clean visualization for improved insights into model performance  
✅ Modularized Python scripts for improved maintainability  

## Results
- Key insights and performance metrics are visualized in the `05_visualization.ipynb` notebook.
- The final model and best parameters are saved in the `/models/` directory for easy deployment.


## License
This project is licensed under the MIT License.

---
For further inquiries or collaboration opportunities, please feel free to reach out!





