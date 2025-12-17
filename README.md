# 🛡️ Insurance Premium Prediction System
---

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success)](https://github.com/PatelG108/Insurance-premium)

---
## 🌐 Live Demo

[![Live on Render](https://img.shields.io/badge/Live%20on-Render-8A2BE2?style=for-the-badge&logo=render&logoColor=white)](https://insurance-premium-prediction-iv8b.onrender.com)

---
## 🐳 Docker Images

 [![Docker Hub](https://img.shields.io/badge/Docker%20Hub-Images-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/u/amitpatel108)
 
- Backend: https://hub.docker.com/r/amitpatel108/insurance-premium-backend
- Frontend: https://hub.docker.com/r/amitpatel108/insurance-premium-frontend
---


## 👤 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit%20Kumar-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amit-kumar-c/)
[![GitHub](https://img.shields.io/badge/GitHub-PatelG108-181717?style=for-the-badge&logo=github)](https://github.com/PatelG108)

---

An end-to-end **Machine Learning + Backend + Frontend** project that predicts an **Insurance Premium Category (Low / Medium / High)** based on user health, lifestyle, and financial information.

The project is fully **Dockerized** with:
- **FastAPI** as backend (ML inference API)
- **Streamlit** as frontend (modern UI)
- **Scikit-learn** trained ML model
- Clean schema validation using **Pydantic**




## 🚀 Features

- Predict insurance premium category
- Confidence score for prediction
- Probability distribution for all classes
- Modern UI with color-coded results
- Health check & model versioning
- Docker & Docker Compose support
- Production-ready project structure

---

## 🖼️ Application Screenshots

### 🔹 VS-Code
![Frontend UI](screenshots/code.png)

### 🔹 Streamlit Frontend
![Frontend UI](screenshots/frontend-dm.png)
![Frontend UI](screenshots/frontend-lm.png)

### 🔹 Prediction Result
![Prediction Output](screenshots/output-dm.png)
![Prediction Output](screenshots/output-lm.png)

### 🔹 FastAPI Swagger Docs
![Swagger UI](screenshots/swagger-1.png)
![Swagger UI](screenshots/swagger-2.png)

---

## 🧠 Tech Stack

### Backend
- Python
- FastAPI
- Pydantic
- Scikit-learn
- Pandas

### Frontend
- Streamlit
- Custom CSS

### DevOps
- Docker
- Docker Compose
- GitHub

---

## 📦 Project Structure

```
Insurance-premium/
│
├── app.py                      # FastAPI application entry point
├── frontend.py                 # Streamlit frontend UI
│
├── docker-compose.yml          # Run backend & frontend together
├── Dockerfile.backend          # Backend Docker image
├── Dockerfile.frontend         # Frontend Docker image
│
├── requirements-backend.txt    # Backend dependencies
├── requirements-frontend.txt   # Frontend dependencies
│
├── Model/
│   ├── model.pkl               # Trained ML model
│   └── predict.py              # Prediction logic
│
├── schema/
│   ├── User_input.py           # Input validation schema
│   └── prediction_response.py  # Output response schema
│
├── config/
│   └── city_tier.py            # City tier mapping logic
│
├── Ml-Code/
│   ├── insurance.csv           # Training dataset
│   └── insurance.ipynb         # Model training notebook
│
├── venv/                       # Virtual environment (ignored in Git)
├── .gitignore                  # Git ignore rules
└── .vscode/                    # VS Code settings

```

## 👨🏻‍💻 Example

```
json

{
  "age": 30,
  "weight": 65,
  "height": 1.7,
  "income_lpa": 10,
  "smoker": true,
  "city": "Mumbai",
  "occupation": "private_job"
}

```
### Response

```
json

{
  "predicted_category": "Low",
  "confidence": 0.47,
  "class_probabilities": {
    "Low": 0.47,
    "Medium": 0.45,
    "High": 0.08
  }
}

```
---
# 👤 Author

📌 Developed by **Amit Kumar**  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit%20Kumar-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amit-kumar-c/)
[![GitHub](https://img.shields.io/badge/GitHub-PatelG108-181717?style=for-the-badge&logo=github)](https://github.com/PatelG108)



- B.Tech CSE (Data Science)
- Focus: AI · ML · Backend · Deployment

