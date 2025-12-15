# Insurance Premium Prediction

Predict insurance premiums from customer features (age, sex, BMI, children, smoking status, region). This repository contains the data processing, model training, API and example UI to estimate insurance charges for new customers.

- Repository: [PatelG108/Insurance-premium](https://github.com/PatelG108/Insurance-premium)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Quick Installation](#quick-installation)
- [Usage](#usage)
  - [Run the API](#run-the-api)
  - [Run the demo UI (Streamlit)](#run-the-demo-ui-streamlit)
  - [Example API request](#example-api-request)
- [Data](#data)
- [Model Training](#model-training)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

Insurance Premium Prediction is a small ML project that predicts medical insurance charges using standard demographic and health features. It can be used as a learning project or as a lightweight prediction service in an application.

## Features

- Data ingestion and preprocessing pipeline
- Exploratory Data Analysis (notebooks)
- Model training and evaluation scripts
- REST API to serve predictions
- Small demo UI (Streamlit) to interactively estimate premiums
- Dockerfile for containerized deployment

## Tech Stack

- Python 3.8+
- pandas, scikit-learn, joblib
- Flask or FastAPI (API)
- Streamlit (demo UI)
- Docker (optional)

## Getting Started

### Prerequisites

- Python 3.8 or later
- git
- Optional: Docker (for containerized run)

### Quick Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PatelG108/Insurance-premium.git
   cd Insurance-premium
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows (PowerShell)
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

If there is no `requirements.txt`, typical packages include:
```text
pandas
numpy
scikit-learn
joblib
flask        # or fastapi + uvicorn
streamlit
```

## Usage

### Run the API

If the project uses Flask:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

If it uses FastAPI:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API serves a `/predict` endpoint that accepts JSON and returns the predicted premium.

### Run the demo UI (Streamlit)

```bash
streamlit run app_streamlit.py
```

Open the provided URL (usually `http://localhost:8501`) and use the interactive form to estimate insurance charges.

### Example API request

Request:
```bash
curl -X POST "http://localhost:5000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 40,
    "sex": "male",
    "bmi": 30.5,
    "children": 2,
    "smoker": "no",
    "region": "southeast"
  }'
```

Response (example):
```json
{
  "predicted_premium": 12345.67
}
```

## Data

Place your dataset in the `data/` folder (e.g., `data/insurance.csv`). A common dataset layout includes columns such as:

- age (int)
- sex (male/female)
- bmi (float)
- children (int)
- smoker (yes/no)
- region (northeast/northwest/southeast/southwest)
- charges (float) — target

If you do not have data, the [Kaggle "Medical Cost Personal Datasets"](https://www.kaggle.com/datasets/mirichoi0218/insurance) is a commonly used example.

## Model Training

A training script (e.g., `train.py`) should:

1. Load and clean the dataset
2. Encode categorical features (one-hot or ordinal where appropriate)
3. Split into train/test sets
4. Train a regression model (LinearRegression, RandomForestRegressor, GradientBoosting, or similar)
5. Evaluate using MAE, RMSE, R^2
6. Save the trained model with joblib/pickle to `models/` (e.g., `models/model.joblib`)

Example (conceptual) training command:
```bash
python train.py --data data/insurance.csv --output models/model.joblib
```

Example evaluation metrics to aim for:
- MAE: lower is better
- RMSE: lower is better
- R^2: closer to 1 is better

## Project Structure

A suggested layout:

```
Insurance-premium/
├─ data/
│  └─ insurance.csv
├─ notebooks/
│  └─ eda.ipynb
├─ src/
│  ├─ data_processing.py
│  ├─ features.py
│  ├─ model.py
│  └─ predict.py
├─ app.py                 # Flask/FastAPI app
├─ app_streamlit.py       # Streamlit demo UI
├─ train.py
├─ requirements.txt
├─ Dockerfile
└─ README.md
```

Adjust according to your repo's existing layout.

## Testing

Add unit tests for preprocessing functions and the prediction endpoint. Example using pytest:

```bash
pytest tests/
```

Example test to check model prediction shape and types.

## Deployment

- Docker:
  - Build: `docker build -t insurance-premium .`
  - Run: `docker run -p 5000:5000 insurance-premium`

- Cloud: You can deploy the API to services like Heroku, AWS Elastic Beanstalk, Google Cloud Run, or Azure App Service. For production, ensure environment variables and secret management are handled securely.

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repo
2. Create a branch: `git checkout -b feat/new-feature`
3. Commit changes and push: `git push origin feat/new-feature`
4. Open a Pull Request

Please include tests and update the README if you add or change functionality.

## License

Specify a license (e.g., MIT) in `LICENSE` file. Example:
```
MIT License
```

## Contact

Maintainer: PatelG108  
Repository: [https://github.com/PatelG108/Insurance-premium](https://github.com/PatelG108/Insurance-premium)

---

If you'd like, I can:
- Customize this README to reflect files already in your repo (I can inspect the repo and update the README accordingly), or
- Open a PR / push the README to the repository. Tell me which you'd prefer.

If you'd like any customization of this README (add badges, CI status, or tailor setup for a specific language/framework present in the repo), tell me which language or framework the project uses and I will update the README accordingly.
