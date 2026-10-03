from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import pandas as pd


def ensure_sample_data():
    data_dir = Path(__file__).resolve().parents[1] / "data" / "raw"
    data_dir.mkdir(parents=True, exist_ok=True)
    file_path = data_dir / "network_traffic.csv"

    if file_path.exists():
        return file_path

    rng = np.random.default_rng(42)
    rows = []

    # Generate a balanced dataset with normal and malicious traffic patterns.
    for i in range(1200):
        attack = i % 2 == 0
        if attack:
            duration = int(rng.integers(20, 180))
            src_bytes = int(rng.integers(150, 1000))
            dst_bytes = int(rng.integers(500, 5000))
            protocol_type = rng.choice(["tcp", "udp", "icmp"])
            count = int(rng.integers(250, 900))
            srv_count = int(rng.integers(40, 200))
            serror_rate = round(float(rng.uniform(0.45, 0.95)), 3)
            rerror_rate = round(float(rng.uniform(0.35, 0.9)), 3)
            same_srv_rate = round(float(rng.uniform(0.3, 0.8)), 3)
            diff_srv_rate = round(float(rng.uniform(0.4, 0.9)), 3)
            label = "attack"
        else:
            duration = int(rng.integers(1, 80))
            src_bytes = int(rng.integers(50, 400))
            dst_bytes = int(rng.integers(100, 800))
            protocol_type = rng.choice(["tcp", "udp"])
            count = int(rng.integers(20, 180))
            srv_count = int(rng.integers(5, 80))
            serror_rate = round(float(rng.uniform(0.0, 0.2)), 3)
            rerror_rate = round(float(rng.uniform(0.0, 0.15)), 3)
            same_srv_rate = round(float(rng.uniform(0.7, 1.0)), 3)
            diff_srv_rate = round(float(rng.uniform(0.0, 0.3)), 3)
            label = "normal"

        rows.append({
            "duration": duration,
            "src_bytes": src_bytes,
            "dst_bytes": dst_bytes,
            "protocol_type": protocol_type,
            "count": count,
            "srv_count": srv_count,
            "serror_rate": serror_rate,
            "rerror_rate": rerror_rate,
            "same_srv_rate": same_srv_rate,
            "diff_srv_rate": diff_srv_rate,
            "label": label,
        })

    df = pd.DataFrame(rows)
    df.to_csv(file_path, index=False)
    return file_path
