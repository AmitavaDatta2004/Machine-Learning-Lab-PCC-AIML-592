"""
Q12_DecisionTree_RandomForest_BreastCancer.py
Train Decision Tree and Random Forest on Breast Cancer dataset (80-20 split).
Print accuracies, confusion matrices, and feature importances.
"""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
import matplotlib.pyplot as plt

data = load_breast_cancer()
X = data.data
y = data.target
feature_names = data.feature_names

# Split data 80-20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)

dt = DecisionTreeClassifier(random_state=0)
rf = RandomForestClassifier(n_estimators=100, random_state=0)

dt.fit(X_train, y_train)
rf.fit(X_train, y_train)

y_pred_dt = dt.predict(X_test)
y_pred_rf = rf.predict(X_test)

print("Decision Tree Accuracy (test):", accuracy_score(y_test, y_pred_dt))
print("Random Forest Accuracy (test):", accuracy_score(y_test, y_pred_rf))

print("\\nConfusion Matrix - Decision Tree")
print(confusion_matrix(y_test, y_pred_dt))
print("\\nConfusion Matrix - Random Forest")
print(confusion_matrix(y_test, y_pred_rf))

# Feature importances (show top 10)
importances_dt = dt.feature_importances_
importances_rf = rf.feature_importances_

idx_dt = importances_dt.argsort()[::-1][:10]
idx_rf = importances_rf.argsort()[::-1][:10]

print("\\nTop features (Decision Tree):")
for i in idx_dt:
    print(f"{feature_names[i]}: {importances_dt[i]:.4f}")

print("\\nTop features (Random Forest):")
for i in idx_rf:
    print(f"{feature_names[i]}: {importances_rf[i]:.4f}")

# Plot feature importances comparison (top 10)
indices = np.arange(10)
labels_dt = [feature_names[i] for i in idx_dt]
labels_rf = [feature_names[i] for i in idx_rf]

plt.figure(figsize=(10,5))
plt.barh(labels_dt[::-1], importances_dt[idx_dt][::-1], alpha=0.6, label='Decision Tree')
plt.barh(labels_rf[::-1], importances_rf[idx_rf][::-1], alpha=0.4, label='Random Forest')
plt.title('Top 10 Feature Importances (DT vs RF)')
plt.xlabel('Importance')
plt.legend()
plt.tight_layout()
plt.show()
