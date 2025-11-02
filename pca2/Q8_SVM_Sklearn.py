"""
Q8_SVM_Sklearn.py
Train linear SVM (SVC with kernel='linear') on Iris dataset using first two features.
Print accuracy and visualize decision boundaries.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.svm import SVC

data = load_iris()
X = data.data[:, :2]  # sepal length, sepal width
y = data.target

model = SVC(kernel='linear')
model.fit(X, y)
print("Training accuracy:", model.score(X,y))

# Decision boundary visualization
x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300), np.linspace(y_min, y_max, 300))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:,0], X[:,1], c=y, edgecolors='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('SVM (linear) Decision Boundary')
plt.show()
