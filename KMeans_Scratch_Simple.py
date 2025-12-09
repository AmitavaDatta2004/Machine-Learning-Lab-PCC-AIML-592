# ------------------------------------------------------------
# K-Means Clustering (Simple + Random Initialization)
# ------------------------------------------------------------

import random  # only for random centroid initialization

# Step 1: Create simple 2D data points
X = [[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]]

k = 2  # number of clusters

# Step 2: Initialize centroids randomly from data points
centroids = random.sample(X, k)
print("Initial centroids:", centroids)

# Step 3: Repeat few times (say 5 iterations)
for _ in range(5):
    # Create empty clusters
    clusters = [[] for i in range(k)]

    # Step 4: Assign each point to the nearest centroid
    for point in X:
        distances = []
        for c in centroids:
            d = ((point[0] - c[0]) ** 2 + (point[1] - c[1]) ** 2) ** 0.5
            distances.append(d)
        nearest = distances.index(min(distances))
        clusters[nearest].append(point)

    # Step 5: Update centroids (average of cluster points)
    new_centroids = []
    for cluster in clusters:
        if len(cluster) > 0:
            x_sum = sum([p[0] for p in cluster])
            y_sum = sum([p[1] for p in cluster])
            new_centroids.append([x_sum / len(cluster), y_sum / len(cluster)])
        else:
            new_centroids.append(random.choice(X))  # if empty, reassign randomly

    centroids = new_centroids
    print("\nIteration:", _ + 1)
    print("Clusters:", clusters)
    print("Updated centroids:", centroids)

print("\nFinal centroids:", centroids)
