from flask import Flask, request, jsonify, render_template
import requests

from openai import OpenAI

app = Flask(__name__)

# DeepSeek API的URL和API密钥
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_API_KEY = ""

def get_deepseek_response(user_input):
    # headers = {
    #     "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    #     "Content-Type": "application/json"
    # }
    # data = {
    #     "message": {
    #         "model": "deepseek-chat",
    #         "messages": [
    #             {"role": "system", "content": "You are a helpful assistant."},
    #             {"role": "user", "content": user_input}
    #         ],
    #         "stream": False
    #     }
    # }
    # response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
    # if response.status_code == 200:
    #     return response.json().get("reply", "Sorry, I couldn't process that.")
    # else:
    #     return response.text
    
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_input},
        ],
        stream=False
    )
    return response.choices[0].message.content
    


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