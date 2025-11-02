"""
Q1_LinearRegression_Scratch.py
Linear Regression (from scratch) on Diabetes dataset using single feature X[:,2] (BMI).
Simple gradient descent, plot, and print slope & intercept.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

# ------------------------------
# Step 1: Load dataset
# ------------------------------
data = load_diabetes()
X = data.data[:, 2].reshape(-1, 1)  # BMI feature
y = data.target.reshape(-1, 1)

# ------------------------------
# Step 2: Prepare data
# Standardize X for stable gradient descent
# ------------------------------
X_mean = X.mean()
X_std = X.std()
X_stdzd = (X - X_mean) / X_std

# Add a column of ones for intercept if you prefer closed-form; here we use separate intercept
# ------------------------------
# Step 3: Gradient Descent (simple)
# y_pred = m * X + c
# initialize parameters
m = 0.0
c = 0.0
lr = 0.01        # learning rate
epochs = 2000
n = len(X_stdzd)

for epoch in range(epochs):
    y_pred = m * X_stdzd + c
    error = y_pred - y
    dm = (2/n) * (error * X_stdzd).sum()
    dc = (2/n) * error.sum()
    m -= lr * dm
    c -= lr * dc

# Convert slope back to original scale: y = m*( (X - mean)/std ) + c
# Equivalent slope in original X units:
slope_original = m / X_std
intercept_original = c - (m * X_mean / X_std)

print(f"Slope (original units): {slope_original:.4f}")
print(f"Intercept (original units): {intercept_original:.4f}")

# ------------------------------
# Step 4: Plot results
# ------------------------------
plt.scatter(X, y, label='Data (BMI vs Progression)', alpha=0.6)
x_vals = np.linspace(X.min(), X.max(), 100).reshape(-1,1)
y_vals = slope_original * x_vals + intercept_original
plt.plot(x_vals, y_vals, color='red', label='Fitted line')
plt.xlabel('BMI (original scale)')
plt.ylabel('Disease Progression')
plt.title('Linear Regression (Scratch) - Diabetes (BMI)')
plt.legend()
plt.grid(True)
plt.show()
