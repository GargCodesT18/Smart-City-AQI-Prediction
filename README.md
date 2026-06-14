# 🌍 Smart City AQI Monitor

An AI-powered Air Quality Index (AQI) prediction and Early Warning System built using **Machine Learning** and **Streamlit**. The application predicts AQI values from environmental sensor readings and provides pollution risk alerts to support smart city environmental monitoring.

---

## ✨ Features

- 🌫️ AQI Prediction using Random Forest
- 🤖 Early Air Pollution Risk Detection
- 📊 Interactive Streamlit Dashboard
- 📈 Pollution Risk Probability Analysis
- 🎨 Color-coded AQI Categories
- ⚡ Fast and Lightweight Predictions

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Random Forest**
- **Pickle**

---

## 📂 Project Structure

```
Smart-City-AQI-Monitor/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   └── aqimain.ipynb
│
└── data/
    └── comprehensive_indian_air_quality_dataset.csv
```

---

## 📊 Input Features

- PM2.5
- PM10
- NO₂
- SO₂
- CO
- O₃
- Temperature
- Humidity
- City Type

---

## 🤖 Models Used

| Model | Purpose |
|--------------------------|------------------------------|
| Random Forest Regressor | AQI Prediction |
| Random Forest Classifier | Early Pollution Risk Detection |

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/GargCodesT18/Smart-City-AQI-Monitor.git
cd Smart-City-AQI-Monitor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔄 Workflow

```
Environmental Data
        │
        ▼
 Data Preprocessing
        │
        ├────────────► Early Warning Model
        │                     │
        │                     ▼
        │             Pollution Risk
        │
        ▼
 AQI Prediction Model
        │
        ▼
 Predicted AQI + Category
```

---

## 📌 Future Improvements

- Real-time AQI API Integration
- IoT Sensor Connectivity
- Time-Series AQI Forecasting
- Interactive Pollution Maps
- Cloud Deployment

---

## 👨‍💻 Author

**Tikshan Garg**

Engineering Student | AI & Machine Learning Enthusiast

---

⭐ If you found this project useful, consider giving it a star!
