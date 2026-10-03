from src.generate_sample_data import ensure_sample_data
from src.train_model import train_model


def main():
    ensure_sample_data()
    train_model()


if __name__ == "__main__":
    main()
