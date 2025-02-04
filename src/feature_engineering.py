import pandas as pd

def remove_irrelevant_features(df):
    """Removes constant and highly correlated features."""
    # Remove constant features
    constant_features = [col for col in df.columns if df[col].nunique() == 1]
    df = df.drop(columns=constant_features)
    
    # Remove highly correlated features
    correlation_matrix = df.iloc[:, 3:].corr().abs()
    upper_triangle = correlation_matrix.where(pd.np.triu(pd.np.ones(correlation_matrix.shape), k=1).astype(bool))
    correlated_features = [column for column in upper_triangle.columns if any(upper_triangle[column] > 0.95)]
    df = df.drop(columns=correlated_features)

    return df

if __name__ == "__main__":
    dataset_path = "../data/train_FD001.txt"
    df = pd.read_csv(dataset_path, sep=r"\s+", engine="python")
    df = remove_irrelevant_features(df)
    print(df.head())
