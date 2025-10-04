
---

# Potato Disease Classification

This project provides a **web-based application** to classify potato diseases using a deep learning model (TensorFlow/Keras). The user can upload an image of a potato leaf, and the model will predict whether the leaf is **Healthy**, has **Early Blight**, or **Late Blight**.

The backend of the app is built using **Flask** and serves a deep learning model that is loaded and used for predictions. This project also uses **TensorFlow** for the model and **Pillow** for image processing.

## Features

* **Image Upload**: Users can upload an image of a potato leaf.
* **Prediction**: The model predicts whether the leaf is healthy or affected by early or late blight.
* **Confidence**: The prediction is returned with a confidence score.

## Requirements

To run this project, you will need to have the following installed:

* **Python 3.x**
* **Flask**: For building the web application
* **TensorFlow**: For running the pre-trained model
* **Pillow**: For processing images
* **Flask-CORS**: For handling Cross-Origin Resource Sharing

You can install all required dependencies using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file can be generated with:

```bash
pip freeze > requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/chandu9502/Potato-disease-classification
cd potato-disease-classification
```

### 2. Install dependencies

Ensure you have a Python environment and install the dependencies:

```bash
pip install flask tensorflow pillow flask-cors
```

### 3. Place your model in the correct directory

Make sure that the pre-trained model file is placed inside the `saved_models/3` directory.

* **Model Path**: `../saved_models/3`

If you don't have the model, you need to train your own model and save it to that directory.

### 4. Run the Flask App

To start the application:

```bash
python main.py
```

The app will start running at `http://localhost:8000`. You can now test the model by sending `POST` requests with images of potato leaves.

## Usage

1. **Upload Image**: The user can upload a potato leaf image via a simple HTML form, or you can interact directly with the API by sending a `POST` request to the `/predict` endpoint with the image data.
2. **Prediction Response**: The server will return a prediction with the class (either "Early Blight", "Late Blight", or "Healthy") and the confidence score of the model.

### Sample Request

The Flask API expects a `POST` request to the `/predict` endpoint with a form-data body that includes the image. You can use tools like **Postman** or **curl** to send the request.

```bash
curl -X POST -F "file=@/path/to/your/image.jpg" http://localhost:8000/predict
```

### Sample Response

```json
{
  "class": "Early Blight",
  "confidence": 0.89
}
```

## Project Structure

```plaintext
potato-disease-classification/
│
├── app.py                  # Main Flask application
├── requirements.txt        # List of Python dependencies
├── saved_models/           # Directory containing pre-trained model
│   └── 3                   # The trained model directory
└── README.md               # Project documentation
```

### `app.py`

The main Flask application, which:

* Loads the pre-trained TensorFlow model.
* Provides a `/predict` route for image uploads.
* Processes the uploaded image and uses the model to predict the class.
* Returns the predicted class and confidence level.

---

## How the Model Works

1. **Model Loading**:
   The model is loaded using TensorFlow (`tf.keras.models.load_model`) from the directory `../saved_models/3`.

2. **Image Preprocessing**:
   The uploaded image is read using **Pillow**, resized to 256x256, and prepared for the model's input format (adding an extra batch dimension).

3. **Prediction**:
   The model predicts the class of the leaf (Healthy, Early Blight, Late Blight) and provides a confidence score, which is returned to the user.

## Troubleshooting

* **CORS Issues**: If you encounter Cross-Origin Resource Sharing (CORS) issues, ensure that you are accessing the server from the correct domain or set up the Flask app with CORS enabled.

* **Model Not Found**: If the app cannot find the model file, make sure it's saved in the correct directory (`../saved_models/3`).

* **Image Not Processed Correctly**: Ensure the image is in a supported format (JPEG, PNG, etc.) and is correctly resized before feeding it into the model.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
