from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status":"running"}

@app.route("/predict-crime", methods=["POST"])
def predict():
    data = request.json
    return {"predicted_crime":"Theft","risk":"Medium"}

if __name__ == "__main__":
    app.run(debug=True)