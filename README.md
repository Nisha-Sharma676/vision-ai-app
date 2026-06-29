Azure AI Vision App

A full-stack web application built using Flask and Microsoft Azure Computer Vision API that performs intelligent image analysis. Users can upload an image or provide an image URL to get AI-powered insights like captioning, tagging (including brand detection), and OCR text extraction.

Features
- Image upload from device
- Image analysis via image URL
- AI-generated image captions
- Smart tag detection (objects, brands, categories)
- Face-related detection (via tags)
- Landmark recognition (based on AI tags)
- OCR text extraction from images
- Real-time API response using Azure AI Vision

Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
AI Service: Microsoft Azure Computer Vision API
Deployment: Vercel + GitHub

Project Structure
vision-ai-app/
│
├── app.py
├── requirements.txt
├── vercel.json
├── README.md
├── .gitignore
│
├── templates/
│     └── index.html