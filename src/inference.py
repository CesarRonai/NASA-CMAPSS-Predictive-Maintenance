import joblib
import pandas as pd

def predict_rul(model, X_new):
    """Predicts RUL for new data."""
    return model.predict(X_new)

if __name__ == "__main__":
    # Load trained model
    model_path = "../models/final_random_forest.pkl"
    model = joblib.load(model_path)

    # Load new data (example)
    dataset_path = "../data/test_FD001.txt"
    df = pd.read_csv(dataset_path, sep=r"\s+", engine="python")
    X_new = df.drop(columns=["unit", "time_in_cycles"])

    # Make predictions
    predictions = predict_rul(model, X_new)
    print("Predicted RUL:", predictions[:10])
