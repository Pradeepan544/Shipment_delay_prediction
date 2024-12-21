# Shipment Delay Prediction

This project predicts the delay status of a shipment based on various features like origin, destination, vehicle type, weather conditions, traffic conditions, and shipment dates. The model is trained using logistic regression, and the application is deployed as a web service using Flask. Users can interact with the model through a simple web interface built using HTML, CSS, and JavaScript to submit their shipment data and get predictions.

## Features

- **EDA (Exploratory Data Analysis)**: Analyzing the dataset to understand data patterns and correlations.
- **Model Training**: A logistic regression model is trained on historical shipment data to predict delays.
- **Deployment**: The application is deployed using Flask for the backend, with a front-end interface for user interaction.
- **Prediction**: Users can enter details like origin, destination, vehicle type, distance, weather conditions, and shipment dates to get the prediction of whether the shipment will be delayed or not.

## Technologies Used

- **Python** (Flask)
- **JavaScript** (Fetch API for front-end)
- **HTML & CSS** (For designing the front-end)
- **Logistic Regression, Decision Tree, Random Forest** (Model training)
- **Pickle** (For saving and loading the trained model)
- **NumPy** (For feature manipulation)

## How to run the file after downloading or cloning
- You need to install the required Python libraries such as flask, sklearn, numpy, pickle. Download the pretrained model say for ex-logistics regression model(shipment_delay_modellr.pkl) and place it in the same directory as app.py
- Start the Flask development server by running the following command: python app.py, This will start the server at http://127.0.0.1:5000/
- Open a browser and go to http://127.0.0.1:5000/ to access the web interface. You can enter shipment details like: Origin, Destination, Vehicle Type, Distance, Weather Conditions, Traffic Conditions, Shipment Date, Planned Delivery Date, Actual Delivery Date.
- After submitting the form, you'll get a prediction of whether the shipment will be delayed or on time.

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-folder>
