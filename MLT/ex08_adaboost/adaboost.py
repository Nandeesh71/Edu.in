# ============================================================
# EX. NO.: 08 - AdaBoost Technique
# ============================================================
# AIM:
# Implement AdaBoost to classify loan approval / not approval
# and plot confusion matrix using credit_risk_dataset.
#
# ALGORITHM:
# 1. Load credit_risk_dataset.csv.
# 2. One-Hot Encode categorical columns.
# 3. Separate features (X) and target (loan_status).
# 4. Handle missing values using SimpleImputer (mean strategy).
# 5. Split 70% train, 30% test.
# 6. Train AdaBoostClassifier with 50 estimators.
# 7. Predict and evaluate accuracy.
# 8. Plot confusion matrix heatmap using seaborn.
# ============================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("credit_risk_dataset.csv")

# Encode Categorical Columns
data = pd.get_dummies(data, drop_first=True)

# Features and Target
X = data.drop('loan_status', axis=1)
y = data['loan_status']

# Handle Missing Values
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train AdaBoost
model = AdaBoostClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# Predict and Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='coolwarm')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - AdaBoost")
plt.show()

# ============================================================
# OUTPUT:
# Accuracy: 0.8721
# Confusion Matrix:
#   [[7157, 456],
#    [ 794, 1368]]
# Plot: Heatmap showing loan approval vs rejection predictions
#
# RESULT:
# AdaBoost classifier successfully classified loan approvals.
# Achieved 87.21% accuracy. Confusion matrix plotted using seaborn.
# ============================================================
