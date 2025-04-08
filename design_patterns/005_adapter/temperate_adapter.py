"""
🌡️ Temperature Adapter Pattern Example

This script demonstrates the Adapter Design Pattern in Python using different temperature sensors.

👷 What It Does:
- Simulates sensors that report temperatures in different units (Fahrenheit, Kelvin).
- Uses adapter classes to convert all readings to a standard Celsius format.

📦 Classes:
- FahrenheitSensor: Returns temperature in °F
- KelvinSensor: Returns temperature in K
- CelsiusSensor: Native Celsius-based sensor
- FahrenheitToCelsiusAdapter: Converts °F to °C
- KelvinToCelsiusAdapter: Converts K to °C

🧠 Design Pattern:
Adapter Pattern — allows objects with incompatible interfaces to work together.

🚀 Example Output:
- Converts Fahrenheit (98.6°F) to Celsius
- Converts Kelvin (293K) to Celsius

✅ Use Case:
When integrating third-party systems (sensors, APIs, etc.) that return data in different formats, adapters provide a clean and scalable way to unify their outputs.
"""


class FahrenheitSensor:
    def get_temperature_f(self):
        return 98.6  # Example

class CelsiusSenor:
    def __init__(self, temp):
        self._temperature = temp

    def get_temperature_c(self):
        return self._temperature
    
class FahrenheitToCelsiusAdapter:
    def __init__(self, fahrenheit_sensor):
        self.fahrenheit_sensor = fahrenheit_sensor

    def get_temperature_c(self):
        f = self.fahrenheit_sensor.get_temperature_f()
        c = (f - 32) * 5 / 9
        return round(c, 2)  # Optional rounding


class KelvinSensor:
    def get_temperature_k(self): return 293

class KelvinToCelsiusAdapter:
    def __init__(self, kelvin_sensor):
        self.kelvin_sensor = kelvin_sensor

    def get_temperature_c(self):
        k = self.kelvin_sensor.get_temperature_k()
        c = k - 273
        return round(c, 2)  # Optional rounding


sensor_f = FahrenheitSensor()
f_adapter = FahrenheitToCelsiusAdapter(sensor_f)

print("Temperature in Celsius:", f_adapter.get_temperature_c(),f'({sensor_f.get_temperature_f()} F)')

sensor_k = KelvinSensor()
k_adapter =KelvinToCelsiusAdapter(sensor_k)
print("Temperature in Celsius:", k_adapter.get_temperature_c(),f'({sensor_k.get_temperature_k()} K)')

print()
f_adapter1 = FahrenheitToCelsiusAdapter(sensor_f)
print("Temperature in Celsius:", f_adapter1.get_temperature_c(),f'({sensor_f.get_temperature_f()} F)')
k_adapter1 =KelvinToCelsiusAdapter(sensor_k)
print("Temperature in Celsius:", k_adapter1.get_temperature_c(),f'({sensor_k.get_temperature_k()} K)')
