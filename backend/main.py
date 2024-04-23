import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
#from flask.ext.session import Session
app = Flask(__name__)
cors = CORS(app)

MODEL = tf.keras.models.load_model("../saved_models/3")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return {
                "res": "No data"
            }
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.s
        image = read_file_as_image(file.read())
        image.resize(256, 256, 3)
        img_batch = np.expand_dims(image, 0)
        print(image)
        predictions = MODEL.predict(img_batch)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        return {
            'class': predicted_class,
            'confidence': float(confidence)
        }

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    app.run(debug=True,host="localhost",port= 8000,use_reloader=False)
