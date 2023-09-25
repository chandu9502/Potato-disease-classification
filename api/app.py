# from flask import Flask
# import cv2
# import matplotlib.pyplot as plt
# import pickle
# import h5py 
# from tensorflow import keras
# import tensorflow as tf
# import tensorflow as tf
# from tensorflow.keras import models, layers
# import matplotlib.pyplot as plt

# app = Flask(__name__)

# @app.route("/")
#  def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/pre")
# def evaluate():
#     return render_template('home.html')

# @app.route("/predict",methods = ["POST"])
# def predict():
#     img=request.files['file']
#     with h5py.File('potatoes.h5', 'r') as model_file:
#         model = keras.models.load_model(model_file)
#     prediction=predict(model,img)
#     print(prediction)

#     return render_template('home.html')
    



# def predict(model, img):
    
#     img_array = tf.keras.preprocessing.image.img_to_array(img.numpy())
#     img_array = tf.expand_dims(img_array, 0)

#     predictions = model.predict(img_array)

#     predicted_class = class_names[np.argmax(predictions[0])]
#     confidence = round(100 * (np.max(predictions[0])), 2)
#     return predicted_class, confidence

from flask import Flask, render_template, request
import h5py
import numpy as np
import tensorflow as tf
import cv2

app = Flask(__name__)

# Define class names if applicable (replace with your actual class names)
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]
MODEL = tf.keras.models.load_model("../saved_models/3")


@app.route("/pre")
def pre():
    return render_template('home.html')
@app.route("/predict", methods=["POST"])
def predict():
    # image = request.files['file']
    
    image=cv2.imread(r"/Users/satwikpuranam/mini_project/alternaria (24).JPG")
    image=cv2.resize(image,(256,256))
    #plt.imshow(image)
    # print("printted")
    img_batch = np.expand_dims(image, 0)
    MODEL = tf.keras.models.load_model("saved_models/3")
    predictions = MODEL.predict(img_batch)
    print(predictions)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    print(predicted_class)
    # with h5py.File('potatoes.h5', 'r') as model_file:
    #     model = tf.keras.models.load_model(model_file)
    # predicted_class, confidence = make_prediction(model, img)
    # print(f"Predicted Class: {predicted_class}, Confidence: {confidence}%")

    return render_template('home.js')

def make_prediction(model, img):
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * np.max(predictions[0]), 2)
    return predicted_class, confidence

if __name__ == "__main__":
    app.run()



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"