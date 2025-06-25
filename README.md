# 🌊 RisingWaters - ML Flood Prediction

This is a SmartBridge Internship Project to predict the **possibility of severe floods** using **Machine Learning algorithms** and a clean **Flask web interface**.

---

## 📁 Folder Structure

> Please organize your project like this in GitHub. ✅ Clickable folders show where files go.

RisingWaters-MLFloodPrediction/
│
├── code/ # 🔧 All code files
│ ├── Floods.ipynb # Jupyter Notebook (EDA, modeling, saving model)
│ ├── app.py # Flask backend
│ ├── floods.save # Trained model file
│ ├── transform.save # Scaler file for input transformation
│
├── data/ # 📊 Dataset files
│ └── flood dataset.xlsx
│
├── report/ # 📄 Project Report
│ └── Flood_Prediction_Report.docx
│
├── screenshots/ # 🖼️ Screenshots of UI
│ ├── homepage.png
│ ├── prediction_form.png
│ └── prediction_result.png
│
├── static/ # 🎨 Static assets (CSS & images)
│ ├── css/
│ │ └── styles.css
│ └── images/
│ └── flood-bg1.jpg
│
├── templates/ # 🌐 HTML files
│ ├── home.html
│ ├── index.html
│ ├── chance.html
│ └── no_chance.html
│
└── README.md # 📘 This documentation file

---

## 📝 Project Overview

Floods pose serious risks to life and infrastructure. Our project uses historical climate and rainfall data to classify whether a **severe flood is likely** using ML models and a Flask-based prediction form.

---

## 💡 Input Features

- Cloud Cover (%)
- Annual Rainfall (mm)
- Jan–Feb Rainfall (mm)
- Mar–May Rainfall (mm)
- Jun–Sep Rainfall (mm)

---

## ⚙️ ML Models Compared

| Model           | Accuracy |
|----------------|----------|
| Decision Tree   | 96.55%   |
| Random Forest ✅| 96.55%   |
| KNN             | 89.65%   |
| XGBoost         | 96.55%   |

📌 **Selected Model:** Random Forest  
💾 Saved using `joblib` → [`code/floods.save`](./code/floods.save)

---

## 📈 Evaluation Metrics

All models were evaluated using:

- ✅ Accuracy
- ✅ Confusion Matrix
- ✅ Classification Report (Precision, Recall, F1-score)

---

## 🌐 Web Application

| Page              | File                   | Description |
|------------------|------------------------|-------------|
| Homepage         | `home.html`            | Project intro with background image
| Prediction Page  | `index.html`           | Input form for 5 climate features
| Result Page (Yes)| `chance.html`          | Displays "Possibility of Severe Flood"
| Result Page (No) | `no_chance.html`       | Displays "No Possibility of Severe Flood"

---

## 🧪 How to Run the App

### 1. Install required libraries:
```bash
pip install flask pandas numpy scikit-learn xgboost joblib openpyxl

---

## 📝 Project Overview

Floods pose serious risks to life and infrastructure. Our project uses historical climate and rainfall data to classify whether a **severe flood is likely** using ML models and a Flask-based prediction form.

---

## 💡 Input Features

- Cloud Cover (%)
- Annual Rainfall (mm)
- Jan–Feb Rainfall (mm)
- Mar–May Rainfall (mm)
- Jun–Sep Rainfall (mm)

---

## ⚙️ ML Models Compared

| Model           | Accuracy |
|----------------|----------|
| Decision Tree   | 96.55%   |
| Random Forest ✅| 96.55%   |
| KNN             | 89.65%   |
| XGBoost         | 96.55%   |

📌 **Selected Model:** Random Forest  
💾 Saved using `joblib` → [`code/floods.save`](./code/floods.save)

---

## 📈 Evaluation Metrics

All models were evaluated using:

- ✅ Accuracy
- ✅ Confusion Matrix
- ✅ Classification Report (Precision, Recall, F1-score)

---

## 🌐 Web Application

| Page              | File                   | Description |
|------------------|------------------------|-------------|
| Homepage         | `home.html`            | Project intro with background image
| Prediction Page  | `index.html`           | Input form for 5 climate features
| Result Page (Yes)| `chance.html`          | Displays "Possibility of Severe Flood"
| Result Page (No) | `no_chance.html`       | Displays "No Possibility of Severe Flood"

---

## 🧪 How to Run the App

### 1. Install required libraries:
```bash
pip install flask pandas numpy scikit-learn xgboost joblib openpyxl
cd code
python app.py
