from utils import create_train_test_splits
import pandas as pd

# Load encoded data
df_encoded = pd.read_csv('data/processed_data/encoded_data.csv')
X = df_encoded.drop('SalePrice', axis=1)
y = df_encoded['SalePrice']

# Split the data
X_train, X_test, y_train, y_test = create_train_test_splits(X, y)

X_train.to_csv('data/train_test_splits/X_train.csv', index=False)
X_test.to_csv('data/train_test_splits/X_test.csv', index=False)
y_train.to_csv('data/train_test_splits/y_train.csv', index=False)
y_test.to_csv('data/train_test_splits/y_test.csv', index=False)