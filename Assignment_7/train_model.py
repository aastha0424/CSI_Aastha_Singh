from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train the Random Forest model
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model to a pickle file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'model.pkl'")
