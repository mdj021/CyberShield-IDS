import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Load Dataset
df = pd.read_csv("dataset/KDDTrain+.txt", header=None)

print("Dataset Loaded Successfully")
print("Shape:", df.shape)

# Encode categorical columns
encoder = LabelEncoder()

for col in [1, 2, 3]:
    df[col] = encoder.fit_transform(df[col])

# Convert labels
df[41] = df[41].apply(
    lambda x: 0 if x == "normal" else 1
)

# Features and Labels
X = df.drop(columns=[41, 42])
y = df[41]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Model...")

# Train Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation Metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"\nAccuracy : {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall   : {recall * 100:.2f}%")
print(f"F1 Score : {f1 * 100:.2f}%")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
plt.imshow(cm, cmap="Blues")

plt.title("Confusion Matrix")
plt.colorbar()

for i in range(len(cm)):
    for j in range(len(cm[i])):
        plt.text(j, i, str(cm[i][j]),
                 ha="center",
                 va="center")

plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.xticks([0, 1], ["Normal", "Attack"])
plt.yticks([0, 1], ["Normal", "Attack"])

plt.tight_layout()

plt.savefig("screenshots/confusion_matrix.png")

print("\nConfusion Matrix Saved!")

# Save Model
joblib.dump(model, "models/ids_model.pkl")

print("Model Saved Successfully!")