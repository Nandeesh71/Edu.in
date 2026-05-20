# ============================================================
# EX.NO: 5 – Decision Tree Classifier (Car Service)
# ============================================================

"""
AIM
To implement a Decision Tree classifier to identify whether cars
require service or not and plot the confusion matrix using Seaborn.
"""

"""
PROCEDURE
1. Create dataset with Mileage, Engine_Temperature, Oil_Quality,
   Brake_Condition and Service_Required.
2. Split 70:30; train DecisionTreeClassifier (criterion='gini').
3. Predict and evaluate; plot confusion matrix heatmap.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    "Mileage":            [12000,25000,30000,15000,50000,60000,18000,22000,40000,55000],
    "Engine_Temperature": [70,85,90,75,95,100,80,88,92,98],
    "Oil_Quality":        [3,2,2,3,1,1,3,2,1,1],
    "Brake_Condition":    [3,2,2,3,1,1,3,2,1,1],
    "Service_Required":   [0,1,1,0,1,1,0,1,1,1]
}
df = pd.DataFrame(data)
X, y = df.drop("Service_Required", axis=1), df["Service_Required"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

dt = DecisionTreeClassifier(criterion="gini").fit(Xtr, ytr)
yp = dt.predict(Xte)
print("Decision Tree Accuracy:", accuracy_score(yte, yp))
print("\nClassification Report:\n", classification_report(yte, yp))

cm = confusion_matrix(yte, yp)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["No Service","Service Required"],
            yticklabels=["No Service","Service Required"])
plt.xlabel("Predicted"); plt.ylabel("True")
plt.title("Confusion Matrix - Decision Tree (Car Service)")
plt.show()

"""
OUTPUT
Decision Tree Accuracy: 1.0
Classification Report:
              precision  recall  f1-score  support
           1       1.00    1.00      1.00        3
    accuracy                         1.00        3
"""

"""
RESULT
Decision Tree classifier was successfully implemented to identify
cars requiring service or not.
"""