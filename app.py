from flask import Flask, request, jsonify, render_template
import os, requests
import base64

app = Flask(__name__)

VISION_KEY = os.getenv("VISION_KEY")
VISION_ENDPOINT = os.getenv("VISION_ENDPOINT")

URL = VISION_ENDPOINT + "computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags,read,objects"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    headers = {
        "Ocp-Apim-Subscription-Key": VISION_KEY,
        "Content-Type": "application/octet-stream"
    }

    # CASE 1: URL
    if data.get("url"):
        body = requests.get(data["url"]).content

    # CASE 2: FILE UPLOAD
    else:
        image_data = data["image_base64"].split(",")[1]
        body = base64.b64decode(image_data)

    response = requests.post(URL, headers=headers, data=body)

    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)