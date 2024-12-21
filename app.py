from flask import Flask, request, jsonify, render_template
from datetime import datetime
import pickle
import numpy as np

# Load the trained model
with open("shipment_delay_modeldt.pkl", "rb") as file:
    model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    # Serve the template.html file when accessing the root route
    return render_template("template.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Convert dates to datetime
    shipment_date = datetime.strptime(data["shipmentDate"], "%Y-%m-%d")
    planned_date = datetime.strptime(data["plannedDate"], "%Y-%m-%d")
    actual_date = datetime.strptime(data["actualDate"], "%Y-%m-%d")

    # Calculate durations
    planned_duration = (planned_date - shipment_date).days
    print(planned_duration)
    delay_duration = (actual_date - planned_date).days
    print(delay_duration)

    # Encode categorical features
    origin_map = {"Ahmedabad": 0, "Bangalore": 1, "Chennai": 2, "Delhi": 3, "Hyderabad": 4,
                  "Jaipur": 5, "Kolkata": 6, "Lucknow": 7, "Mumbai": 8, "Pune": 9}
    vehicle_map = {"Truck": 3, "Lorry": 1, "Container": 0, "Trailer": 2}
    weather_map = {"Clear": 0, "Fog": 1, "Rain": 2, "Storm": 3}

    if data["trafficConditions"] == "Heavy":
        traffic_conditions_heavy = 1.0
        traffic_conditions_light = 0.0
        traffic_conditions_moderate = 0.0
    elif data["trafficConditions"] == "Light":
        traffic_conditions_heavy = 0.0
        traffic_conditions_light = 1.0
        traffic_conditions_moderate = 0.0
    elif data["trafficConditions"] == "Moderate":
        traffic_conditions_heavy = 0.0
        traffic_conditions_light = 0.0
        traffic_conditions_moderate = 1.0

    origin = origin_map[data["origin"]]
    destination = origin_map[data["destination"]]
    vehicle_type = vehicle_map[data["vehicleType"]]
    weather = weather_map[data["weather"]]

    # Create feature array
    features = np.array([
        origin, destination, vehicle_type, data["distance"],
        weather, traffic_conditions_light, traffic_conditions_moderate, traffic_conditions_heavy, planned_duration, delay_duration
    ]).reshape(1, -1)

    print(f"features: {features}")

    # Make prediction
    prediction = model.predict(features)[0]
    print(f"result: {prediction}")
    result = "Delayed" if prediction == 1 else "On Time"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)