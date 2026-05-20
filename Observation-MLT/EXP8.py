# ============================================================
# EX.NO: 8 – AdaBoost (Loan Approval Classification)
# ============================================================

"""
AIM
To implement AdaBoost to classify loan approval / not approval and
plot the confusion matrix using Seaborn.
"""

"""
PROCEDURE
1. Generate synthetic imbalanced classification dataset (500 samples).
2. Split 70:30.
3. Define DecisionTreeClassifier (max_depth=1) as base estimator.
4. Train AdaBoostClassifier (50 estimators).
5. Evaluate metrics; plot confusion matrix heatmap.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=500, n_features=10, n_informative=5,
                            n_redundant=0, n_classes=2, weights=[0.8,0.2],
                            flip_y=0.05, random_state=42)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.30, random_state=42)

base = DecisionTreeClassifier(max_depth=1, random_state=42)
ada  = AdaBoostClassifier(estimator=base, n_estimators=50,
                           learning_rate=1.0, random_state=42)
ada.fit(Xtr, ytr)
yp = ada.predict(Xte)

print("=== AdaBoost Performance ===")
print(classification_report(yte, yp, target_names=["Not Approved","Approved"]))

cm = confusion_matrix(yte, yp)
df_cm = pd.DataFrame(cm, index=["Not Approved","Approved"],
                         columns=["Not Approved","Approved"])
sns.heatmap(df_cm, annot=True, fmt="d", cmap="Blues")
plt.ylabel("True Label"); plt.xlabel("Predicted Label")
plt.title("AdaBoost Classifier Confusion Matrix")
plt.show()

"""
OUTPUT
=== AdaBoost Performance ===
                   precision  recall  f1-score  support
Not Approved (0)       0.95    0.97      0.96      119
    Approved (1)       0.89    0.81      0.85       31
        accuracy                         0.94      150
"""

"""
RESULT
AdaBoost was successfully implemented to classify loan approval and
not approval, and the confusion matrix was plotted using Seaborn.
"""