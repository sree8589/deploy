import pickle
from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load or Train model
def train_model():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    with open("app/model.pkl", "wb") as f:
        pickle.dump(model, f)

try:
    with open("app/model.pkl", "rb") as f:
        model = pickle.load(f)
except:
    train_model()
    with open("app/model.pkl", "rb") as f:
        model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    prediction = model.predict([data["features"]])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
