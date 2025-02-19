import numpy as np
import pandas as pd
import time

# Constants
s = 0.000041  # Instrument factor
e = 0.99      # Emissivity of human skin
VVV = 5.0     # Reference voltage
R_fixed = 100 # Fixed resistor value in kilo-ohms

def read_sensor_values():
    """Simulate sensor readings (replace with actual sensor data in real use)."""
    sensor_thermistor = np.random.randint(200, 800)  # Simulated analog value
    sensor_thermopile = np.random.randint(100, 900)  # Simulated analog value
    return sensor_thermistor, sensor_thermopile

def calculate_temperatures(sensor_thermistor, sensor_thermopile):
    """Calculate temperatures from sensor values."""
    # Convert raw sensor values to voltage
    voltage_thermistor = sensor_thermistor * (VVV / 1023.0)
    voltage_thermopile = sensor_thermopile * (VVV / 1023.0)

    # Calculate thermistor resistance
    resistance = (voltage_thermistor * R_fixed) / (VVV - voltage_thermistor)

    # Calculate ambient temperature
    amb_temp = 98750 / (25 * np.log(resistance / R_fixed) + 3950)

    # Calculate object temperature using Stefan-Boltzmann equation
    obj_temp = np.power((voltage_thermopile / (s * e)) + np.power(amb_temp, 4), 0.25)

    return voltage_thermistor, resistance, amb_temp, voltage_thermopile, obj_temp

# Store data in a Pandas DataFrame
columns = ["Thermistor Voltage (V)", "Resistance (kΩ)", "Ambient Temp (°C)", 
           "Thermopile Voltage (V)", "Object Temp (°C)"]
df = pd.DataFrame(columns=columns)

# Run the simulation
for i in range(5):  # Simulating 5 readings
    sensor_thermistor, sensor_thermopile = read_sensor_values()
    results = calculate_temperatures(sensor_thermistor, sensor_thermopile)
    
    # Append data to DataFrame
    df.loc[i] = results

    # Print results
    print(df.iloc[i])
    print("=" * 50)
    time.sleep(2)  # Delay to mimic real sensor readings

# Save to CSV file
df.to_csv("thermometer_readings.csv", index=False)
