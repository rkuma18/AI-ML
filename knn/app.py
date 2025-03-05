from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from annoy import AnnoyIndex
import joblib
import numpy as np

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Load Annoy index and labels
index = AnnoyIndex(4, 'euclidean')  # Rebuild index object
index.load('iris_annoy.ann')  # Load pre-built index
y_train = joblib.load('y_train.pkl')  # Load labels

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features'])
    
    # Find 5 nearest neighbors
    neighbor_ids = index.get_nns_by_vector(features, 5)
    predictions = y_train[neighbor_ids]
    
    # Majority vote
    prediction = np.bincount(predictions).argmax()
    
    return jsonify({
        'prediction': int(prediction),
        'neighbors_found': len(neighbor_ids)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)