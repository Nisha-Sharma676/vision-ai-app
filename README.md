# Azure AI Vision App

A full-stack web application built using **Python Flask** and **Microsoft Azure AI Vision API**. The application analyzes images from a URL or an uploaded file and provides AI-powered insights such as image captions, tags, and OCR text extraction.

## Features

* Image upload from device
* Image analysis using image URL
* AI-generated image captions
* Smart tag detection
* OCR text extraction from images
* Real-time image analysis using Azure AI Vision API

## Tech Stack

* Frontend: HTML, CSS, JavaScript
* Backend: Python (Flask)
* AI Service: Microsoft Azure AI Vision API
* Deployment: Vercel + GitHub

## Project Structure

```
vision-ai-app/
│
├── app.py
├── requirements.txt
├── vercel.json
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
```

## Run Locally

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Set environment variables

```
VISION_KEY=your_azure_key
VISION_ENDPOINT=your_azure_endpoint
```

3. Run the application

```bash
python app.py
```

4. Open your browser

```
http://127.0.0.1:5000
```

## Deployment

This project is deployed using **GitHub** and **Vercel**.
