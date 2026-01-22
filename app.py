import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def run_ai(user_input):
    return "AI: " + user_input

@app.route("/")
def home():
    return "AI is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    return jsonify({"reply": run_ai(data["message"])})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)