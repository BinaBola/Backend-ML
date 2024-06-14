import os

from dotenv import load_dotenv

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
import tensorflow as tf
import keras
import numpy as np
from PIL import Image

from flask import Flask, request, jsonify


load_dotenv()

model = keras.models.load_model("model.h5")

class_data = {
    0: {'name': 'anggur', 'calories': 69, 'carbs': 18.1, 'crotein' : 0.72, 'fat' : 0.16},
    1: {'name': 'apel', 'calories': 52, 'carbs': 13.81, 'protein' : 0.26, 'fat' : 0.17},
    2: {'name': 'ayam-goreng', 'calories': 295, 'carbs': 10.76, 'protein' : 37, 'fat' : 14.7},
    3: {'name': 'ayam-kampung', 'calories': 246, 'carbs': 10.76, 'protein' : 37.9, 'fat' : 9},
    4: {'name': 'daging', 'calories': 288, 'carbs': 0, 'protein' : 26.33, 'fat' : 19.54},
    5: {'name': 'nasi', 'calories': 180, 'carbs': 39.8, 'protein' : 3, 'fat' : 0.3},
    6: {'name': 'pasta', 'calories': 157, 'carbs': 30.68, 'protein' : 5.76, 'fat' : 0.92},
    7: {'name': 'pisang', 'calories': 89, 'carbs': 22.48, 'protein' : 1.09, 'fat' : 0.33},
    8: {'name': 'roti', 'calories': 264, 'carbs': 55.81, 'protein' : 9.61, 'fat' : 1.3},
    9: {'name': 'sayur', 'calories': 60, 'carbs': 13.09, 'protein' : 2.86, 'fat' : 0.15},
    10: {'name': 'tahu', 'calories': 78, 'carbs': 2.1, 'protein' : 4.95, 'fat' : 7.97},
    11: {'name': 'telur', 'calories': 153, 'carbs': 0.60, 'protein' : 10.62, 'fat' : 12.02},
    12: {'name': 'tempe', 'calories': 193, 'carbs': 9.39, 'protein' : 18.54, 'fat' : 10.8}
}

def transform_image(pillow_image):
    data = np.asarray(pillow_image)
    data = data / 255.0
    data = np.expand_dims(data, axis=-1)
    data = np.repeat(data, 3, axis=-1)
    data = tf.image.resize(data, [224, 224])
    data = np.expand_dims(data, axis=0)
    return data

def predict(x):
    predictions = model(x)
    predictions = tf.nn.softmax(predictions)
    pred0 = predictions[0]
    label0 = np.argmax(pred0)
    confidence_score = pred0[label0].numpy()
    class_info = class_data[int(label0)]
    return class_info, confidence_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})

        try:
            image_bytes = file.read()
            pillow_img = Image.open(io.BytesIO(image_bytes)).convert('L')
            tensor = transform_image(pillow_img)
            class_info, confidence_score = predict(tensor)
            data = {
                "Message" : "Model is predicted successfully",
                "Food Prediction" : class_info['name'],
                "Calories": class_info['calories'],
                "Carbs": class_info['carbs'],
                "Protein": class_info['protein'],
                "Fat": class_info['fat'],
                "Confidence": float(confidence_score)
            }
            return jsonify(data), 200
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), 400

    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

