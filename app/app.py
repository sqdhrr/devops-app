from flask import Flask, jsonify

# this MUST be called "app"
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from my DevOps pipeline!"

@app.route("/health")
def health():
    return jsonify(status="ok")

