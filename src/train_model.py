import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd

def train_random_forest(X_train, y_train):
    """Trains and returns a Random Forest model."""
    model = RandomForestRegressor(n_estimators=300, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    # Load preprocessed dataset
    dataset_path = "../data/train_FD001.txt"
    df = pd.read_csv(dataset_path, sep=r"\s+", engine="python")

    # Prepare data
    X = df.drop(columns=["unit", "time_in_cycles", "RUL"])
    y = df["RUL"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = train_random_forest(X_train, y_train)

    # Save model
    joblib.dump(model, "../models/final_random_forest.pkl")
    print("Model trained and saved successfully!")
