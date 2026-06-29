from flask import Flask, request, jsonify
import os, requests
import base64

app = Flask(__name__)

VISION_KEY = os.environ.get("VISION_KEY")
VISION_ENDPOINT = os.environ.get("VISION_ENDPOINT")

URL = VISION_ENDPOINT + "computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags,read,objects,brands"

headers = {
    "Ocp-Apim-Subscription-Key": VISION_KEY,
    "Content-Type": "application/json"
}

@app.route("/")
def home():
    return "Vision AI App Running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    # CASE 1: URL
    if "url" in data:
        body = {"url": data["url"]}

    # CASE 2: Base64 image
    elif "image_base64" in data:
        image_data = data["image_base64"].split(",")[1]
        body = {"data": image_data}

    else:
        return jsonify({"error": "No valid input provided"})

    response = requests.post(URL, headers=headers, json=body)

    return jsonify(response.json())

# Vercel requirement
app = app
