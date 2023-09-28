import socket
from tkinter import Image
import cv2
import numpy as np
import requests
from OCR import OCR
import gradio as gr
import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route("/api/<path:image_path>")
def process_image(image_path):
    # remove any previous files from outputs directory:
    dir_path = r"C:/Users/omarb/Downloads/waj/outputs"
    for file_path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file_path)) and file_path.split(".")[1] != "txt":
            os.remove(os.path.join(dir_path, file_path))

    # Load the image
    image_path = image_path.split('5000/')[1].split(' HTTP')[0]
    print(image_path)
    img = os.path.join(image_path)
    image_row = cv2.imread(img, cv2.COLOR_BGR2GRAY)

    image = cv2.rotate(image_row, cv2.ROTATE_90_COUNTERCLOCKWISE)
    rows, cols, _ = image.shape
    print("Rows", rows)
    print("Cols", cols)
    # segment image

    # name infos
    names = image[int(rows//2.2): rows, cols//3: cols]
    cv2.imwrite('outputs/name_infos.jpg', names)
    rows_1, cols_1, _ = names.shape
    names_1 = names[0: int(rows_1//2.4), int(cols//3.5): cols]
    cv2.imwrite('outputs/name_1_infos.jpg', names_1)
    # CIN number
    number = image[int(rows//3.5): int(rows//2.2), cols//4:  int(cols//1.2)]
    cv2.imwrite('outputs/number.jpg', number)

    # processing

    ret, thresh1 = cv2.threshold(names, 140, 255, cv2.THRESH_BINARY)
    # Create the sharpening kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # Sharpen the image
    sharpened_image = cv2.filter2D(names_1, -1, kernel)
    cv2.imwrite('outputs/sharpened_names.jpg', sharpened_image)
    sharpened_number = cv2.filter2D(number, -1, kernel)
    cv2.imwrite('outputs/sharpened_umber.jpg', sharpened_number)

    OCR_image = OCR()
    OCR_image.image = 'outputs/name_1_infos.jpg'
    transcriptions = OCR_image.get_info()

    OCR_number = OCR()
    OCR_number.image = 'outputs/number.jpg'
    transcriptions_number = OCR_number.get_info()

    return jsonify('CIN number : ' + transcriptions_number + '\n' + '\n' + 'name : ' + transcriptions)


# title = "Tnker National ID information extractor"
# description = "This is an interface for testing the NID (CIN) ocr model for Tnker"
# gr.Interface(
#     fn=process_image,
#     title=title,
#     description=description,
#     inputs=[
#         gr.inputs.Image(source="upload", type='filepath', optional=True)],
#     outputs="text").launch()

app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'})

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected image'})

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Replace with your server's URL
        url = f'http://172.18.184.107:5000/uploads/{filename}'
        return jsonify({'url': url})


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    # getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    app.run(debug=True, host=ip_address, port=5000)
