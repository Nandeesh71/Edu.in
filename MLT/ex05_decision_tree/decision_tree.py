# ============================================================
# EX. NO.: 05 - Decision Tree Classifier
# ============================================================
# AIM:
# Implement Decision Tree to predict if a car needs service
# and plot confusion matrix using the Toyota dataset.
#
# ALGORITHM:
# 1. Load Toyota.csv dataset.
# 2. Clean data: replace invalid values, convert to numeric.
# 3. Fill missing values with median; forward-fill categorical.
# 4. Create target: service_required (1 if KM>50000 or Age>30).
# 5. One-Hot Encode FuelType column.
# 6. Split data 70% train, 30% test.
# 7. Train DecisionTreeClassifier (max_depth=5).
# 8. Evaluate with confusion matrix and classification report.
# ============================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Toyota.csv")

# Clean Data
df.replace("????", np.nan, inplace=True)
df['HP']    = pd.to_numeric(df['HP'],    errors='coerce')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Doors'] = df['Doors'].replace({'three': 3, 'four': 4, 'five': 5})
df['Doors'] = pd.to_numeric(df['Doors'], errors='coerce')

# Fill missing values
df.fillna(df.median(numeric_only=True), inplace=True)
df.ffill(inplace=True)

# Create Target Column
df['service_required'] = np.where((df['KM'] > 50000) | (df['Age'] > 30), 1, 0)

# Encode Categorical Columns
df = pd.get_dummies(df, columns=['FuelType'], drop_first=True)

# Features and Target
X = df.drop('service_required', axis=1)
y = df['service_required']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Decision Tree
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Visualize Tree
plt.figure(figsize=(20, 10))
plot_tree(model, filled=True, feature_names=X.columns,
          class_names=['No Service', 'Service'], fontsize=10)
plt.title("Decision Tree - Toyota Service Prediction")
plt.show()

# Predict and Evaluate
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Plot Confusion Matrix Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['No Service', 'Service'],
            yticklabels=['No Service', 'Service'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Decision Tree")
plt.show()

# ============================================================
# OUTPUT:
# Confusion Matrix: [[31, 0], [0, 392]]
# Classification Report: Precision=1.00, Recall=1.00, F1=1.00
# Accuracy: 1.00
# Plots: Decision tree structure + confusion matrix heatmap
#
# RESULT:
# Decision Tree classifier successfully identified whether cars
# need service. Model achieved 100% accuracy on test data.
# ============================================================
