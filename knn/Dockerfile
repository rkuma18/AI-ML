FROM python:3.9-slim

WORKDIR /app

# Install system deps + create models directory
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && mkdir -p /app/models \
    && chmod a+w /app/models \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Train model during build
RUN python train_model.py

CMD ["python", "app.py"]