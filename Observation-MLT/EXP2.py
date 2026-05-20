# ============================================================
# EX.NO: 2 – Linear & Multiple Linear Regression (GHI Dataset)
# ============================================================

"""
AIM
To implement Simple Linear Regression and Multiple Linear Regression
to predict the Global Hunger Index (GHI) using key hunger indicators.
"""

"""
PROCEDURE
1. Generate synthetic GHI dataset (Undernourishment, ChildWasting,
   ChildStunting, ChildMortality).
2. Compute GHI as weighted combination + noise.
3. Simple LR: one predictor (Undernourishment) → GHI; 80:20 split.
4. Evaluate using MAE, MSE, R².
5. Multiple LR: all four predictors → GHI; same split.
6. Evaluate and plot Actual vs Predicted.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(42)
data = pd.DataFrame({
    "Undernourishment": np.random.uniform(5, 40, 200),
    "ChildWasting":     np.random.uniform(2, 25, 200),
    "ChildStunting":    np.random.uniform(10, 50, 200),
    "ChildMortality":   np.random.uniform(1, 15, 200)
})
data["GHI"] = (0.25*data["Undernourishment"] + 0.25*data["ChildWasting"]
             + 0.25*data["ChildStunting"]    + 0.25*data["ChildMortality"]
             + np.random.normal(0, 1.5, 200))

print("Synthetic GHI Dataset:\n", data.head())

y = data["GHI"]

# Simple LR
X_s = data[["Undernourishment"]]
Xtr_s, Xte_s, ytr_s, yte_s = train_test_split(X_s, y, test_size=0.2, random_state=42)
slr = LinearRegression().fit(Xtr_s, ytr_s)
yp_s = slr.predict(Xte_s)
print("\n--- Simple LR ---")
print("MAE:", mean_absolute_error(yte_s, yp_s))
print("MSE:", mean_squared_error(yte_s, yp_s))
print("R2 :", r2_score(yte_s, yp_s))

# Multiple LR
X_m = data[["Undernourishment","ChildWasting","ChildStunting","ChildMortality"]]
Xtr_m, Xte_m, ytr_m, yte_m = train_test_split(X_m, y, test_size=0.2, random_state=42)
mlr = LinearRegression().fit(Xtr_m, ytr_m)
yp_m = mlr.predict(Xte_m)
print("\n--- Multiple LR ---")
print("MAE:", mean_absolute_error(yte_m, yp_m))
print("MSE:", mean_squared_error(yte_m, yp_m))
print("R2 :", r2_score(yte_m, yp_m))

"""
OUTPUT
Synthetic GHI Dataset:
   Undernourishment  ChildWasting  ChildStunting  ChildMortality        GHI
0         18.108904     16.766728      14.124955        3.365091  11.905708
1         38.275001      3.935219      46.102116        4.900265  24.010353
2         30.619788      5.717460      30.210095        3.478147  20.329409
3         25.953047     22.666746      43.058299        2.241835  25.498112
4         10.460652     15.947868      22.801984        2.688902  15.364632

--- Simple LR ---
MAE: 3.041983782620014
MSE: 14.956599744135037
R2 : 0.34734049973251757

--- Multiple LR ---
MAE: 1.1059453765970535
MSE: 1.8504677196206836
R2 : 0.9192513433661731
"""

"""
RESULT
Simple and Multiple Linear Regression were successfully implemented.
Multiple LR produced better accuracy by using all four predictors.
"""