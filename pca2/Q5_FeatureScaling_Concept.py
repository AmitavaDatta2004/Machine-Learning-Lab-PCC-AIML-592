"""
Q5_FeatureScaling_Concept.py
Short demonstration of why feature scaling is important.
Uses the Wine dataset to show KMeans clustering results before and after scaling.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load wine dataset and pick two features with different scales
data = load_wine()
X = data.data
# Choose feature 0 (alcohol, small range) and feature 10 (proline, large range)
X_sel = X[:, [0, 10]]

# Without scaling
kmeans1 = KMeans(n_clusters=3, random_state=0).fit(X_sel)
labels1 = kmeans1.labels_

# With scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_sel)
kmeans2 = KMeans(n_clusters=3, random_state=0).fit(X_scaled)
labels2 = kmeans2.labels_

print("Inertia without scaling:", kmeans1.inertia_)
print("Inertia with scaling:", kmeans2.inertia_)

# Plot side-by-side to visualize effect
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.scatter(X_sel[:,0], X_sel[:,1], c=labels1, cmap='viridis', alpha=0.6)
plt.title('KMeans without scaling')
plt.xlabel('Alcohol')
plt.ylabel('Proline')

plt.subplot(1,2,2)
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=labels2, cmap='viridis', alpha=0.6)
plt.title('KMeans with StandardScaler')
plt.xlabel('Alcohol (scaled)')
plt.ylabel('Proline (scaled)')
plt.tight_layout()
plt.show()
