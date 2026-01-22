from flask import Flask, request, jsonify

app = Flask(__name__)

def run_ai(user_input):
    return "AI: " + user_input

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_text = data["message"]
    return jsonify({"reply": run_ai(user_text)})

app.run(host="0.0.0.0", port=3000)
port = int(os.environ.get("PORT", 10000))