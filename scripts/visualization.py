from utils import plot_predictions
import pandas as pd

# Load predictions
y_test = pd.read_csv('data/train_test_splits/y_test.csv')
y_test_pred = pd.read_csv('data/train_test_splits/y_test.csv')  # Placeholder for actual predictions

# Visualization
plot_predictions(y_test, y_test_pred)