from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# DeepSeek API的URL和API密钥
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat"
DEEPSEEK_API_KEY = "sk-f3a0e394f8f5489cab316e2ed8667519"

def get_deepseek_response(user_input):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "message": user_input
    }
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("reply", "Sorry, I couldn't process that.")
    else:
        return "Sorry, there was an error connecting to DeepSeek."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"reply": "Please provide a message."}), 400
    reply = get_deepseek_response(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)