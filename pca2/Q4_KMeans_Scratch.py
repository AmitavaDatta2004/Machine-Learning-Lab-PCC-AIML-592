"""
Q4_KMeans_Scratch.py
K-Means clustering implemented from scratch on Iris dataset using two features:
sepal length and sepal width. Plots clusters and centroids.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

np.random.seed(0)

# ------------------------------
# Load data (two features)
# ------------------------------
data = load_iris()
X = data.data[:, :2]  # sepal length, sepal width

# ------------------------------
# K-means parameters
# ------------------------------
k = 3
max_iters = 100

# ------------------------------
# Initialize centroids randomly from data points
# ------------------------------
indices = np.random.choice(len(X), k, replace=False)
centroids = X[indices].astype(float)

for itr in range(max_iters):
    # assign clusters
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)  # shape (n_samples, k)
    clusters = np.argmin(distances, axis=1)
    # update centroids
    new_centroids = np.array([X[clusters==i].mean(axis=0) if np.any(clusters==i) else centroids[i] for i in range(k)])
    if np.allclose(centroids, new_centroids):
        break
    centroids = new_centroids

print("Final centroids:\n", centroids)

# ------------------------------
# Plot clusters and centroids
# ------------------------------
for i in range(k):
    pts = X[clusters==i]
    plt.scatter(pts[:,0], pts[:,1], label=f'cluster {i}', alpha=0.6)
plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=150, color='k', label='centroids')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('K-Means (scratch) on Iris')
plt.legend()
plt.grid(True)
plt.show()
