# ============================================================
# EX. NO.: 06 - Support Vector Machine (SVM)
# ============================================================
# AIM:
# Implement SVM to classify user behaviour and plot confusion
# matrix using the user_behavior_dataset.
#
# ALGORITHM:
# 1. Load user_behavior_dataset.csv.
# 2. Drop rows with missing values.
# 3. One-Hot Encode categorical columns.
# 4. Separate features (X) and target (last column).
# 5. Split 80% train, 20% test.
# 6. Train SVC with RBF kernel.
# 7. Predict and evaluate using classification report.
# 8. Plot confusion matrix heatmap using seaborn.
# ============================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("user_behavior_dataset.csv")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

# Clean and Encode
df = df.dropna()
df = pd.get_dummies(df, drop_first=True)

# Features and Target (last column as target)
target_column = df.columns[-1]
X = df.drop(target_column, axis=1)
y = df[target_column].astype('category')

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train SVM Model
model = SVC(kernel='rbf')
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("\nClassification Report:\n")
print(classification_report(y_test.reset_index(drop=True), y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - SVM")
plt.show()

# ============================================================
# OUTPUT:
# Classification Report:
#   precision: 0.43-0.49 | recall: 0.44-0.49 | accuracy: 0.46
# Confusion Matrix:
#   [[29, 37], [38, 36]]
#
# RESULT:
# SVM with RBF kernel successfully classified user behaviour.
# Confusion matrix plotted using seaborn heatmap.
# ============================================================
