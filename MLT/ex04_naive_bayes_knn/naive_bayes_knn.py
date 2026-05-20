# ============================================================
# EX. NO.: 04 - Naive Bayes and K-Nearest Neighbors (KNN)
# ============================================================
# AIM:
# Apply Naive Bayes and KNN to classify experience level
# (Low / Medium / High) using the GHI dataset.
#
# ALGORITHM:
# 1. Load GHI_Report.csv dataset.
# 2. Convert H_Score into categories: Low, Medium, High.
# 3. Features: Economy, Fam, Health, Freedom. Target: Experience.
# 4. Split data 70% train, 30% test.
# 5. Train GaussianNB and KNeighborsClassifier (k=3).
# 6. Evaluate accuracy and plot confusion matrices.
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# Load Dataset
data = pd.read_csv("GHI_Report.csv")

# Create Experience Level from H_Score
def level(score):
    if score <= 5.5:
        return "Low"
    elif score <= 6.5:
        return "Medium"
    else:
        return "High"

data["Experience"] = data["H_Score"].apply(level)

# Plot Experience Distribution
data["Experience"].value_counts().plot(kind="bar")
plt.title("Experience Level Distribution")
plt.xlabel("Experience Level")
plt.ylabel("Count")
plt.show()

# Features and Target
X = data[['Economy', 'Fam', 'Health', 'Freedom']]
y = data['Experience']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Naive Bayes
nb = GaussianNB()
nb.fit(X_train, y_train)
nb_pred = nb.predict(X_test)

# KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

# Accuracy
nb_acc  = accuracy_score(y_test, nb_pred)
knn_acc = accuracy_score(y_test, knn_pred)
print("Naive Bayes Accuracy:", nb_acc)
print("KNN Accuracy        :", knn_acc)

# Accuracy Comparison Bar Chart
plt.bar(["Naive Bayes", "KNN"], [nb_acc, knn_acc])
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()

# Confusion Matrix - Naive Bayes
ConfusionMatrixDisplay(confusion_matrix(y_test, nb_pred)).plot()
plt.title("Naive Bayes Confusion Matrix")
plt.show()

# Confusion Matrix - KNN
ConfusionMatrixDisplay(confusion_matrix(y_test, knn_pred)).plot()
plt.title("KNN Confusion Matrix")
plt.show()

# ============================================================
# OUTPUT:
# Naive Bayes Accuracy: 0.8125
# KNN Accuracy        : 0.75
# Plots: Experience distribution bar, accuracy comparison bar,
#        confusion matrices for both models
#
# RESULT:
# Naive Bayes and KNN algorithms were applied on GHI dataset.
# Naive Bayes achieved higher accuracy (81.25%) vs KNN (75%).
# ============================================================
