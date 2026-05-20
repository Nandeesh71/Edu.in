# ============================================================
# EX. NO.: 09 - XGBoost and LightGBM Technique
# ============================================================
# AIM:
# Implement XGBoost and LightGBM to classify Waitlist vs Admit
# in MBA dataset and plot confusion matrices.
#
# ALGORITHM:
# 1. Load MBA.csv and clean column names.
# 2. Filter dataset for Admit and Waitlist classes only.
# 3. Convert target to binary: Waitlist=0, Admit=1.
# 4. Label Encode all categorical columns.
# 5. Split 80% train, 20% test.
# 6. Train XGBClassifier and LGBMClassifier.
# 7. Predict and evaluate both models.
# 8. Plot confusion matrix heatmaps for both models.
# ============================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# Load Dataset
df = pd.read_csv("MBA.csv")
df.columns = df.columns.str.strip()

# Find Admission Column
target_col = next((c for c in df.columns if c.lower() == 'admission'), None)
if target_col is None:
    raise ValueError("Admission column not found")

# Filter classes and encode target
df[target_col] = df[target_col].astype(str).str.strip().str.lower()
df = df[df[target_col].isin(['admit', 'waitlist'])]
df['Status'] = df[target_col].map({'waitlist': 0, 'admit': 1})
df = df.drop(target_col, axis=1)

# Encode Categorical Columns
for col in df.select_dtypes(include='object').columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# Features and Target
X = df.drop('Status', axis=1)
y = df['Status']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── XGBoost ──────────────────────────────────────────────────
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)

print("XGBoost Accuracy:", accuracy_score(y_test, y_pred_xgb))
print(classification_report(y_test, y_pred_xgb))

plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y_test, y_pred_xgb), annot=True, fmt='d',
            cmap='coolwarm', xticklabels=['Waitlist', 'Admit'],
            yticklabels=['Waitlist', 'Admit'])
plt.title("XGBoost Confusion Matrix")
plt.xlabel("Predicted"); plt.ylabel("Actual")
plt.show()

# ── LightGBM ─────────────────────────────────────────────────
lgb = LGBMClassifier()
lgb.fit(X_train, y_train)
y_pred_lgb = lgb.predict(X_test)

print("LightGBM Accuracy:", accuracy_score(y_test, y_pred_lgb))
print(classification_report(y_test, y_pred_lgb))

plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y_test, y_pred_lgb), annot=True, fmt='d',
            cmap='viridis', xticklabels=['Waitlist', 'Admit'],
            yticklabels=['Waitlist', 'Admit'])
plt.title("LightGBM Confusion Matrix")
plt.xlabel("Predicted"); plt.ylabel("Actual")
plt.show()

# ============================================================
# OUTPUT:
# XGBoost  Accuracy: 0.895
#   Confusion Matrix: [[6,16],[5,173]]
# LightGBM Accuracy: 0.895
#   Confusion Matrix: [[6,16],[5,173]]
# Plots: Heatmaps for both XGBoost and LightGBM
#
# RESULT:
# XGBoost and LightGBM classified MBA admissions with 89.5%
# accuracy. Confusion matrices plotted using seaborn.
# ============================================================
