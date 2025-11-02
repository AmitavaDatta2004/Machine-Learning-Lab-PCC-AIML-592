"""
Q9_DecisionTree_RandomForest_Wine.py
Train DecisionTree and RandomForest on Wine dataset.
Show accuracies and plot the decision tree.
"""
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

data = load_wine()
X = data.data
y = data.target
feature_names = data.feature_names
class_names = data.target_names

dt = DecisionTreeClassifier(random_state=0)
rf = RandomForestClassifier(random_state=0)

dt.fit(X,y)
rf.fit(X,y)

print("Decision Tree accuracy (train):", dt.score(X,y))
print("Random Forest accuracy (train):", rf.score(X,y))

plt.figure(figsize=(12,8))
plot_tree(dt, feature_names=feature_names, class_names=class_names, filled=True, max_depth=3)
plt.title('Decision Tree (Wine) - first 3 levels')
plt.show()
