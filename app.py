from fastapi import FastAPI
from schema.prediction_response import PredictionResponse
from schema.User_input import InsuranceRequest
from Model.predict import model, MODEL_VERSION, predict_output

# -- Initialize FastAPI app --
app = FastAPI()

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API!"}

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "model_status": "loaded" if model else "not loaded",
        "version": MODEL_VERSION
    }

# Prediction endpoint (STRICT & SAFE)
@app.post("/predict", response_model=PredictionResponse)
def predict_insurance_premium(data: InsuranceRequest):

    user_input = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }

    prediction_result = predict_output(user_input)

    return PredictionResponse(
        predicted_category=prediction_result["predicted_category"],
        confidence=prediction_result["confidence"],
        class_probabilities=prediction_result["class_probabilities"]
    )
