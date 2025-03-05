# onnx_export.py
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import joblib

# Train a lightweight scikit-learn model for edge devices
data = load_iris()
model = KNeighborsClassifier(n_neighbors=3).fit(data.data, data.target)

# Export to ONNX
initial_type = [('float_input', FloatTensorType([None, 4]))]
onnx_model = convert_sklearn(model, initial_types=initial_type)

with open("iris_knn.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())