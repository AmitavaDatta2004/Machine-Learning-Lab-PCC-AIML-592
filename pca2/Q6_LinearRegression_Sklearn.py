"""
Q6_LinearRegression_Sklearn.py
LinearRegression from sklearn on Diabetes dataset using all features.
Print coefficients, intercept, and R^2 score.
"""
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import numpy as np

data = load_diabetes()
X = data.data
y = data.target

model = LinearRegression()
model.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("R^2 score:", model.score(X,y))
