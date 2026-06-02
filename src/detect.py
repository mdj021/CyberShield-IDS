import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/ids_model.pkl")

print("=== Intrusion Detection System ===")

print("\nEnter Network Traffic Features")

features = []

for i in range(41):
    value = float(input(f"Feature {i+1}: "))
    features.append(value)

data = pd.DataFrame([features])

prediction = model.predict(data)

if prediction[0] == 0:
    print("\nNormal Traffic")
else:
    print("\nAttack Detected!")