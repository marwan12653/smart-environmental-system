Smart Environmental Monitoring System


A real-time environmental monitoring system using an ESP32 microcontroller, designed to detect temperature, humidity, smoke, and flammable gases (LPG/Natural Gas) using affordable and widely available sensors. The system transmits sensor data to a Flask-based backend server for further processing, alerting, and logging.

Project Overview
This system addresses the need for affordable and scalable environmental safety monitoring in residential, educational, and industrial settings. It provides a compact, low-power solution capable of real-time data collection and wireless communication.

🔧 Hardware Components
ESP32 Dev Board

DHT22 Temperature and Humidity Sensor

MQ2 Smoke Sensor

MQ5 Gas Sensor (LPG/Natural Gas)

10kΩ Resistor (for DHT22 pull-up)

Breadboard & Jumper Wires

Power Supply (USB or battery)

Software Components
Arduino IDE with ESP32 Board Support

DHT Sensor Library

Flask (Python) for backend server

React.js (optional) for frontend visualization

System Workflow
Sensors read temperature, humidity, smoke, and gas data.

ESP32 collects and formats the readings.

ESP32 sends the data via HTTP POST to a local Flask server.

Flask server logs, processes, and stores the data (e.g., in JSON or database).

Alerts or visualizations can be triggered if thresholds are exceeded.

Circuit Diagram
All components are placed on a breadboard and wired to the ESP32 GPIO pins. A pull-up resistor is used with the DHT22 sensor to ensure signal reliability.
Refer to the project diagram for the exact pin configuration.

Sample Output
makefile
Copy
Edit
Temp: 27.3°C
Humidity: 45%
MQ2 (Smoke): 0
MQ5 (Gas): 1
The system updates readings every 2 seconds and sends them to the Flask backend automatically.

Future Improvements
Cloud integration (e.g., Firebase, AWS, or Thingspeak)

SMS or email alert system for gas/smoke detection

Real-time dashboard using charts and analytics

Integration with home automation systems
