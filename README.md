# Machine Learning Model Serving with Flask

This project demonstrates how to deploy a machine learning model locally using Flask. The model predicts food based on an input image.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- pip

## Setup

Clone the project repository:

```bash
git clone =https://github.com/BinaBola/Backend-ML.git
cd Backend-ML
```

Create Virtual Environment and activate the Virtual Environment:

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

Install dependencies:

```
pip install -r requirements.txt
```

## Notes

If you want to deploy to google cloud you can use bucket by changing the value of the variable bucket_name. But if you want to run locally, you can uncomment line code 12,39,40 and comment line code 8,41,42,43,44,45. Also in local you need to create folder .\static\uploads and .env in work directory. Lastly, you need to copy configuration in .env.example to .env and run back-end while trying this API. If, the PORT are the same, you can change this API PORT to 5000.

## Model

Before deploying the model, ensure you have a model file (model.h5)

## Running the Flask App Locally

Start the Flask app:

```
flask run
```

Open your web browser and go to http://localhost:8080 to check the health of the API.

## Usage

Use the /prediction endpoint to make predictions based on an input image.

```
curl -X POST -F "image=@path/to/your/image.jpg" http://localhost:8080/prediction
```

Replace path/to/your/image.jpg with the path to the image file you want to predict.

API Endpoints
Health Check
Path: /
Method: GET

Image Prediction
Path: /prediction
Method: POST
Payload: Form data with the image file.

Example Response

```
{
    "data": {
        "confidence": 0.9999995231628418,
        "exercise": {
            "data": {
                []
            }
        },
        "gym_equipment_prediction": "Dumbells"
    },
    "status": {
        "code": 200,
        "message": "Success Predicting"
    }
}
```
