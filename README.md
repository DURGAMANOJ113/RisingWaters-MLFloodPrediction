# 🌊 RisingWaters-MLFloodPrediction

---

## 📝 Project Description

Floods pose a significant threat to lives, infrastructure, and the environment. This project applies machine learning techniques to historical weather data in order to predict the **likelihood of a severe flood** based on rainfall patterns and cloud cover. The trained model is deployed using a **Flask web application**, allowing users to enter meteorological values and instantly receive a prediction.

---

## 📊 Dataset Overview

- **File:** `flood dataset.xlsx`
- **Total Records:** 115
- **Target Variable:** `flood`  
  *(0: No Flood, 1: Flood)*

### ✅ Final Input Features:
- Cloud Cover
- ANNUAL (Annual Rainfall)
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall

---

## 🧪 Machine Learning Models

| Model           | Accuracy |
|----------------|----------|
| Decision Tree  | 100%     |
| Random Forest  | 100%     |
| XGBoost        | 100%     |
| KNN            | 95.6%    |

All models were evaluated using:
- ✅ Accuracy
- ✅ Confusion Matrix
- ✅ Classification Report *(Precision, Recall, F1-score)*

### ⚠️ Overfitting Observation

The Decision Tree, Random Forest, and XGBoost models achieved **100% accuracy** on the test set. While this appears perfect, it often indicates **overfitting**, especially when:
- The dataset is small (115 samples)
- The test set is not diverse enough
- Models are over-tuned to training data

> 🔍 These models might **not generalize well** to unseen or real-world data.

#### 🔧 Future Fixes:
- Implement cross-validation
- Use techniques like pruning or regularization
- Expand the dataset with samples from different years or regions

---

## 📈 Visualizations

The project includes the following visual analysis:

- 📊 Distribution plots and boxplots for each input feature  
- 🔥 Correlation heatmap  
- 📉 Confusion matrix heatmaps for each model  
- 📊 Bar chart comparing model accuracies  

📁 All visualizations are available in the [`screenshots/`](screenshots/) folder.

---

## 🌐 Web Application (Flask)

A user-friendly web application built using **Flask + HTML + Bootstrap**.

### 🔹 Input Form Fields:
- Cloud Cover
- ANNUAL
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall

### 🔸 Web Pages:
- `home.html`: Project intro and overview  
- `index.html`: User input form  
- `chance.html`: Prediction = Possibility of Flood  
- `no_chance.html`: Prediction = No Possibility of Flood

---

## 💾 Model & Scaler

- `floods.save`: Trained Random Forest model  
- `transform.save`: StandardScaler object for consistent input scaling

Both are used by the Flask backend to perform real-time predictions.

---

## 📦 Project Structure

RisingWaters-MLFloodPrediction/
├── code/ # Jupyter notebook & app.py
├── data/ # Excel dataset
├── screenshots/ # Visual output & web app screenshots
├── report/ # Project report (docx)
├── Flask/ # Flask app folder with templates/static/model
└── README.md # This documentation file


---

## 🎥 Demo Video

📽️ [Click here to watch the project demo](https://your-demo-video-link-here)

> Replace this link with your actual video (Google Drive or YouTube)

---

## 🔗 GitHub Repository Link

This is the repository you're currently viewing:  
🔗 **[https://github.com/DURGAMANOJ113/RisingWaters-MLFloodPrediction](https://github.com/DURGAMANOJ113/RisingWaters-MLFloodPrediction)**

---

## ✅ Project Checklist

- [x] Dataset loaded and cleaned  
- [x] EDA performed and visualized  
- [x] Models trained and evaluated  
- [x] Best model saved (`floods.save`)  
- [x] Flask app developed and tested  
- [x] README and documentation added  
- [x] GitHub repository structured  
- [x] Screenshots uploaded  
- [x] Demo video recorded

---

## 🚀 Future Enhancements

- 🌍 Train with data from multiple regions  
- 📈 Add flood severity prediction (e.g., mild, moderate, severe)  
- 🤖 Integrate rainfall forecasting using LSTM or Prophet  
- ☁️ Deploy the Flask app to Render, Vercel, or AWS  
- 📡 Connect real-time weather APIs for live predictions

---

> Made with ❤️ by **DURGAMANOJ113**  
> SmartBridge Internship – Flood Prediction ML Project
