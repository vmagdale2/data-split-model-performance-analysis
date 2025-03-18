import pandas as pd
from utils import load_data, handle_missing_values, one_hot_encode

# Load and process data
df = load_data('/content/drive/MyDrive/Professional/Portfolio/test_split/Ames_Housing_Sales.csv')
df = handle_missing_values(df)
df_encoded = one_hot_encode(df)

df_encoded.to_csv('data/processed_data/encoded_data.csv', index=False)
