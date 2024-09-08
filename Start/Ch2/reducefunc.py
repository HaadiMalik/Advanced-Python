# Example file for Advanced Python: Hands On by Joe Marini
# Using the reduce function

import json
from functools import reduce

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: how much snowfall is in the entire dataset?
total_snowfall = reduce(lambda x,y: x + y, [day['snow'] for day in weatherdata])
print(f"Total Snowfall: {total_snowfall}")

# TODO: how much total precipitation is in the entire dataset?
total_precip = reduce(lambda x,y: x + y, [day['prcp'] + day['snow'] for day in weatherdata])
print(f"Total Precip: {total_precip}")

# TODO: What was the warmest day in which it snowed? Need to find highest 'tmax' for all
# days where 'snow' > 0
def warm_snow_day(acc, elem):
    # return the elem value if the snow amount > 0 and its tmax value is
    # larger than the tmax value that is in the acc argument
    if acc is None:
        return elem
    
    return elem if elem['snow'] > 0 and elem['tmax'] > acc['tmax'] else acc

# define a "zero" value start date for the reduce function to start with
start_val = {
    "date": "1900-01-01",
    "tmin": 0,
    "tmax": 0,
    "prcp": 0.0,
    "snow": 0.0,
    "snwd": 0.0,
    "awnd": 0.0
}

# TODO: reduce the data set to the warmest snow day
warmest_snow_day = reduce(warm_snow_day, weatherdata, start_val)
print(warmest_snow_day)
