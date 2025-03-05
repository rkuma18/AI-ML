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
├── docker-compose.yml        # Orchestrates API + monitoring stack
├── Dockerfile                # Builds the API container
├── prometheus.yml            # Configures Prometheus scraping
├── requirements.txt          # Python dependencies
├── train_model.py            # Trains model and builds Annoy index
├── app.py                    # Flask API with prediction endpoint
├── onnx_export.py            # Converts scikit-learn model to ONNX
└── models/                   # Generated artifacts
    ├── iris_annoy.ann        # Annoy index (optimized for speed)
    ├── y_train.pkl           # Training labels
    └── iris_knn.onnx         # ONNX model for edge devices
```bash

## 📂 Repository Structure

Prerequisites
Python 3.9+


