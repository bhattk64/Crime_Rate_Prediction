# 🔍 Crime Rate Prediction System

This project is a machine learning-based web application that predicts crime rates in 19 metropolitan Indian cities. It uses historical crime data (2014–2021) sourced from the **National Crime Records Bureau (NCRB)** and supports prediction for 10 major crime categories. The system integrates a chatbot, interactive UI, and emergency contact details to help users get insights and guidance.

## 📌 Features

- 📈 **Crime Rate Prediction** based on city, crime type, and year
- 🤖 **Chatbot Integration** using Chatbase for interactive Q&A
- 📊 **Model Comparison Graphs** (R² Score, MAE, RMSE)
- 🚨 **Emergency Contact Information** for each crime type
- 🌐 **Responsive UI** built with HTML/CSS + Flask backend

## 💡 Problem Statement

Law enforcement agencies face challenges in anticipating where and what types of crimes are likely to happen next. This system helps predict future crime trends to aid in better resource planning and crime prevention.

## 🧠 Machine Learning Models Used

| Model Name               | R² Score (%) | MAE  | RMSE   |
|--------------------------|--------------|------|--------|
| Support Vector Regressor | -17.80       | 10.32| 371.79 |
| K-Nearest Neighbors      | 52.20        | 6.84 | 150.54 |
| Decision Tree Regressor  | 88.90        | 2.88 | 34.96  |
| **Random Forest Regressor** | **93.20**  | **2.48** | **21.36** |
| MLP Regressor            | 2.48         | 12.42| 307.55 |

📌 *Random Forest was selected as the final model due to its superior performance.*

## 📂 Project Structure

```bash
Crime_Rate_Prediction/
│
├── Dataset/
│   ├── crp.xlsx
│   └── new_dataset.xlsx
│
├── Mappings/
│   ├── City_Mapping.txt
│   └── Type_Mapping.txt
│
├── Model/
│   └── model.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── styles.css
│   └── images/
│       └── favicon.png
│
├── app.py
├── requirements.txt
└── README.md

📌 Technologies Used
Python

Flask – Web Framework

scikit-learn – Machine Learning

Chatbase – Chatbot Platform

HTML/CSS/JS – Frontend

Matplotlib / pandas – Data Visualization


📈 Working Example
User selects city, crime type, and year.

The system:

Encodes inputs

Projects population for the year

Predicts crime rate using ML model

Outputs:

Crime Rate per 100,000

Expected number of cases

Risk Level: Very Low / Low / High / Very High

Chatbot and emergency contact section provide support info.

📍 Future Improvements
🔊 Voice-based chatbot queries

🌐 Multilingual support (Hindi, Bengali, Marathi, etc.)

🛰️ Integration with real-time police crime databases

🗺️ Heatmap visualization using Mapbox or Leaflet.js

⚙️ Admin dashboard for dataset/model management


👨‍💻 Project Team
Kul Chandra Bhatt 

Anup Ghimire 

Atul Khetan

Guided by: Dr. Niyati Aggrawal, Jaypee Institute of Information Technology


🚀 Getting Started
Prerequisites:pip install -r requirements.txt
Run the App:python app.py
Then open your browser at: http://127.0.0.1:5000
