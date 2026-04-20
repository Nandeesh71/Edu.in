# ============================================================
# EX.NO: 9 – XGBoost & LightGBM (Wharton Admit/Waitlist)
# ============================================================

"""
AIM
To implement XGBoost and LightGBM to classify Waitlist/Admit in
Wharton Class of 2025 statistics and plot confusion matrices.
"""

"""
PROCEDURE
1. Generate synthetic imbalanced dataset (500 samples, 10 features).
2. Split 70:30.
3. Train XGBClassifier and LGBMClassifier separately.
4. Evaluate Accuracy, Precision, Recall, F1.
5. Plot confusion matrix heatmap for each model.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import xgboost as xgb
import lightgbm as lgb

X, y = make_classification(n_samples=500, n_features=10, n_informative=5,
                            n_redundant=0, n_classes=2, weights=[0.8,0.2],
                            flip_y=0.05, random_state=42)
CLASS_LABELS = ["Waitlist (0)", "Admit (1)"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.30, random_state=42)

models = {
    "XGBoost":  xgb.XGBClassifier(use_label_encoder=False,
                                   eval_metric="logloss", random_state=42),
    "LightGBM": lgb.LGBMClassifier(random_state=42)
}

for name, mdl in models.items():
    mdl.fit(Xtr, ytr)
    yp = mdl.predict(Xte)
    print(f"\n--- {name} Results ---")
    print(classification_report(yte, yp, target_names=CLASS_LABELS))

    cm = confusion_matrix(yte, yp)
    df_cm = pd.DataFrame(cm, index=CLASS_LABELS, columns=CLASS_LABELS)
    sns.heatmap(df_cm, annot=True, fmt="d", cmap="Blues", linewidths=.5)
    plt.ylabel("True Label"); plt.xlabel("Predicted Label")
    plt.title(f"Confusion Matrix – {name}")
    plt.show()

"""
OUTPUT
--- XGBoost Results ---
              precision  recall  f1-score  support
Waitlist (0)       0.97    0.97      0.97      119
   Admit (1)       0.88    0.90      0.89       31
    accuracy                         0.95      150

--- LightGBM Results ---
              precision  recall  f1-score  support
Waitlist (0)       0.97    0.96      0.96      119
   Admit (1)       0.84    0.87      0.86       31
    accuracy                         0.94      150
"""

"""
RESULT
XGBoost and LightGBM were successfully implemented to classify
Waitlist and Admit, and confusion matrices were plotted.
"""