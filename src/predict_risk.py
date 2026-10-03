import joblib
import pandas as pd

from src.config import MODEL_PATH


def predict_single_record(record):
    bundle = joblib.load(MODEL_PATH)
    model = bundle["model"]
    feature_columns = bundle["feature_columns"]
    threshold = bundle["threshold"]

    df = pd.DataFrame([record])
    df = df.copy()

    if "label" in df.columns:
        df = df.drop(columns=["label"])

    if "protocol_type" in df.columns:
        protocol_dummies = pd.get_dummies(df["protocol_type"], prefix="protocol_type")
        df = df.drop(columns=["protocol_type"])
        df = pd.concat([df.reset_index(drop=True), protocol_dummies.reset_index(drop=True)], axis=1)

    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0

    # Keep only expected feature columns in training order.
    df = df[feature_columns]

    probability = model.predict_proba(df)[0][1]
    prediction = int(model.predict(df)[0])
    risk_score = float(probability)
    status = "High Risk" if risk_score >= threshold else "Low Risk"

    return {
        "predicted_label": prediction,
        "risk_score": round(risk_score, 4),
        "status": status,
    }
