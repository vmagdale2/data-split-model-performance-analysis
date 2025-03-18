from utils import scale_data
import pandas as pd

# Load data
df = pd.read_csv('data/processed_data/encoded_data.csv')
df_scaled = scale_data(df, columns=['1stFlrSF', 'TotalBsmtSF'], scaler_type='StandardScaler')
df_scaled.to_csv('data/processed_data/scaled_data.csv', index=False)