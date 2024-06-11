import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
import tensorflow as tf
import keras
import numpy as np
from PIL import Image

from flask import Flask, request, jsonify

model = keras.models.load_model("model.h5")

class_names = {
    0: 'anggur',
    1: 'apel',
    2: 'ayam-goreng',
    3: 'ayam-kampung',
    4: 'daging',
    5: 'nasi',
    6: 'pasta',
    7: 'pisang',
    8: 'roti',
    9: 'sayur',
    10: 'tahu',
    11: 'telur',
    12: 'tempe'
}

def transform_image(pillow_image):
    # Mengubah gambar PIL menjadi array numpy dan normalisasi
    data = np.asarray(pillow_image)
    data = data / 255.0
    data = np.expand_dims(data, axis=-1)  # Tambahkan saluran warna jika tidak ada
    data = np.repeat(data, 3, axis=-1)    # Ubah gambar grayscale menjadi RGB
    data = tf.image.resize(data, [224, 224])  # Mengubah ukuran gambar
    data = np.expand_dims(data, axis=0)   # Tambahkan dimensi batch
    return data

def predict(x):
    predictions = model(x)
    predictions = tf.nn.softmax(predictions)
    pred0 = predictions[0]
    label0 = np.argmax(pred0)
    confidence_score = pred0[label0].numpy()
    class_name = class_names[int(label0)]
    return class_name, confidence_score

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
            class_name, confidence_score = predict(tensor)
            data = {
                "Message" : "Model is predicted successfully",
                "Food Prediction" : class_name,
                "Confidence": float(confidence_score)
            }
            return jsonify(data), 200
        except Exception as e:
            return jsonify({
                "status": {
                    "code": 400,
                    "message": e
                },
                "data": None
            }), 400

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
