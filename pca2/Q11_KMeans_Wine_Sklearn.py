"""
Q11_KMeans_Wine_Sklearn.py
KMeans on Wine dataset after StandardScaler. Print centers, inertia, and ARI.
"""
from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt

data = load_wine()
X = data.data
y = data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_scaled)

print("Cluster centers (scaled space):\n", kmeans.cluster_centers_)
print("Inertia:", kmeans.inertia_)
print("Adjusted Rand Index:", adjusted_rand_score(y, kmeans.labels_))

# Optional 2D projection for visualization: use first two PCA-like axes (just first two features here)
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=kmeans.labels_, cmap='viridis', alpha=0.6)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker='x', color='red', s=100)
plt.xlabel('Feature 1 (scaled)')
plt.ylabel('Feature 2 (scaled)')
plt.title('KMeans on Wine (scaled features)')
plt.grid(True)
plt.show()
