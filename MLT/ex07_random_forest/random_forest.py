# ============================================================
# EX. NO.: 07 - Random Forest Algorithm
# ============================================================
# AIM:
# Implement Random Forest to classify users based on driving
# habits and plot confusion matrix using ev_charging_patterns.
#
# ALGORITHM:
# 1. Load ev_charging_patterns.csv dataset.
# 2. Set "User Type" as target column.
# 3. One-Hot Encode categorical feature columns.
# 4. Split 80% train, 20% test.
# 5. Train RandomForestClassifier with 100 trees.
# 6. Predict and calculate accuracy.
# 7. Plot confusion matrix heatmap using seaborn.
# ============================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("ev_charging_patterns.csv")

# Target and Features
target_column = "User Type"
X = df.drop(target_column, axis=1)
y = df[target_column]

# Encode Categorical Columns
X = pd.get_dummies(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=model.classes_,
            yticklabels=model.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Random Forest")
plt.show()

# ============================================================
# OUTPUT:
# Accuracy: 0.3674
# Confusion Matrix:
#   Casual Driver  → [12, 47, 16]
#   Commuter       → [17, 62, 18]
#   Long-Distance  → [21, 48, 23]
# Plot: Heatmap of 3x3 confusion matrix
#
# RESULT:
# Random Forest algorithm classified EV users based on driving
# habits. Confusion matrix plotted using seaborn successfully.
# ============================================================
