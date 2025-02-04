import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluate_model(model, X_test, y_test):
    """Evaluates a model and prints MAE, MSE, and RMSE."""
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")

if __name__ == "__main__":
    # Load model
    model_path = "../models/final_random_forest.pkl"
    model = joblib.load(model_path)

    # Load test data
    dataset_path = "../data/train_FD001.txt"
    df = pd.read_csv(dataset_path, sep=r"\s+", engine="python")
    X = df.drop(columns=["unit", "time_in_cycles", "RUL"])
    y = df["RUL"]

    # Evaluate model
    evaluate_model(model, X, y)
