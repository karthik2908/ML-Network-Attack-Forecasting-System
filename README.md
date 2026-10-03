# Machine Learning-Based Network Attack Risk Forecasting and Early Warning System

## Overview
This project develops a proactive network security system that analyzes traffic behavior, detects anomalies, and forecasts attack risk using machine learning. Instead of reacting only after an attack begins, the system predicts risk from abnormal traffic patterns and raises early warnings.

## Project Idea
Traditional Intrusion Detection Systems (IDS) often detect malicious activity while it is occurring. This project goes a step further by forecasting the likelihood of an attack based on abnormal behavior indicators such as:
- sudden increase in connection volume
- failed connection attempts
- port scanning activity
- abnormal packet flow
- unusual protocol usage

## Features
- Network traffic feature extraction
- Data preprocessing and class balancing
- Machine learning-based abnormal traffic detection
- Risk score calculation
- Early warning generation
- Lightweight Flask dashboard

## Project Structure
```text
ML-Network-Attack-Forecasting-System/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── data/
│   └── raw/
│       └── network_traffic.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── generate_sample_data.py
│   ├── preprocess.py
│   ├── train_model.py
│   ├── predict_risk.py
│   └── dashboard.py
├── models/
│   └── attack_risk_model.joblib
└── notebooks/
    └── experiments.ipynb
```

## Setup
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

## Run the Project
```bash
python main.py
```
This trains the model and prints sample prediction output.

To launch the dashboard:
```bash
python src/dashboard.py
```
Then open:
```text
http://localhost:5000
```

## Sample Risk Scenario
Example input:
- connection count: 450
- failed connection rate: high
- port scan activity: detected
- packet rate: increasing rapidly

The system estimates a high risk score and triggers an early warning.

## Model
The current implementation uses a Random Forest classifier, which is robust for tabular network-traffic data and provides good classification performance with interpretable feature importance.

## Future Improvements
- LSTM/GRU for time-series attack forecasting
- Real-time traffic ingestion
- SIEM integration
- Explainable AI for security teams
- Multi-class attack classification

## License
This project is intended for educational and research purposes.
