from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "raw" / "network_traffic.csv"
MODEL_PATH = BASE_DIR / "models" / "attack_risk_model.joblib"
TARGET_COLUMN = "label"
RISK_THRESHOLD = 0.60
