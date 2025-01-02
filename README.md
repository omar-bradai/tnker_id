Tunisian ID Card OCR Backend 🎉

This project is the backend component of a Tunisian ID Card OCR system, which integrates AI-driven Optical Character Recognition (OCR) to extract and process text data from images of Tunisian ID cards. The backend is developed using Python and serves as the core engine for image processing and text extraction, connecting seamlessly with a Flutter-based mobile application.

🌟 Key Features

OCR for Tunisian ID Cards: Utilizes advanced OCR techniques to extract key information like CIN numbers and names from ID card images.

Arabic Text Support: Tailored to handle Arabic text recognition effectively.

Image Pre-Processing: Includes image enhancement techniques such as thresholding and sharpening to improve OCR accuracy.

REST API: Exposes endpoints for uploading and processing ID card images, returning the extracted text data.

🚀 Workflow

Image Capture: The Flutter app captures an image of the Tunisian ID card using the device's camera and sends it to the Python API.

Data Transfer: The image is sent to the backend via a secure HTTP request.

OCR Processing:

The backend applies image pre-processing techniques (e.g., rotation, binarization) to enhance the image quality.

The OCR engine extracts the text, focusing on key fields like CIN number and name.

Data Return: Extracted information is returned as a JSON response to the Flutter app for display or further use.

🛠️ Technologies Used

Python: Core programming language for the backend.

Flask: Lightweight web framework for creating the API.

ArabicOCR: OCR library for Arabic text extraction.

OpenCV: For image processing tasks.

📂 Project Structure

├── app.py                # Main Flask app with API endpoints
├── OCR.py                # OCR processing logic
├── Binary_photo.py       # Image thresholding and pre-processing script
├── outputs/              # Directory for processed images and output files
└── uploads/              # Directory for temporarily storing uploaded images

📋 API Endpoints

1. Process Image Endpoint

URL: /api/<path:image_path>

Method: GET

Description: Processes the uploaded ID card image, extracts key information, and returns it as JSON.

2. Upload Image Endpoint

URL: /upload

Method: POST

Description: Accepts image uploads from the Flutter app and stores them temporarily for processing.

✨ Image Pre-Processing Workflow

Grayscale Conversion: Converts the image to grayscale for easier processing.

Rotation Correction: Adjusts the orientation of the image.

Region Segmentation: Identifies and extracts specific regions of interest (e.g., name, CIN number).

Thresholding: Binarizes the image to enhance contrast for OCR.

Sharpening: Enhances image edges for better text recognition.

🔍 OCR Engine Highlights

Library: ArabicOCR

Capabilities: Specializes in recognizing Arabic text, making it ideal for Tunisian ID cards.

Output: Extracted text is structured into key fields for easy use.

🌐 Integration with Flutter

The Flutter app serves as the frontend, handling image capture and displaying the extracted data. It interacts with the Python backend through the following workflow:

Capture Image: Users take a picture of the ID card in the app.

Send Image: The app sends the image to the backend via an HTTP request.

Receive Data: The backend processes the image and returns the extracted text data as JSON.


