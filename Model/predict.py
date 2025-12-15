import pickle
import pandas as pd

# ---import model--
with open('Model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"

# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    if model is None:
        raise RuntimeError("Model not loaded")

    df = pd.DataFrame([user_input])

    predicted_class = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]

    class_probs = {
        cls: float(round(prob, 4))
        for cls, prob in zip(class_labels, probabilities)
    }

    confidence = float(round(max(probabilities), 4))

    return {
        "predicted_category": predicted_class,
        "confidence": confidence,
        "class_probabilities": class_probs
    }
