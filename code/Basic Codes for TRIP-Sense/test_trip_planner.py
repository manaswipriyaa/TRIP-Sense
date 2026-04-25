from trip_planner import generate_trip_plan

goa_lat = 15.2993
goa_lon = 74.1240

plan = generate_trip_plan(goa_lat, goa_lon)

print("Weather:", plan["weather"])
print("Decision:", plan["decision"])
print("Final Plan:")
for place in plan["final_plan"]:
    print("-", place["name"]) 