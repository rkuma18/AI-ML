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

a
