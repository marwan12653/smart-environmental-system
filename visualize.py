import pandas as pd
import matplotlib.pyplot as plt

csv_file = 'sensor_data.csv'

try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Error: File '{csv_file}' not found.")
    exit()

# Add timestamp if not present
if 'timestamp' not in df.columns:
    df['timestamp'] = pd.date_range(start='2025-01-01', periods=len(df), freq='2S')

df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Temperature'], label='Temperature (°C)', color='red')
plt.plot(df.index, df['Humidity'], label='Humidity (%)', color='blue')
plt.plot(df.index, df['MQ2'], label='MQ2 (Smoke)', color='green')
plt.plot(df.index, df['MQ5'], label='MQ5 (Gas)', color='orange')

plt.title('Environmental Sensor Data Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Sensor Readings')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
