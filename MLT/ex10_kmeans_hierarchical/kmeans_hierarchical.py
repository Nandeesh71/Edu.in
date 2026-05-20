# ============================================================
# EX. NO.: 10 - K-Means and Hierarchical Clustering
# ============================================================
# AIM:
# Implement K-Means and Hierarchical Clustering on customer
# segmentation dataset and plot elbow curve and dendrogram.
#
# ALGORITHM:
# 1. Load credit_risk_dataset.csv.
# 2. Drop missing values; Label Encode categorical columns.
# 3. Scale features using StandardScaler.
# 4. Apply Elbow Method to find optimal K for K-Means.
# 5. Train K-Means with best K; map clusters to true labels.
# 6. Plot dendrogram using Ward linkage (first 100 samples).
# 7. Apply Hierarchical clustering and evaluate accuracy.
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, accuracy_score
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Load Dataset
df = pd.read_csv("credit_risk_dataset.csv")
df = df.dropna()

# Encode Categorical Columns
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

# Features and Target
X = df.drop(columns=['loan_status'])
y = df['loan_status']

# Scale Features
scaler   = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ── Elbow Method ─────────────────────────────────────────────
wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, random_state=42)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

plt.figure()
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method (K-Means)")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# ── K-Means Clustering ────────────────────────────────────────
kmeans           = KMeans(n_clusters=3, random_state=42)
clusters_kmeans  = kmeans.fit_predict(X_scaled)

# Map each cluster to the most frequent true label
mapping = {i: y[clusters_kmeans == i].mode()[0]
           for i in np.unique(clusters_kmeans)}
y_pred_kmeans = [mapping[c] for c in clusters_kmeans]

print("\n===== K-MEANS RESULTS =====")
print("Accuracy:", accuracy_score(y, y_pred_kmeans))
print(classification_report(y, y_pred_kmeans))

# ── Hierarchical Clustering ───────────────────────────────────
linked = linkage(X_scaled[:100], method='ward')

plt.figure(figsize=(12, 6))
dendrogram(linked)
plt.title("Dendrogram (Hierarchical Clustering)")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()

# Apply Hierarchical clusters and evaluate
clusters_hier = fcluster(linked, t=3, criterion='maxclust')
y_subset      = y.iloc[:100]

mapping_hier  = {i: y_subset[clusters_hier == i].mode()[0]
                 for i in np.unique(clusters_hier)}
y_pred_hier   = [mapping_hier[c] for c in clusters_hier]

print("\n===== HIERARCHICAL RESULTS =====")
print("Accuracy:", accuracy_score(y_subset, y_pred_hier))
print(classification_report(y_subset, y_pred_hier))

# ============================================================
# OUTPUT:
# K-Means  Accuracy: 0.7834
#   precision 0→0.78, recall 0→1.00 | precision 1→0.00
# Hierarchical Accuracy: 0.59
#   precision 0→1.00, recall 0→0.02 | precision 1→0.59
# Plots: Elbow curve (WCSS vs K) + Dendrogram
#
# RESULT:
# K-Means and Hierarchical Clustering implemented on credit
# risk dataset. Elbow curve and dendrogram plotted successfully.
# ============================================================
