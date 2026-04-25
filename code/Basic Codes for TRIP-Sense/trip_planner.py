from weather_engine import get_weather
from itinerary_weather_logic import weather_based_suggestion

# Mock ML recommendation output (India-focused)
def get_ml_recommendations():
    return [
        {"name": "Baga Beach", "type": "outdoor"},
        {"name": "Fort Aguada", "type": "outdoor"},
        {"name": "Goa State Museum", "type": "indoor"},
        {"name": "Cafe Chocolatti", "type": "indoor"}
    ]


def generate_trip_plan(lat, lon):
    weather = get_weather(lat, lon)
    decision = weather_based_suggestion(weather)

    recommendations = get_ml_recommendations()

    if "indoor" in decision.lower():
        filtered = [p for p in recommendations if p["type"] == "indoor"]
    else:
        filtered = recommendations

    return {
        "weather": weather,
        "decision": decision,
        "final_plan": filtered
    } 