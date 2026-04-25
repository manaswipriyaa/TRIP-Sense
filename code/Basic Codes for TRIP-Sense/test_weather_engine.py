from weather_engine import get_weather

goa_lat = 15.2993
goa_lon = 74.1240

weather = get_weather(goa_lat, goa_lon)
print(weather) 