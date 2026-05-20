# ============================================================
# EX. NO.: 03 - Polynomial Regression
# ============================================================
# AIM:
# Apply Polynomial Regression to model non-linear relationships
# and study how polynomial degree affects model fitting on GHI data.
#
# ALGORITHM:
# 1. Load GHI_Report.csv; select Economy (X) and H_Score (Y).
# 2. Split data 80% train, 20% test.
# 3. For degrees 1 to 4: fit polynomial + linear model, compute
#    Train R², Test R², and RMSE.
# 4. Classify each as Overfitting / Underfitting / Good Fit.
# 5. Plot polynomial curves (2x2 grid) and R² / RMSE comparisons.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load and prepare data
data = pd.read_csv("GHI_Report.csv")
X = data['Economy'].values.reshape(-1, 1)
Y = data['H_Score'].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Test polynomial degrees 1 to 4
degrees = [1, 2, 3, 4]
results = []

print("=" * 55)
print("POLYNOMIAL REGRESSION ANALYSIS")
print("=" * 55)

for deg in degrees:
    poly  = PolynomialFeatures(degree=deg)
    model = LinearRegression().fit(poly.fit_transform(X_train), Y_train)

    train_r2  = model.score(poly.transform(X_train), Y_train)
    test_r2   = model.score(poly.transform(X_test),  Y_test)
    test_rmse = np.sqrt(mean_squared_error(Y_test, model.predict(poly.transform(X_test))))

    if train_r2 - test_r2 > 0.15:
        status = "OVERFITTING"
    elif test_r2 < 0.5:
        status = "UNDERFITTING"
    else:
        status = "GOOD FIT"

    results.append({'deg': deg, 'train_r2': train_r2, 'test_r2': test_r2,
                    'rmse': test_rmse, 'poly': poly, 'model': model})
    print(f"Degree {deg}: Train R²={train_r2:.4f}, Test R²={test_r2:.4f}, "
          f"RMSE={test_rmse:.4f} [{status}]")

best = max(results, key=lambda x: x['test_r2'])
print(f"\nBest Degree: {best['deg']}  (Test R² = {best['test_r2']:.4f})")
print("=" * 55)

# Plot polynomial curves (2x2 grid)
X_range = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for idx, r in enumerate(results):
    ax = axes.flatten()[idx]
    ax.scatter(X_train, Y_train, c='blue', alpha=0.5, s=30, label='Train')
    ax.scatter(X_test,  Y_test,  c='red',  alpha=0.7, s=50, marker='*', label='Test')
    ax.plot(X_range, r['model'].predict(r['poly'].transform(X_range)),
            'g-', linewidth=2, label=f"Deg {r['deg']}")
    ax.set_title(f"Degree {r['deg']}  (R²={r['test_r2']:.3f})")
    ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.show()

# R² and RMSE comparison plots
degs = [r['deg'] for r in results]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(degs, [r['train_r2'] for r in results], 'o-', label='Train R²')
ax1.plot(degs, [r['test_r2']  for r in results], 's-', label='Test R²')
ax1.axvline(x=best['deg'], color='red', linestyle='--', label='Best')
ax1.set_title("R² vs Degree"); ax1.legend(); ax1.grid(True, alpha=0.3)

ax2.plot(degs, [r['rmse'] for r in results], 'o-', color='orange')
ax2.axvline(x=best['deg'], color='red', linestyle='--', label='Best')
ax2.set_title("RMSE vs Degree"); ax2.legend(); ax2.grid(True, alpha=0.3)
plt.tight_layout(); plt.show()

# ============================================================
# OUTPUT:
# Degree 1: Train R²=0.5986, Test R²=0.6419, RMSE=0.7128 [GOOD FIT]
# Degree 2: Train R²=0.6108, Test R²=0.6517, RMSE=0.7030 [GOOD FIT]
# Degree 3: Train R²=0.6153, Test R²=0.6450, RMSE=0.7096 [GOOD FIT]
# Degree 4: Train R²=0.6173, Test R²=0.6546, RMSE=0.7001 [GOOD FIT]
# Best Degree: 4  (Test R² = 0.6546)
# Plots: 2x2 polynomial curves + R²/RMSE comparison charts
#
# RESULT:
# Polynomial Regression applied on GHI data. Degree 4 gave the
# best Test R². Overfitting and underfitting analysis completed.
# ============================================================
