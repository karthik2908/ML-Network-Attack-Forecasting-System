from src.generate_sample_data import ensure_sample_data
from src.train_model import train_model
from src.predict_risk import predict_single_record


def main():
    ensure_sample_data()
    train_model()

    sample = {
        "duration": 20,
        "src_bytes": 120,
        "dst_bytes": 500,
        "protocol_type": "tcp",
        "count": 450,
        "srv_count": 80,
        "serror_rate": 0.75,
        "rerror_rate": 0.65,
        "same_srv_rate": 0.90,
        "diff_srv_rate": 0.30,
        "label": "normal",
    }

    print(predict_single_record(sample))


if __name__ == "__main__":
    main()
