# 🌍 Disaster Relief Resource Optimizer

> An AI-powered decision support system that predicts disaster relief priority using machine learning and provides an interactive geospatial dashboard for emergency response planning.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![XGBoost](https://img.shields.io/badge/XGBoost-Machine%20Learning-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)

---

# 📖 Overview

Natural disasters such as typhoons, floods, earthquakes, and landslides frequently affect communities in the Philippines. Emergency responders often need to determine which incidents require immediate attention and how available resources should be allocated efficiently.

The **Disaster Relief Resource Optimizer** is an AI-driven decision support system designed to assist disaster management agencies by automatically predicting the relief priority of reported incidents using historical disaster data and machine learning.

Instead of relying solely on manual assessment, the system analyzes disaster-related indicators and provides an objective prediction of the incident's priority level, enabling faster and more informed decision-making.

---

# 🎯 Problem Statement

Emergency response teams often face challenges such as:

- Delayed prioritization of disaster incidents
- Limited emergency resources
- Increasing number of simultaneous disasters
- Subjective assessment of incident severity
- Difficulty identifying which locations require immediate assistance

These challenges can delay disaster response and reduce the effectiveness of relief operations.

---

# 💡 Proposed Solution

This project utilizes a supervised machine learning model trained on historical disaster data to classify incidents into:

- 🟢 Low Priority
- 🟡 Medium Priority
- 🔴 High Priority

The prediction is based on several disaster-related indicators, allowing emergency personnel to quickly determine which incidents require immediate response.

The system also stores prediction results in a PostgreSQL database and visualizes disaster information through an interactive web dashboard.

---

# 🚀 Features

## 🤖 Machine Learning Prediction

- Relief Priority Prediction
- Prediction Probability (Confidence Score)
- Multi-class Classification
- XGBoost Model

---

## 📍 Incident Management

- Create Incident Reports
- Update Incident Status
- Store Predictions
- Historical Incident Records

---

## 📊 Analytics Dashboard

- Active Incidents Overview
- Disaster Distribution
- Relief Priority Distribution
- Prediction History
- Feature Importance Visualization
- Correlation Analysis

---

## 🗺 Interactive GIS Map

Visualize disaster incidents across the Philippines using an interactive map.

Features include:

- Incident markers
- Priority color coding
- Disaster clustering
- Geographic visualization
- Incident information popup

---

# 🧠 Machine Learning Pipeline

```
Historical Disaster Dataset
            │
            ▼
     Data Cleaning
            │
            ▼
 Feature Engineering
            │
            ▼
 Label Encoding
            │
            ▼
 Train/Test Split
            │
            ▼
     XGBoost Classifier
            │
            ▼
 Relief Priority Prediction
            │
            ▼
 Probability Estimation
            │
            ▼
 FastAPI REST API
```

---

# 📊 Features Used

The model predicts disaster relief priority using the following features:

| Feature       | Description                        |
| ------------- | ---------------------------------- |
| affected_rate | Percentage of affected population  |
| damage_rate   | Infrastructure damage ratio        |
| homeless_rate | Percentage of displaced population |
| casualty_rate | Injury/Fatality ratio              |
| duration      | Disaster duration                  |
| disaster_type | Disaster category                  |

---

# 🛠 Technology Stack

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Alembic
- Uvicorn

---

## Machine Learning

- XGBoost
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Frontend

- React
- Tailwind CSS
- Leaflet.js
- React Router
- Axios
- Recharts

---

## DevOps

- Docker
- Docker Compose
- Git
- GitHub

---

# 📈 Model Performance

The trained XGBoost classifier achieved excellent performance in classifying disaster relief priority.

Evaluation includes:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Feature Importance
- Correlation Analysis

---

# 📂 Project Structure

```text
disaster_relief/
│
├── app/
│   ├── api/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── routers/
│   ├── utils/
│   └── main.py
│
├── model_weights/
│
├── frontend/
│
├── notebooks/
│
├── reports/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🔌 REST API

## Prediction

```
POST /disaster_relief_optimizer/predict
```

Predicts the relief priority of a disaster incident.

---

## Update Incident Status

```
PUT /disaster_relief_optimizer/{incident_id}/status
```

Updates the current status of an incident.

---

## Sample Prediction Response

```json
{
  "status": "success",
  "status_code": 201,
  "message": "Incident predicted successfully.",
  "data": {
    "incident_id": 15,
    "prediction": {
      "relief_priority": "High",
      "probability": 0.99997
    }
  }
}
```

---

# 📷 Dashboard

The web dashboard provides:

- 📍 Interactive Philippine Disaster Map
- 📊 Disaster Analytics
- 📈 Priority Distribution
- 📋 Incident Management
- 🤖 AI Predictions
- 📉 Feature Importance
- 📌 Correlation Heatmap

---

# 🎯 Future Improvements

- Live Weather API Integration
- Satellite Data Integration
- Real-time Disaster Monitoring
- SMS Notification System
- Resource Optimization Engine
- Route Optimization
- Multi-user Authentication
- Mobile Application

---

# 👨‍💻 Author

**Alfred Quinto Yap**

Bachelor of Science in Computer Science

Interested in:

- Artificial Intelligence
- Machine Learning
- Data Science
- Computer Vision
- Full Stack Development

GitHub: https://github.com/apyotDev

LinkedIn: https://linkedin.com/in/alfred-yap

