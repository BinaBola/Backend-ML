# Installation and Usage of Flask Application

This application uses Flask as a web framework to create an image prediction API using a TensorFlow model. Several dependencies must be installed before running the application.

## Prerequisites
Make sure you have installed:

Python 3.9 or newer
pip (package installer for Python)
Virtual environment (optional but recommended)

## Installation Steps

1. Clone the Repository
Clone the repository from GitHub to your computer.

```bash
git clone https://github.com/BinaBola/Backend-ML.git
cd Backend-ML
```

2. Create and Activate a Virtual Environment

```
python -m venv .venv
```

- Windows:

```
.venv\Scripts\activate
```

- Linux & MacOS:

```
source .venv/bin/activate
```

3. Install Dependencies

```
pip install -r requirements.txt
```
4. Ensure Model and Data Availability
Make sure the model file (model.h5) is available in the project's root directory.

5. Run the Application
Run the Flask application using the following command:

```bash
python local.py
```

Open your browser and go to http://127.0.0.1:8080 to check the API.

## API Endpoints

Predict
This endpoint is used to upload an image and get a prediction.

URL: /predict
Method: POST
Content-Type: multipart/form-data
Form Data:
image: File gambar (jpg, jpeg, png)

## Usage

Use the /predict endpoint to make predictions based on the input image.

```
curl -X POST -F "image=@path/to/your/image.jpg" http://127.0.0.1:8080/predict
```

Replace path/to/your/image.jpg with the path to the image file you want to predict.

## Example Response

```
{
    "Message": "Model predicted successfully",
    "Food Prediction": "apel",
    "Calories": 52,
    "Carbs": 13.81,
    "Protein": 0.26,
    "Fat": 0.17,
    "Confidence": 0.95
}
```
