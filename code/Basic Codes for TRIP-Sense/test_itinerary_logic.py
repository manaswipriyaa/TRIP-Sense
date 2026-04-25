from weather_engine import get_weather
from itinerary_weather_logic import weather_based_suggestion

lat = 15.2993   # Goa
lon = 74.1240

weather = get_weather(lat, lon)
decision = weather_based_suggestion(weather)

print("Weather:", weather)
print("Suggestion:", decision) 