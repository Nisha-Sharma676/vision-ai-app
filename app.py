from flask import Flask, request, jsonify, render_template
import os
import requests

app = Flask(__name__)

VISION_KEY = os.environ.get("VISION_KEY")
VISION_ENDPOINT = os.environ.get("VISION_ENDPOINT")

if not VISION_ENDPOINT.endswith("/"):
    VISION_ENDPOINT += "/"

URL = VISION_ENDPOINT + "computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags,read"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    headers = {
        "Ocp-Apim-Subscription-Key": VISION_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "url": data["url"]
    }

    response = requests.post(URL, headers=headers, json=body)

    return jsonify(response.json())


@app.route("/analyze-file", methods=["POST"])
def analyze_file():

    image = request.files["image"]

    headers = {
        "Ocp-Apim-Subscription-Key": VISION_KEY,
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(
        URL,
        headers=headers,
        data=image.read()
    )

    return jsonify(response.json())


app = app
