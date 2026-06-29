from flask import Flask, request, jsonify, render_template
import os, requests

app = Flask(__name__)

VISION_KEY = os.environ.get("VISION_KEY")
VISION_ENDPOINT = os.environ.get("VISION_ENDPOINT")

URL = VISION_ENDPOINT + "computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags,read,objects"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json

        headers = {
            "Ocp-Apim-Subscription-Key": VISION_KEY,
            "Content-Type": "application/json"
        }

        body = {"url": data["url"]}

        response = requests.post(URL, headers=headers, json=body)

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)})

app = app
