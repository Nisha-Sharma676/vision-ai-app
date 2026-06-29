from flask import Flask, request, jsonify, render_template
import os, requests

app = Flask(__name__)

# Environment variables
VISION_KEY = os.environ.get("VISION_KEY")
VISION_ENDPOINT = os.environ.get("VISION_ENDPOINT")

# Safety check (important for Vercel)
if not VISION_ENDPOINT:
    VISION_ENDPOINT = ""

if not VISION_ENDPOINT.endswith("/"):
    VISION_ENDPOINT += "/"

URL = VISION_ENDPOINT + "computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags,read"

headers = {
    "Ocp-Apim-Subscription-Key": VISION_KEY,
    "Content-Type": "application/json"
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    try:
        # Case 1: URL image
        if "url" in data:
            body = {"url": data["url"]}

        # Case 2: Base64 image (safe fallback)
        elif "image_base64" in data:
            image_data = data["image_base64"].split(",")[1]
            body = {"data": image_data}

        else:
            return jsonify({"error": "No input provided"})

        response = requests.post(URL, headers=headers, json=body)

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)})

# Vercel requirement
app = app
