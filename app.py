from flask import Flask, request, jsonify, send_file
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        # Here you can call your image processing function
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200

def process_and_crop_image(image_path, processed_folder='processed'):
    # Ensure processed folder exists
    if not os.path.exists(processed_folder):
        os.makedirs(processed_folder)

    # Read the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blur, 75, 200)

    # Find contours
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cropped_images = []
    for i, contour in enumerate(contours):
        # Compute the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Use aspect ratio and area filtering here (adjust values as needed)
        aspect_ratio = w / float(h)
        area = w * h
        if 0.6 < aspect_ratio < 1.4 and 10000 < area < 30000:  # Example values, adjust based on your images
            cropped_image = img[y:y+h, x:x+w]
            cropped_image_path = os.path.join(processed_folder, f'card_{i}.png')
            cv2.imwrite(cropped_image_path, cropped_image)
            cropped_images.append(cropped_image_path)

    return cropped_images


if __name__ == '__main__':
    app.run(debug=True)
