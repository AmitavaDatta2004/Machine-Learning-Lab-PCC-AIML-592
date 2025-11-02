"""
Q3_DecisionTree_Scratch.py
Simple Decision Tree (one-level / greedy split) using entropy (information gain)
on Iris dataset using two features: petal length and petal width.
This demonstrates how the first split is chosen.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# ------------------------------
# Step 1: Load dataset (two features)
# ------------------------------
data = load_iris()
X = data.data[:, 2:4]  # petal length, petal width
y = data.target

# ------------------------------
# Step 2: Define entropy and information gain
# ------------------------------
def entropy(labels):
    # labels: 1D array of class labels
    unique, counts = np.unique(labels, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs + 1e-9))

def information_gain(feature_values, labels, threshold):
    left_labels = labels[feature_values <= threshold]
    right_labels = labels[feature_values > threshold]
    if len(left_labels) == 0 or len(right_labels) == 0:
        return 0
    parent_entropy = entropy(labels)
    left_entropy = entropy(left_labels)
    right_entropy = entropy(right_labels)
    w_left = len(left_labels) / len(labels)
    w_right = len(right_labels) / len(labels)
    gain = parent_entropy - (w_left * left_entropy + w_right * right_entropy)
    return gain

# ------------------------------
# Step 3: Search best split (feature and threshold)
# ------------------------------
best_gain = 0
best_feat = None
best_thresh = None

for feat in range(X.shape[1]):
    values = np.unique(X[:, feat])
    for thresh in values:
        gain = information_gain(X[:, feat], y, thresh)
        if gain > best_gain:
            best_gain = gain
            best_feat = feat
            best_thresh = thresh

feature_names = ['petal length', 'petal width']
print(f"Best split: feature='{feature_names[best_feat]}', threshold={best_thresh:.3f}, information gain={best_gain:.4f}")

# ------------------------------
# Step 4: Visualize split
# ------------------------------
colors = ['red','green','blue']
for cls in np.unique(y):
    idx = y == cls
    plt.scatter(X[idx,0], X[idx,1], label=f'class {cls}', alpha=0.6)

if best_feat == 0:
    plt.axvline(x=best_thresh, color='k', linestyle='--', label='split')
else:
    plt.axhline(y=best_thresh, color='k', linestyle='--', label='split')

plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.title('Iris dataset — best first split (entropy)')
plt.legend()
plt.grid(True)
plt.show()
