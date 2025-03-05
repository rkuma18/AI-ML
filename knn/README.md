# K-Nearest Neighbors (K-NN) API | Scalable ML Deployment with Docker & ONNX

**An end-to-end machine learning pipeline** for training, optimizing, and deploying a K-NN model with Docker. Built for scalability (Annoy), observability (Prometheus/Grafana), and edge compatibility (ONNX). Ideal for classification/regression tasks on large datasets.

---

## 🌟 Key Features
- **Production-Ready API**: Flask-based REST API with Prometheus metrics.
- **Billion-Scale Optimization**: Uses Annoy for approximate nearest neighbor search.
- **Edge Deployment**: Export models to ONNX for IoT/mobile devices.
- **Monitoring Stack**: Integrated Prometheus + Grafana dashboards.
- **Dockerized Workflow**: Reproducible from training to inference.

---

## 📂 Repository Structure
```bash
.
├── docker-compose.yml
├── Dockerfile
├── prometheus.yml
├── requirements.txt
├── train_model.py
├── app.py
├── onnx_export.py
└── models/
    ├── iris_annoy_model.pkl
    └── iris_knn.onnx

```
## 🚀 Quick Start

Prerequisites
- **Python 3.9+**
- **Docker** & **Docker Compose**
- (Optional) **AWS CLI** for ECR deployment

## Steps

1. Clone the Repository:

```bash
git clone https://github.com/<your-username>/knn-api.git
cd knn-api
```

2. Build and Run with Docker:

```bash
# Build the Docker image
docker build -t iris-knn-api .

# Start the API (port 5001)
docker run -p 5001:5001 iris-knn-api
```

3. Test the API:

```bash
curl -X POST http://localhost:5001/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```
Sample Response:

```bash
{
  "prediction": 0,
  "class_name": "Setosa",
  "neighbors_found": 5
}
```
## 🛠️ Advanced Usage

1. Monitoring Stack (Prometheus + Grafana)

   ```bash
   # Start the full stack (API + monitoring)
    docker-compose up --build
    ```
    Prometheus Dashboard: http://localhost:9090
    Grafana: http://localhost:3000 (Default: admin/admin)
    Import the dashboard template from grafana-dashboard.json (optional).

2. Export to ONNX for Edge Devices

   ```bash
   # Generate ONNX model (for IoT/mobile)
    python onnx_export.py
   ```
 - Output: models/iris_knn.onnx

3. Scale for Large Datasets

   Modify train_model.py to use Annoy with your data:
   ```bash
    index = AnnoyIndex(num_features, 'euclidean')  # For 100M+ data points
    index.build(n_trees=20)  # More trees → higher accuracy
   ```

## ☁️ Deployment Guide

# Option A: Docker Hub

```bash
# Tag and push
docker tag iris-knn-api <your-dockerhub-username>/iris-knn-api:1.0
docker push <your-dockerhub-username>/iris-knn-api:1.0

# Pull and run anywhere
docker run -p 5001:5001 <your-dockerhub-username>/iris-knn-api:1.0
```

# Option B: AWS ECR
```bash
# Authenticate Docker to ECR
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com

# Push image
docker tag iris-knn-api:latest <account-id>.dkr.ecr.<region>.amazonaws.com/iris-knn-api:1.0
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/iris-knn-api:1.0
```
## 🐛 Troubleshooting

- **Port Conflicts**: Use docker ps and docker stop <container-id> to resolve "port already in use" errors.

- **Missing Dependencies**: Rebuild Docker with --no-cache if packages are missing:

```bash
docker build --no-cache -t iris-knn-api .
```
- **Model Not Found**: Verify models/ directory exists and contains iris_annoy.ann and y_train.pkl.

## 🤝 Contributing
1. Fork the repository.

2. Create a branch: git checkout -b feature/your-feature

3. Commit changes: git commit -m "Add your feature"

4. Push: git push origin feature/your-feature

5. Open a Pull Request.

