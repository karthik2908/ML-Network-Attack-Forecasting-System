import os
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

from src.config import DATA_PATH, MODEL_PATH, TARGET_COLUMN, RISK_THRESHOLD
from src.generate_sample_data import ensure_sample_data


def preprocess_data(df):
    df = df.copy()
    for col in df.columns:
        if col == TARGET_COLUMN:
            continue
        if df[col].isnull().sum() > 0:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(df[col].median())
            else:
                df[col] = df[col].fillna(df[col].mode()[0])

    target = df[TARGET_COLUMN].map({"normal": 0, "attack": 1})
    features = df.drop(columns=[TARGET_COLUMN])
    features = pd.get_dummies(features, columns=["protocol_type"], drop_first=True)

    return features, target


def train_model():
    ensure_sample_data()
    df = pd.read_csv(DATA_PATH)
    X, y = preprocess_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=12,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-score: {f1:.4f}")
    print(classification_report(y_test, y_pred, target_names=["normal", "attack"]))

    model_bundle = {
        "model": model,
        "feature_columns": list(X.columns),
        "threshold": RISK_THRESHOLD,
    }

    os.makedirs(str(MODEL_PATH.parent), exist_ok=True)
    import joblib
    joblib.dump(model_bundle, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

    return model_bundle
