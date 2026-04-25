def weather_based_suggestion(weather):
    condition = weather["condition"]
    temperature = weather["temperature"]
    wind = weather["wind_speed"]

    if condition in ["Rain", "Thunderstorm"]:
        return "Recommend indoor activities (museums, cafes, shopping)"

    if temperature > 35:
        return "Avoid outdoor activities during afternoon; suggest indoor or evening plans"

    if wind > 8:
        return "Avoid ferry or boat activities"

    return "Outdoor activities recommended" 