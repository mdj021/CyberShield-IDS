import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_data():
    file_path = "dataset/KDDTrain+.txt"

    df = pd.read_csv(file_path, header=None)

    print("Original Shape:", df.shape)

    # Convert categorical columns
    encoder = LabelEncoder()

    for col in [1, 2, 3]:
        df[col] = encoder.fit_transform(df[col])

    # Label column
    label_col = 41

    df[label_col] = df[label_col].apply(
        lambda x: 0 if x == "normal" else 1
    )

    X = df.drop(columns=[41, 42])
    y = df[41]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training Samples:", len(X_train))
    print("Testing Samples:", len(X_test))

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    preprocess_data()