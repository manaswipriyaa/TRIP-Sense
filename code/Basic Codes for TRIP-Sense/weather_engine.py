import requests

API_KEY = "a33e34339d132ff2d76e0e59de3203f5"

def get_weather(lat, lon):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    weather_info = {
        "condition": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

    return weather_info 