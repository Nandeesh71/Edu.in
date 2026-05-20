# ============================================================
# EX. NO.: 01 - Data Preprocessing Techniques
# ============================================================
# AIM:
# Explore NumPy and Pandas for data preprocessing — handling
# missing values, outliers, and encoding for ML models.
#
# ALGORITHM:
# 1. Load dataset into a Pandas DataFrame.
# 2. Fill missing numerical values with mean using SimpleImputer.
# 3. Apply One-Hot Encoding on categorical column.
# 4. Split data into 80% train and 20% test sets.
# ============================================================

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

# Load Dataset
dataset = pd.read_csv("Data_preprocessing.csv")
print("Missing Values:\n", dataset.isnull().sum())

# Separate features and target
x = dataset.iloc[:, 0:3].values
y = dataset.iloc[:, 3:4].values

# Fill missing numerical values with mean
imputer = SimpleImputer(strategy='mean')
x[:, 1:3] = imputer.fit_transform(x[:, 1:3])

# One-Hot Encode categorical column (index 0)
ct = ColumnTransformer(
    transformers=[('onehot', OneHotEncoder(), [0])],
    remainder='passthrough'
)
x = ct.fit_transform(x)
x = x[:, 1:]  # Drop first dummy to avoid multicollinearity

# Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=0
)

print("\nx_train shape:", x_train.shape)
print("x_test shape :", x_test.shape)
print("y_train:\n", y_train)
print("y_test:\n",  y_test)

# ============================================================
# OUTPUT:
# Missing Values: count of nulls per column
# x_train / x_test: encoded numeric feature arrays
# y_train / y_test: target label arrays (Yes / No)
#
# RESULT:
# Data preprocessing using NumPy and Pandas was successfully
# executed. Missing values handled, one-hot encoding applied,
# and data split into train/test sets.
# ============================================================
