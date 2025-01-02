# Tunisian ID Card OCR Backend 🎉

This project is the **backend component** of a Tunisian ID Card OCR system, designed to extract and process text data from ID card images using AI-driven Optical Character Recognition (OCR). Developed in Python, this backend serves as the core processing engine, seamlessly integrating with a Flutter-based mobile application.

---

## 🌟 Key Features

- **OCR for Tunisian ID Cards**: Extracts key information like CIN numbers and names from ID card images.
- **Arabic Text Support**: Optimized for Arabic text recognition.
- **Image Pre-Processing**: Applies techniques such as thresholding and sharpening to improve OCR accuracy.
- **REST API**: Provides endpoints for uploading and processing ID card images, returning extracted text data.

---

## 🚀 Workflow

1. **Image Capture**: The Flutter app captures an image of the Tunisian ID card using the device's camera and sends it to the Python API.
2. **Data Transfer**: The image is transmitted to the backend via a secure HTTP request.
3. **OCR Processing**:
   - Pre-processing techniques (e.g., rotation, binarization) enhance the image quality.
   - The OCR engine extracts text, focusing on fields like CIN number and name.
4. **Data Return**: Extracted information is returned as a JSON response to the Flutter app for display or further use.

---

## 🛠️ Technologies Used

- **Python**: Core programming language for the backend.
- **Flask**: Lightweight web framework for creating the API.
- **ArabicOCR**: OCR library specializing in Arabic text extraction.
- **OpenCV**: Handles image processing tasks.

---

## 📂 Project Structure

```
├── app.py                # Main Flask app with API endpoints
├── OCR.py                # OCR processing logic
├── Binary_photo.py       # Image thresholding and pre-processing script
└── outputs/              # Directory for processed images and output files
```

---

## 📋 API Endpoints

### 1. Process Image Endpoint
- **URL**: `/api/<path:image_path>`
- **Method**: `GET`
- **Description**: Processes the uploaded ID card image, extracts key information, and returns it as JSON.

### 2. Upload Image Endpoint
- **URL**: `/upload`
- **Method**: `POST`
- **Description**: Accepts image uploads from the Flutter app and stores them temporarily for processing.

---

## ✨ Image Pre-Processing Workflow

1. **Grayscale Conversion**: Converts the image to grayscale for easier processing.
2. **Rotation Correction**: Adjusts the orientation of the image.
3. **Region Segmentation**: Identifies and extracts specific regions of interest (e.g., name, CIN number).
4. **Thresholding**: Binarizes the image to enhance contrast for OCR.
5. **Sharpening**: Enhances image edges for better text recognition.

---

## 🔍 OCR Engine Highlights

- **Library**: ArabicOCR
- **Capabilities**: Specializes in recognizing Arabic text, ideal for Tunisian ID cards.
- **Output**: Extracted text is structured into key fields for easy use.

---

## 🌐 Integration with Flutter

While this README focuses on the backend, it is essential to note the integration with a Flutter-based mobile app. The interaction is as follows:

1. **Capture Image**: Users take a picture of the ID card in the app.
2. **Send Image**: The app sends the image to the backend via an HTTP request.
3. **Receive Data**: The backend processes the image and returns the extracted text data as JSON.


