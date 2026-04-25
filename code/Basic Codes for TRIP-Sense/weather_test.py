import requests

API_KEY = "a33e34339d132ff2d76e0e59de3203f5"

lat = 15.2993   # Goa latitude
lon = 74.1240   # Goa longitude

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

condition = data["weather"][0]["main"]
description = data["weather"][0]["description"]
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]

print("Condition:", condition)
print("Description:", description)
print("Temperature (°C):", temperature)
print("Humidity (%):", humidity)
print("Wind Speed (m/s):", wind_speed) 