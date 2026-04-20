# ============================================================
# EX.NO: 1 – NumPy & Pandas Data Pre-processing
# ============================================================

"""
AIM
To implement data preprocessing using NumPy and Pandas by handling
missing data, outliers, and encoding categorical variables.
"""

"""
PROCEDURE
A. Handling Missing Data
   1. Load dataset into a Pandas DataFrame.
   2. Identify missing values using isnull() / isna().
   3. Fill missing numerical values with mean/median.
   4. Fill missing categorical values with mode.
   5. Optionally drop rows/columns with dropna().

B. Detecting & Handling Outliers (IQR Method)
   1. Compute Q1, Q3, IQR = Q3 - Q1.
   2. Lower bound = Q1 - 1.5*IQR; Upper bound = Q3 + 1.5*IQR.
   3. Cap values outside bounds.

C. Encoding Categorical Data
   1. Apply Label Encoding for ordinal categories.
   2. Apply One-Hot Encoding (pd.get_dummies) for nominal categories.

D. Final Dataset Preparation
   1. Verify no missing values remain.
   2. Combine processed features ready for ML.
"""

import numpy as np
import pandas as pd

data = {
    "Age":        [25, 28, np.nan, 32, 100, 29],
    "Salary":     [50000, np.nan, 45000, 52000, 51000, 700000],
    "Department": ["HR", "IT", "IT", np.nan, "Finance", "HR"]
}
df = pd.DataFrame(data)
print("Original Data:\n", df)

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)
df["Department"].fillna(df["Department"].mode()[0], inplace=True)

Q1, Q3 = df["Salary"].quantile(0.25), df["Salary"].quantile(0.75)
IQR = Q3 - Q1
lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
df["Salary"] = np.where(df["Salary"] > upper, upper,
               np.where(df["Salary"] < lower, lower, df["Salary"]))

df_encoded = pd.get_dummies(df, columns=["Department"])
print("\nProcessed Data:\n", df_encoded)

"""
OUTPUT
Original Data:
    Age    Salary Department
0  25.0   50000.0         HR
1  28.0       NaN         IT
2   NaN   45000.0         IT
3  32.0   52000.0        NaN
4 100.0   51000.0    Finance
5  29.0  700000.0         HR

Processed Data:
    Age   Salary  Department_Finance  Department_HR  Department_IT
0  25.0  50000.0               False           True          False
1  28.0  51000.0               False          False           True
2  42.8  48000.0               False          False           True
3  32.0  52000.0               False           True          False
4 100.0  51000.0                True          False          False
5  29.0  54000.0               False           True          False
"""

"""
RESULT
The dataset was successfully pre-processed by handling missing values,
treating outliers, encoding categorical variables, and generating a
clean dataset ready for machine learning.
"""