"""
Q2_LogisticRegression_Scratch.py
Logistic Regression (from scratch) on Breast Cancer dataset.
Sigmoid, gradient descent, print training accuracy.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

# ------------------------------
# Step 1: Load dataset
# ------------------------------
data = load_breast_cancer()
X = data.data  # shape (n_samples, n_features)
y = data.target.reshape(-1,1)  # 0 or 1

# ------------------------------
# Step 2: Prepare data
# Standardize features for gradient descent stability
# ------------------------------
X_mean = X.mean(axis=0)
X_std = X.std(axis=0) + 1e-8
X_stdzd = (X - X_mean) / X_std

# ------------------------------
# Step 3: Implement logistic regression with GD
# ------------------------------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

n_samples, n_features = X_stdzd.shape
W = np.zeros((n_features, 1))  # weights
b = 0.0                        # bias
lr = 0.1
epochs = 2000

for epoch in range(epochs):
    z = X_stdzd.dot(W) + b
    A = sigmoid(z)
    dz = A - y
    dW = (1/n_samples) * X_stdzd.T.dot(dz)
    db = dz.mean()
    W -= lr * dW
    b -= lr * db

# ------------------------------
# Step 4: Evaluate on training set
# ------------------------------
probs = sigmoid(X_stdzd.dot(W) + b)
preds = (probs >= 0.5).astype(int)
accuracy = (preds == y).mean()
print(f"Training Accuracy (scratch logistic): {accuracy*100:.2f}%")

# (Optional) show histogram of predicted probabilities
import matplotlib.pyplot as plt
plt.hist(probs, bins=30)
plt.title('Predicted probabilities (training set)')
plt.xlabel('Probability of class 1 (malignant)')
plt.ylabel('Count')
plt.grid(True)
plt.show()
