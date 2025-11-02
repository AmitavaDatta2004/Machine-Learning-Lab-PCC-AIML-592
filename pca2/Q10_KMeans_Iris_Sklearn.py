"""
Q10_KMeans_Iris_Sklearn.py
Apply KMeans (n_clusters=3) on Iris dataset using all features.
Print centers, inertia, and compare clusters with true species (ARI).
"""
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
import numpy as np

data = load_iris()
X = data.data
y = data.target

kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

print("Cluster centers:\n", kmeans.cluster_centers_)
print("Inertia:", kmeans.inertia_)
print("Adjusted Rand Index:", adjusted_rand_score(y, kmeans.labels_))

# plot first two features colored by cluster
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='viridis', alpha=0.6)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker='x', color='red', s=100)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('KMeans (sklearn) on Iris (clusters)')
plt.grid(True)
plt.show()
