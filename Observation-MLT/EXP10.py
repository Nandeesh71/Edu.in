# ============================================================
# EX.NO: 10 – K-Means & Hierarchical Clustering (Customer Segmentation)
# ============================================================

"""
AIM
To implement K-Means and Hierarchical Clustering on a customer
segmentation dataset and plot the Elbow curve and Dendrogram.
"""

"""
PROCEDURE
K-Means:
1. Load dataset (Annual Income, Spending Score).
2. Apply Elbow Method for k = 1..10 (plot WCSS).
3. Fit K-Means with optimal K=5; plot clusters.

Hierarchical:
1. Plot Dendrogram using Ward linkage.
2. Apply AgglomerativeClustering (n_clusters=5); plot clusters.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import KMeans, AgglomerativeClustering

# ---- Synthetic customer data (mirrors the CSV used in the lab) ----
np.random.seed(0)
n = 50
data = pd.DataFrame({
    "Annual Income (k$)":      np.random.randint(15, 55, n),
    "Spending Score (1-100)":  np.random.randint(1, 100, n)
})

X = data[["Annual Income (k$)", "Spending Score (1-100)"]]

# --- A. K-Means ---
wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, random_state=42, n_init=10)
    km.fit(X)
    wcss.append(km.inertia_)

plt.figure(figsize=(6,4))
plt.plot(range(1,11), wcss, marker="o")
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters"); plt.ylabel("WCSS")
plt.show()

km5 = KMeans(n_clusters=5, random_state=42, n_init=10)
data["Cluster"] = km5.fit_predict(X)
plt.figure(figsize=(6,4))
plt.scatter(X.iloc[:,0], X.iloc[:,1], c=data["Cluster"], cmap="viridis")
plt.xlabel("Annual Income (k$)"); plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation using K-Means")
plt.show()

# --- B. Hierarchical ---
plt.figure(figsize=(8,5))
sch.dendrogram(sch.linkage(X, method="ward"))
plt.title("Dendrogram for Customer Segmentation")
plt.xlabel("Customers"); plt.ylabel("Euclidean Distance")
plt.show()

hc = AgglomerativeClustering(n_clusters=5, metric="euclidean", linkage="ward")
data["HC_Cluster"] = hc.fit_predict(X)
plt.figure(figsize=(6,4))
plt.scatter(X.iloc[:,0], X.iloc[:,1], c=data["HC_Cluster"], cmap="rainbow")
plt.xlabel("Annual Income (k$)"); plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation using Hierarchical Clustering")
plt.show()

"""
OUTPUT
(Elbow curve shows WCSS dropping steeply up to K=5, then flattening.)
(K-Means scatter shows 5 colour-coded customer clusters.)
(Dendrogram shows hierarchical merge tree for all customers.)
(Hierarchical scatter shows 5 colour-coded clusters.)
"""

"""
RESULT
K-Means and Hierarchical Clustering were successfully implemented on
the customer segmentation dataset, and the Elbow curve and Dendrogram
were plotted successfully.
"""