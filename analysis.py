from flask import Flask, jsonify, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

DATA_FILE = 'sensor_data.csv'
model = LinearRegression()

# Load saved data or create empty DataFrame
if os.path.exists(DATA_FILE):
    sensor_data = pd.read_csv(DATA_FILE)
else:
    sensor_data = pd.DataFrame(columns=['Temperature', 'Humidity', 'MQ2', 'MQ5'])

# Train the model if there’s enough data
def train_model():
    if len(sensor_data) > 1:
        X = sensor_data[['Humidity', 'MQ2', 'MQ5']]
        y = sensor_data['Temperature']
        model.fit(X, y)

train_model()

@app.route('/api/sensor/readings', methods=['POST'])
def post_sensor_readings():
    global sensor_data

    new_data = request.json
    new_row = pd.DataFrame([new_data])

    # Append to in-memory DataFrame
    sensor_data = pd.concat([sensor_data, new_row], ignore_index=True)

    # Save to CSV
    sensor_data.to_csv(DATA_FILE, index=False)

    # Retrain model
    train_model()

    return jsonify({
        "message": "Sensor reading added and saved",
        "total_readings": len(sensor_data),
        "last_entry": new_data
    }), 201


@app.route('/api/predict', methods=['POST'])
def predict():
    input_data = request.json
    input_df = pd.DataFrame([input_data])

    if len(sensor_data) <= 1:
        return jsonify({"error": "Model needs at least 2 readings to train"}), 400

    prediction = model.predict(input_df[['Humidity', 'MQ2', 'MQ5']])

    return jsonify({
        "predicted_temperature": round(prediction[0], 2)
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7771, debug=True)
