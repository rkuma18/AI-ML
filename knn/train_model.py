from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from annoy import AnnoyIndex
import joblib

# Load data
data = load_iris()
X, y = data.data, data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Build Annoy index
index = AnnoyIndex(4, 'euclidean')  # 4 features, Euclidean distance
for i in range(len(X_train)):
    index.add_item(i, X_train[i])
index.build(10)  # 10 trees

# Save Annoy index and labels separately
index.save('iris_annoy.ann')  # Annoy's native save method
joblib.dump(y_train, 'y_train.pkl')  # Save labels with joblib