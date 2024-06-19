import os
from io import BytesIO
from urllib.request import urlopen

import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model('model.h5')

class_info = {
    0: {'name': 'anggur', 'calories': 69, 'carbs': 18.1, 'protein': 0.72, 'fat': 0.16},
    1: {'name': 'apel', 'calories': 52, 'carbs': 13.81, 'protein': 0.26, 'fat': 0.17},
    2: {'name': 'ayam-goreng', 'calories': 295, 'carbs': 10.76, 'protein': 37, 'fat': 14.7},
    3: {'name': 'ayam-kampung', 'calories': 246, 'carbs': 10.76, 'protein': 37.9, 'fat': 9},
    4: {'name': 'daging', 'calories': 288, 'carbs': 0, 'protein': 26.33, 'fat': 19.54},
    5: {'name': 'nasi', 'calories': 180, 'carbs': 39.8, 'protein': 3, 'fat': 0.3},
    6: {'name': 'pasta', 'calories': 157, 'carbs': 30.68, 'protein': 5.76, 'fat': 0.92},
    7: {'name': 'pisang', 'calories': 89, 'carbs': 22.48, 'protein': 1.09, 'fat': 0.33},
    8: {'name': 'roti', 'calories': 264, 'carbs': 55.81, 'protein': 9.61, 'fat': 1.3},
    9: {'name': 'sayur', 'calories': 60, 'carbs': 13.09, 'protein': 2.86, 'fat': 0.15},
    10: {'name': 'tahu', 'calories': 78, 'carbs': 2.1, 'protein': 4.95, 'fat': 7.97},
    11: {'name': 'telur', 'calories': 153, 'carbs': 0.60, 'protein': 10.62, 'fat': 12.02},
    12: {'name': 'tempe', 'calories': 193, 'carbs': 9.39, 'protein': 18.54, 'fat': 10.8}
}

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(img_path):
    # Check if the path is a URL or a local file
    if img_path.startswith(('http:', 'https:')):
        # If it's a URL, download the image
        response = urlopen(img_path)
        img = Image.open(BytesIO(response.read()))
    else:
        # If it's a local file, open it directly
        img = Image.open(img_path)

    # Resize the image to the target size
    img = img.resize((224, 224))

    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    return img_array


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image part in the request'})

        file = request.files['image']

        if file.filename == '':
            return jsonify({'error': 'No selected image file'})

        if file and allowed_file(file.filename):
            # Secure filename
            filename = secure_filename(file.filename)

            # Save the file to local directory
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Preprocess the image
            img = preprocess_image(file_path)

            # Delete the local file after processing
            os.remove(file_path)

            # Make predictions
            predictions = model.predict(img)
            predicted_index = np.argmax(predictions)
            predicted_label = class_info[predicted_index]
            confidence_score = np.max(predictions)

            result = {
                "Message": "Model predicted successfully",
                "Food Prediction": predicted_label['name'],
                "Calories": predicted_label['calories'],
                "Carbs": predicted_label['carbs'],
                "Protein": predicted_label['protein'],
                "Fat": predicted_label['fat'],
                "Confidence": float(confidence_score)
            }

            return jsonify(result), 200
        else:
            return jsonify({'error': 'Invalid file format. Supported formats: jpg, jpeg, png'})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
