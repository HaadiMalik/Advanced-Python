# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# print(weatherdata[0])

# TODO: What was the warmest day in the data set?
highest = min(weatherdata, key=lambda x: x['tmax'])
print(f"Warmest day was {highest}")

# TODO: What was the coldest day in the data set?
lowest = min(weatherdata, key=lambda x: x['tmin'])
print(f"Coldest day was {lowest}")

# TODO: How many days had snowfall?
for day in weatherdata:
    if day['snow'] > 0:
        print(f"{day['date']} had {day['snow']} inches of snow")
