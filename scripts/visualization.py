# ==============================
# 📊 Visualizations
# ==============================
# Residual Plot
residuals = y_test - y_pred
plt.figure(figsize=(8, 5))
sns.residplot(x=y_pred, y=residuals, lowess=True, line_kws={'color': 'red', 'lw': 2})
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.title('Residual Plot')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.show()

# Prediction vs Actual Plot
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title('Predicted vs Actual Values')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.grid(True)
plt.show()

# Error Distribution Plot
plt.figure(figsize=(8, 5))
sns.histplot(residuals, kde=True, bins=30)
plt.axvline(residuals.mean(), color='red', linestyle='--', label='Mean')
plt.title('Error Distribution (Residuals)')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Feature Importance Analysis
feature_importance = pd.Series(best_ridge_model.coef_, index=X_train.columns).sort_values(key=abs, ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importance.values, y=feature_importance.index)
plt.title('Feature Importance (Ridge Model)')
plt.xlabel('Coefficient Value (Strength of Impact)')
plt.show()


