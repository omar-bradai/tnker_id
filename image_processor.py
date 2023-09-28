import cv2
import numpy as np
from OCR import OCR
import gradio as gr
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api")
def process_image():
    # remove any previous files from outputs directory:
    dir_path = r"C:/Users/omarb/Downloads/waj/outputs"
    for file_path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file_path)) and file_path.split(".")[1] != "txt":
            os.remove(os.path.join(dir_path, file_path))

    # Load the image
    image_path = str(request.args.get('path'))
    image = cv2.imread(image_path)
    rows, cols, _ = image.shape
    print("Rows", rows)
    print("Cols", cols)

    # segment image

    # name infos
    names = image[int(rows//2.5): rows, cols//3: cols]
    cv2.imwrite('outputs/name_infos.jpg', names)
    # # --> let's segment even further
    # rows_i, cols_i, _ = names.shape
    # name_parts = []
    # den = rows_i
    # den2 = 5
    # for i in range(5):
    #     name_parts.append(
    #         names[int(rows_i//den): int(rows_i // den2), 0: cols_i])
    #     if den == rows_i:
    #         den = 5
    #         den2 -= 1
    #     else:
    #         den -= 1
    #         den2 -= 1

    # for i, img in enumerate(name_parts):
    #     cv2.imwrite(f"outputs/name_infos_{i}.jpg", img)

    # CIN number
    number = image[int(rows//4.5): int(rows//2.2), cols//4:  int(cols//1.2)]
    cv2.imwrite('outputs/number.jpg', number)

    # Define a kernel for dilation and erosion
    kernel = np.ones((3, 3), np.uint8)

    # Perform erosion
    eroded_names = cv2.erode(names, kernel, iterations=1)
    eroded_number = cv2.erode(number, kernel, iterations=1)

    # Threshold the eroded image to obtain a binary result
    _, binary_names = cv2.threshold(eroded_names, 70, 255, cv2.THRESH_BINARY)
    _, binary_number = cv2.threshold(
        eroded_number, 70, 255, cv2.THRESH_BINARY)

    # Save the resulting images
    cv2.imwrite('outputs/binary_names.jpg', binary_names)
    cv2.imwrite('outputs/binary_number.jpg', binary_number)

    # remove noise
    dst_names = cv2.blur(binary_names, (3, 3))
    dst_number = cv2.blur(binary_number, (3, 3))

    # extract dark regions which corresponds to text
    val_names, dst_names = cv2.threshold(
        dst_names, 50, 255, cv2.THRESH_BINARY_INV)
    val_number, dst_number = cv2.threshold(
        dst_number, 50, 255, cv2.THRESH_BINARY_INV)

    # morphological close to connect seperated blobs
    dst_names = cv2.dilate(dst_names, None)
    dst_names = cv2.erode(dst_names, None)

    dst_number = cv2.dilate(dst_number, None)
    dst_number = cv2.erode(dst_number, None)

    # Save the resulting images
    cv2.imwrite('outputs/dst_names.jpg', dst_names)
    cv2.imwrite('outputs/dst_number.jpg', dst_number)

    OCR_image = OCR()
    OCR_image.image = 'outputs/dst_names.jpg'

    transcriptions = OCR_image.get_info()

    return jsonify(transcriptions)


# title = "Tnker National ID information extractor"
# description = "This is an interface for testing the NID (CIN) ocr model for Tnker"
# gr.Interface(
#     fn=process_image,
#     title=title,
#     description=description,
#     inputs=[
#         gr.inputs.Image(source="upload", type='filepath', optional=True)],
#     outputs="text").launch()


if __name__ == '__main__':
    app.run(debug=True)
