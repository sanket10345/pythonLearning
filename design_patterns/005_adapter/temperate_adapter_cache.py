"""
🌡️ Temperature Adapter Pattern with Caching in Python

This script demonstrates how the Adapter Design Pattern can be combined with caching 
to efficiently work with temperature sensors that return data in different units.

📌 What It Does:
- Simulates three different types of sensors: Fahrenheit, Kelvin, and native Celsius.
- Uses Adapter classes to convert Fahrenheit and Kelvin to Celsius.
- Implements caching inside the adapters to avoid repeated conversions for the same input.

🧱 Classes Overview:
- FahrenheitSensor: Simulates a temperature reading in Fahrenheit (°F).
- KelvinSensor: Simulates a temperature reading in Kelvin (K).
- CelsiusSensor: Directly provides Celsius readings (not used in conversion here, but useful for context).
- FahrenheitToCelsiusAdapter: Converts °F to °C with a cache to avoid recalculating the same value.
- KelvinToCelsiusAdapter: Converts K to °C with similar caching logic.

🧠 Design Pattern Used:
- Adapter Pattern: Allows integrating third-party systems (sensors) with incompatible interfaces 
  by wrapping them in a unified interface (`get_temperature_c()`).
- Caching: Ensures that if the same temperature value is received again, conversion logic is skipped,
  improving performance and simulating a realistic optimization.

🎯 Example Behavior:
- Converts 98.6°F to Celsius once, then returns the cached value on the next call.
- Converts 293K to Celsius once, then returns the cached value on reuse.
- Demonstrates caching in action with print statements like "Returning Cached Value..."

✅ Why This is Useful:
In real-world applications like IoT, hardware interfacing, or API integrations,
you often receive data in various formats. Adapter + Caching allows you to:
- Standardize how data is accessed
- Avoid redundant computation or API calls
- Improve performance and scalability
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
    _cache = {}
    def __init__(self, fahrenheit_sensor):
        self.fahrenheit_sensor = fahrenheit_sensor

    def get_temperature_c(self):
        f = self.fahrenheit_sensor.get_temperature_f()
        if f'{f}' in self._cache:
            print('Returning Cached Value...')
            return self._cache[f'{f}']
        c = (f - 32) * 5 / 9
        self._cache[f'{f}'] = round(c, 2)
        return round(c, 2)  # Optional rounding


class KelvinSensor:
    def get_temperature_k(self): return 293

class KelvinToCelsiusAdapter:
    _cache = {}
    def __init__(self, kelvin_sensor):
        self.kelvin_sensor = kelvin_sensor

    def get_temperature_c(self):
        k = self.kelvin_sensor.get_temperature_k()
        if f'{k}' in self._cache:
            print('Returning Cached Value...')
            return self._cache[f'{k}']
        c = k - 273
        self._cache[f'{k}'] = round(c, 2)
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
