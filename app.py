
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "Message vide"}), 400

    try:
        # Simulation de réponse (à la place de localhost:11434)
        response_text = f"Infirmier Virtuel vous répond : {user_message}"
        return jsonify({"response": response_text})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Compatible avec Render
    app.run(host="0.0.0.0", port=port)




"""
from flask import Flask, request, jsonify, render_template
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "Message vide"}), 400

    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3",
            "prompt": user_message,
            "stream": False
        })

        data = response.json()
        return jsonify({"response": data.get("response", "Pas de réponse")})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)"""
     










"""from flask import Flask, request, jsonify, render_template
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "Message vide"}), 400

    try:
        # Option 1: Use Groq's FREE Llama3 API (no local setup)
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer YOUR_GROQ_API_KEY"},
            json={
                "model": "llama3-70b-8192",  # Groq's fast Llama3
                "messages": [{"role": "user", "content": user_message}]
            }
        )
        data = response.json()
        return jsonify({"response": data["choices"][0]["message"]["content"]})

        # Option 2: Keep local Llama3 (but host it separately)
        # response = requests.post("http://your-llama3-server.com/api/generate", ...)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500"""
