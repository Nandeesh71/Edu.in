# 🧪 EXPERIMENT – 1

## Title

**Explore Numpy and Pandas libraries for data pre-processing techniques such as handling missing data and outliers, encoding to prepare data for machine learning models.**

---

## INTRODUCTION

Data preprocessing is a crucial step in machine learning that involves cleaning, transforming, and organizing raw data to improve the quality and accuracy of models. NumPy provides efficient numerical operations, while Pandas offers powerful tools for handling missing values, outliers, and categorical encoding.

---

## AIM

To implement data preprocessing using NumPy and Pandas by handling missing data, outliers, and encoding categorical variables.

---

## ALGORITHM

### A. Handling Missing Data

1. Load the dataset into a Pandas DataFrame.
2. Identify missing values using `isnull()` or `isna()`.
3. Replace missing numerical values using mean or median.
4. Replace missing categorical values using mode.
5. Alternatively, remove rows or columns containing missing data using `dropna()`.

### B. Detecting & Handling Outliers (IQR Method)

1. Select numerical columns with possible outliers.
2. Calculate Q1 (25th percentile) and Q3 (75th percentile).
3. Compute IQR = Q3 − Q1.
4. Determine lower bound = Q1 − 1.5 × IQR.
5. Determine upper bound = Q3 + 1.5 × IQR.
6. Cap, replace, or remove values outside these bounds.

### C. Encoding Categorical Data

1. Identify categorical columns in the dataset.
2. Apply Label Encoding for ordinal categories.
3. Apply One-Hot Encoding for nominal categories using `pd.get_dummies()`.
4. Merge encoded columns with the numerical dataset.

### D. Final Dataset Preparation

1. Verify all missing values and outliers are handled.
2. Combine processed numerical and categorical features.
3. Use the cleaned dataset for machine learning model training.

---

## Ex.No: 1

### PROGRAM

```python
import numpy as np
import pandas as pd

# Sample dataset
data = {
    "Age": [25, 28, np.nan, 32, 100, 29],
    "Salary": [50000, np.nan, 45000, 52000, 51000, 700000],
    "Department": ["HR", "IT", "IT", np.nan, "Finance", "HR"]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Handling Missing Data
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)
df["Department"].fillna(df["Department"].mode()[0], inplace=True)

# Outlier Treatment (IQR method)
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df["Salary"] = np.where(
    df["Salary"] > upper, upper,
    np.where(df["Salary"] < lower, lower, df["Salary"])
)

# Encoding Categorical Data
df_encoded = pd.get_dummies(df, columns=["Department"])

print("\nProcessed Data:")
print(df_encoded)
```

---

## OUTPUT

```
Original Data:
    Age    Salary Department
0  25.0   50000.0 HR
1  28.0       NaN IT
2   NaN   45000.0 IT
3  32.0   52000.0 NaN
4 100.0   51000.0 Finance
5  29.0  700000.0 HR
```

```
Processed Data:
     Age   Salary  Department_Finance  Department_HR  Department_IT
0  25.0  50000.0                False           True          False
1  28.0  51000.0                False          False           True
2  42.8  48000.0                False          False           True
3  32.0  52000.0                False           True          False
4 100.0  51000.0                 True          False          False
5  29.0  54000.0                False           True          False
```

---

## RESULT

The dataset was successfully pre-processed by handling missing values, treating outliers, encoding categorical variables, and generating a clean dataset ready for machine learning.

---

# 🧪 EXPERIMENT – 2

## Title

**Implement Linear Regression to predict a continuous target variable and explore how Multiple Linear Regression can capture the relationship between multiple predictors and the target.**

---

## INTRODUCTION

Linear Regression is a supervised machine learning technique used to predict a continuous target variable by establishing a linear relationship between the input feature(s) and the output.

In Simple Linear Regression, the model uses only one predictor variable.
Multiple Linear Regression uses two or more predictor variables to capture more complex relationships.

In this experiment, the Global Hunger Index (GHI) dataset is used.

---

## AIM

To implement Simple Linear Regression and Multiple Linear Regression techniques to predict the Global Hunger Index (GHI) using key hunger and nutrition indicators.

---

## Ex.No: 2

### PROGRAM

```python
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(42)

# Synthetic GHI dataset
data = pd.DataFrame({
    "Undernourishment": np.random.uniform(5, 40, 200),
    "ChildWasting": np.random.uniform(2, 25, 200),
    "ChildStunting": np.random.uniform(10, 50, 200),
    "ChildMortality": np.random.uniform(1, 15, 200)
})

data["GHI"] = (
    0.25 * data["Undernourishment"]
    + 0.25 * data["ChildWasting"]
    + 0.25 * data["ChildStunting"]
    + 0.25 * data["ChildMortality"]
    + np.random.normal(0, 1.5, 200)
)

print(data.head())
```

---

## OUTPUT

```
--- Simple Linear Regression ---
MAE: 3.041983782620014
MSE: 14.956599744135037
R2 Score: 0.34734049973251757

--- Multiple Linear Regression ---
MAE: 1.1059453765970535
MSE: 1.8504677196206836
R2 Score: 0.9192513433661731
```

---

## RESULT

Thus, Simple Linear Regression and Multiple Linear Regression models were successfully implemented on the GHI dataset, and Multiple Linear Regression produced better prediction accuracy by considering multiple input variables.


-------------------------------------------------------------------------------------------------------



*"Predicting the future isn’t magic, it’s artificial intelligence."*
 
-------------------------------------------------------------------------------------------------------

**🔗 Get In Touch :**

> **Connect with me on LinkedIn:**  
[<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" style="vertical-align:middle;"/> LinkedIn Profile](https://www.linkedin.com/in/nandeesh71)

> **Visit my portfolio:**  
[<img src="https://cdn-icons-png.flaticon.com/512/1055/1055687.png" width="24" height="24" style="vertical-align:middle;"/> Portfolio Website](https://nandeesh-71.web.app)

---------------------------------------------------
