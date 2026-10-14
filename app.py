from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Generate deterministic coefficients using student roll number
STUDENT_ROLL_NUMBER = 20
random.seed(STUDENT_ROLL_NUMBER)

a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

REGISTRATION_NUMBER = "FA23-BDS-020"


@app.route("/predict", methods=["GET"])
def predict():
    try:
        x1 = float(request.args["x1"])
        x2 = float(request.args["x2"])
        x3 = float(request.args["x3"])

        prediction = a1 * x1 + a2 * x2 + a3 * x3 + b

        return jsonify({
            "registration number": REGISTRATION_NUMBER,
            "prediction": round(prediction, 2)
        })
    except (KeyError, ValueError):
        return jsonify({
            "error": "Provide numeric x1, x2, and x3 parameters."
        }), 400


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Linear Regression Prediction API",
        "endpoint": "/predict?x1=2&x2=3&x3=1"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
