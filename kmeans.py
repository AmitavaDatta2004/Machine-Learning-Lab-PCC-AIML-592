# K-Means Clustering from Scratch (No Modules)

# Sample dataset (you can replace this with your given data)
data = [[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]]

k = 2  # number of clusters
max_iters = 100

# Step 1: Initialize centroids (choose first k points)
centroids = []
for i in range(k):
    centroids.append(data[i])

for iteration in range(max_iters):
    print(f"\nIteration {iteration + 1}")
    # Step 2: Create empty clusters
    clusters = []
    for i in range(k):
        clusters.append([])

    # Step 3: Assign points to nearest centroid
    for point in data:
        # Calculate distance from each centroid
        distances = []
        for c in centroids:
            d = ((point[0] - c[0]) ** 2 + (point[1] - c[1]) ** 2) ** 0.5
            distances.append(d)
        # Find nearest centroid
        min_dist = distances[0]
        cluster_index = 0
        for i in range(1, len(distances)):
            if distances[i] < min_dist:
                min_dist = distances[i]
                cluster_index = i
        clusters[cluster_index].append(point)

    print("Clusters:", clusters)

    # Step 4: Recalculate new centroids
    new_centroids = []
    for cluster in clusters:
        if len(cluster) == 0:
            continue
        sum_x = sum_y = 0
        for point in cluster:
            sum_x += point[0]
            sum_y += point[1]
        new_centroids.append([sum_x / len(cluster), sum_y / len(cluster)])

    print("New centroids:", new_centroids)

    # Step 5: Check if centroids changed
    if new_centroids == centroids:
        print("Centroids stabilized. Stopping...")
        break
    else:
        centroids = new_centroids

print("\nFinal Clusters:", clusters)
print("Final Centroids:", centroids)
