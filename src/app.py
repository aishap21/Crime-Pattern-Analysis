from flask import Flask, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "API is running"

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

@app.route("/predict-crime", methods=["POST"])
def predict():
    try:
        data = request.json

        features = [[
            data['Latitude'],
            data['Longitude'],
            data['Hour'],
            data['Month']
        ]]

        prediction = model.predict(features)

        return {"prediction": str(prediction[0])}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(debug=True)
