from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_TOKEN")  # aquí uso variable de entorno definida en render
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/", methods=["GET"])
def home():
    return "sofibot funcionando"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Respuesta simple
        reply = f"Me dijiste: {text}"

        requests.post(URL, json={
            "chat_id": chat_id,
            "text": reply
        })

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)