# ============================================================
# EX. NO.: 02 - Simple Linear and Multiple Linear Regression
# ============================================================
# AIM:
# Implement Simple and Multiple Linear Regression to predict
# Happiness Score using the GHI dataset.
#
# ALGORITHM:
# 1. Load GHI_Report.csv dataset.
# 2. Select Economy for simple regression; Economy, Fam,
#    Health, Freedom for multiple regression.
# 3. Train both models using LinearRegression.
# 4. Calculate RMSE and R² for both models.
# 5. Plot Simple regression line and Multiple regression
#    Actual vs Predicted scatter plot.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load Dataset
df = pd.read_csv("GHI_Report.csv")
Y = df['H_Score'].values

# ── Simple Linear Regression ──────────────────────────────
X_simple = df[['Economy']].values
simple_model = LinearRegression().fit(X_simple, Y)
Y_simple_pred = simple_model.predict(X_simple)

rmse_simple = np.sqrt(mean_squared_error(Y, Y_simple_pred))
r2_simple   = simple_model.score(X_simple, Y)

print("--- Simple Linear Regression ---")
print("Slope    :", simple_model.coef_[0])
print("Intercept:", simple_model.intercept_)
print("RMSE     :", rmse_simple)
print("R² Score :", r2_simple)

plt.figure()
plt.scatter(X_simple, Y, marker='*', label="Actual Data")
plt.plot(X_simple, Y_simple_pred, 'b-', label="Regression Line")
plt.xlabel("Economy")
plt.ylabel("H_Score")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()

# ── Multiple Linear Regression ────────────────────────────
features = ['Economy', 'Fam', 'Health', 'Freedom']
X_multi  = df[features].values
multi_model = LinearRegression().fit(X_multi, Y)
Y_multi_pred = multi_model.predict(X_multi)

rmse_multi = np.sqrt(mean_squared_error(Y, Y_multi_pred))
r2_multi   = multi_model.score(X_multi, Y)

print("\n--- Multiple Linear Regression ---")
for f, c in zip(features, multi_model.coef_):
    print(f"Coefficient for {f}: {c}")
print("Intercept:", multi_model.intercept_)
print("RMSE     :", rmse_multi)
print("R² Score :", r2_multi)

plt.figure()
plt.scatter(Y, Y_multi_pred, marker='o')
plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], 'r--')
plt.xlabel("Actual H_Score")
plt.ylabel("Predicted H_Score")
plt.title("Multiple Linear Regression: Actual vs Predicted")
plt.show()

# ============================================================
# OUTPUT:
# Simple  → Slope: 2.18, Intercept: 3.49, RMSE: 0.71, R²: 0.60
# Multiple→ Coefficients for each feature, RMSE: 0.54, R²: 0.76
# Plots   → Scatter + regression line / Actual vs Predicted
#
# RESULT:
# Simple and Multiple Linear Regression were implemented on
# the GHI dataset. Model training, validation, and performance
# evaluation completed successfully.
# ============================================================
