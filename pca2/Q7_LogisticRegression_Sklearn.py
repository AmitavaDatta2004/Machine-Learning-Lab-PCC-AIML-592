"""
Q7_LogisticRegression_Sklearn.py
LogisticRegression from sklearn on Breast Cancer dataset.
Print accuracy, confusion matrix, and classification report.
"""
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

data = load_breast_cancer()
X = data.data
y = data.target

model = LogisticRegression(max_iter=5000)
model.fit(X, y)
y_pred = model.predict(X)

print("Accuracy:", model.score(X,y))
print("Confusion Matrix:")
print(confusion_matrix(y, y_pred))
print("Classification Report:")
print(classification_report(y, y_pred))
