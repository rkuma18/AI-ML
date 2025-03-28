# BERT-Based Phishing Site Classifier 🛡️

This repository contains an implementation of a phishing site classifier using `bert-base-uncased` from the Hugging Face `transformers` library. The model is fine-tuned on the [Phishing Site Classification dataset](https://huggingface.co/datasets/shawhin/phishing-site-classification) to distinguish between phishing and non-phishing websites.

## 🚀 Features

- **Pre-trained BERT Model:** Utilized `bert-base-uncased` for text-based phishing detection.
- **Efficient Fine-Tuning:** Freezed base layers while allowing pooling layers to train.
- **Dataset Preprocessing:** Tokenized text data and applied padding for consistent input.
- **Evaluation Metrics:** Implemented Accuracy and AUC-ROC scoring.
- **Training Optimization:** Hyperparameter tuning with `Trainer` API.

## 📌 Setup

1. Clone the repository:
   ```bash
   git clone [Your Repo Link]
   cd bert-phishing-classifier
   ```
2. Install dependencies:
   ```bash
   pip install datasets transformers evaluate numpy torch
   ```


## 📊 Model Performance

After fine-tuning, the model achieves high accuracy and AUC scores, making it effective for phishing detection.

## 📂 File Structure

- `Fine-tuning_BERT.ipynb`: Fine-tuning script
- `README.md`: Documentation

## 🔗 References
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Dataset](https://huggingface.co/datasets/shawhin/phishing-site-classification)

Feel free to contribute or raise issues! 🚀

