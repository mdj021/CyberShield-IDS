from flask import Flask, render_template, request
import pandas as pd
import joblib
import os
from src.pcap_analyzer import analyze_pcap
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load trained model
model = joblib.load("models/ids_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return "No file uploaded."

    file = request.files["file"]

    if file.filename == "":
        return "No file selected."

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    try:
        # Read CSV without header
        df = pd.read_csv(filepath, header=None)

        print("Shape:", df.shape)

        if df.empty:
            return "Uploaded CSV is empty."

        if df.shape[1] != 41:
            return f"Error: Expected 41 columns but found {df.shape[1]} columns."

        predictions = model.predict(df)

        df["Prediction"] = predictions

        df["Prediction"] = df["Prediction"].replace({
            0: "Normal",
            1: "Attack"
        })

        result_file = os.path.join(
            RESULT_FOLDER,
            "predictions.csv"
        )

        df.to_csv(result_file, index=False)

        table = df.head(20).to_html(
            classes="table table-bordered",
            index=False
        )

        return render_template(
            "results.html",
            table=table
        )

    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["pcapfile"]

    filepath = os.path.join(
        "uploads",
        file.filename
    )

    file.save(filepath)

    result = analyze_pcap(filepath)

    return render_template(
        "results.html",
        result=result
    )
if __name__ == "__main__":
    app.run(debug=True)