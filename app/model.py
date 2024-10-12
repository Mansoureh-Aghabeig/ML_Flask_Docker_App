import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a simple model
clf = RandomForestClassifier()
clf.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as model_file:
    pickle.dump(clf, model_file)
