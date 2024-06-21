# BinaBola - ENTS-H113
## Table of Contents

1. [Team ENTS-H113 - CC](#Team-ENTS-H113---CC)
2. [What is BinaBola?](#BinaBola)
3. [Technology](#Technology)
4. [Installation](#Installation)
5. [Database Configuration](#Database-Configuration)
6. [Running the Project](#Running-the-Project)
7. [API Endpoints](#API-Endpoints)


## Team ENTS-H1137 - CC

| Bangkit ID | Name | Learning Path | University |LinkedIn |
| ---      | ---       | ---       | ---       | ---       |
| C117D4KY0805 | Farhan Al Farisi | Cloud Computing | 	Institut Teknologi Nasional Bandung | [![text](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/farhan-al-farisi-744499196/) |
| C117D4KY0310 | Qays Arkan Chairy |  Cloud Computing | Institut Teknologi Nasional Bandung | [![text](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/qaysarkan/) |

## BinaBola

this application has the potential to make a real difference in the lives of Indonesian football players. This application will be a valuable tool for young football talents. It can help them improve their health, physicality, prevent injuries, and reach their full potential. We are committed to making this application affordable and accessible to all young Indonesian football players.

## Technology
The Binabola project is built using the following technologies:

# Installation and Usage of Flask Application

This application uses Flask as a web framework to create an image prediction API using a TensorFlow model. Several dependencies must be installed before running the application.

## Requirement
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
