import matplotlib.pyplot as plt
import pandas as pd

# Replace these values with YOUR project results
models = ['Support Vector Regressor (SVR)', 'K-Nearest Neighbors (KNN)', 'Decision Tree Regressor (DTR)', 'Random Forest Regressor (RFR)', 'MLP Regressor (MLP)']
r2_scores = [-17.8, 52.2, 88.9, 93.20, 2.48]  # Accuracy (R² * 100)
mae = [10.32, 6.84, 2.88, 2.48, 12.42]         # Mean Absolute Error
rmse = [371.79, 150.54, 34.96, 21.36, 307.55]  # Root Mean Squared Error

# Create a DataFrame for table
comparison_table = pd.DataFrame({
    'Model': models,
    'R² Score (%)': r2_scores,
    'MAE': mae,
    'RMSE': rmse
})

# Display the table
print("\nComparison Table of ML Models:\n")
print(comparison_table.to_string(index=False))

# Plot 1: Bar Chart of Accuracy (R² Score)
plt.figure(figsize=(10,6))
plt.bar(models, r2_scores, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.xlabel('Machine Learning Models', fontsize=14)
plt.ylabel('Accuracy (R² Score %)', fontsize=14)
plt.title('Comparison of ML Models Based on Accuracy', fontsize=16)
plt.ylim(0, 100)
plt.xticks(rotation=20, ha='right')
plt.grid(axis='y')
plt.tight_layout()


plt.figtext(0.5, 0.01, "Random Forest Regressor achieved the highest accuracy of 93.20%.", wrap=True, horizontalalignment='center', fontsize=12)

plt.show()

# Plot 2: Line Chart of MAE and RMSE
plt.figure(figsize=(10,6))
plt.plot(models, mae, marker='o', label='MAE', linestyle='--', color='blue')
plt.plot(models, rmse, marker='s', label='RMSE', linestyle='--', color='red')
plt.xlabel('Machine Learning Models', fontsize=14)
plt.ylabel('Error Value', fontsize=14)
plt.title('Model Error Comparison (MAE vs RMSE)', fontsize=16)
plt.legend()
plt.xticks(rotation=20, ha='right')
plt.grid()
plt.tight_layout()


plt.figtext(0.5, 0.01, "Random Forest showed the lowest MAE and RMSE among all models.", wrap=True, horizontalalignment='center', fontsize=12)

plt.show()
