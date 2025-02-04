import pandas as pd

def load_data(filepath):
    """Loads dataset from a given filepath."""
    columns = ["unit", "time_in_cycles", "operational_setting_1", "operational_setting_2", "operational_setting_3",
               "sensor_1", "sensor_2", "sensor_3", "sensor_4", "sensor_5",
               "sensor_6", "sensor_7", "sensor_8", "sensor_9", "sensor_10",
               "sensor_11", "sensor_12", "sensor_13", "sensor_14", "sensor_15",
               "sensor_16", "sensor_17", "sensor_18", "sensor_19", "sensor_20", "sensor_21"]
    
    df = pd.read_csv(filepath, sep=r"\s+", header=None, names=columns, engine="python")
    return df

def add_rul_column(df):
    """Adds Remaining Useful Life (RUL) column to the dataset."""
    df["RUL"] = df.groupby("unit")["time_in_cycles"].transform(lambda x: x.max() - x)
    return df

if __name__ == "__main__":
    dataset_path = "../data/train_FD001.txt"
    df = load_data(dataset_path)
    df = add_rul_column(df)
    print(df.head())
