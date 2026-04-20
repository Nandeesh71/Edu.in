# ============================================================
# EX.NO: 3 – Polynomial Regression (GHI Dataset)
# ============================================================

"""
AIM
To apply Polynomial Regression to model non-linear relationships and
study the effect of polynomial degree on underfitting/overfitting.
"""

"""
PROCEDURE
1. Generate synthetic GHI dataset with non-linear target formula.
2. Select Undernourishment as single feature for visualization.
3. Split 80:20; transform features with PolynomialFeatures.
4. Train LinearRegression on polynomial features.
5. Evaluate MAE, MSE, R² for degrees 2, 3, 4.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(42)
data = pd.DataFrame({
    "Undernourishment": np.random.uniform(5, 40, 200),
    "ChildWasting":     np.random.uniform(2, 25, 200),
    "ChildStunting":    np.random.uniform(10, 50, 200),
    "ChildMortality":   np.random.uniform(1, 15, 200)
})
data["GHI"] = (0.5*data["Undernourishment"]**2 - 0.3*data["ChildWasting"]
             + 0.2*data["ChildStunting"] + 0.1*data["ChildMortality"]**2
             + np.random.normal(0, 2, 200))

X = data[["Undernourishment"]]
y = data["GHI"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

for deg in [2, 3, 4]:
    poly = PolynomialFeatures(degree=deg)
    Xtr_p, Xte_p = poly.fit_transform(Xtr), poly.transform(Xte)
    mdl = LinearRegression().fit(Xtr_p, ytr)
    yp  = mdl.predict(Xte_p)
    print(f"\nPolynomial Degree: {deg}")
    print("MAE:", mean_absolute_error(yte, yp))
    print("MSE:", mean_squared_error(yte, yp))
    print("R2 :", r2_score(yte, yp))

"""
OUTPUT
Polynomial Degree: 2
MAE: 8.016642169039732   MSE: 86.67263045315755   R2: 0.9984125977139668

Polynomial Degree: 3
MAE: 8.006337541687225   MSE: 85.8495575145922    R2: 0.9984276722289253

Polynomial Degree: 4
MAE: 7.941560255854671   MSE: 85.90949759470602   R2: 0.998426574431158
"""

"""
RESULT
Polynomial Regression successfully modelled the non-linear relationship.
An optimal degree balanced underfitting and overfitting.
"""