# Example file for Advanced Python: Hands On by Joe Marini
# Load and parse a JSON data file and determine some information about it

import json
import pprint

# TODO: open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


# TODO: make sure the data loaded correctly by printing the length of the dataset
# print(len(weatherdata))

# TODO: let's also take a look at the first item in the data
# print(weatherdata[0])

# TODO: How many days of data do we have for each year?
years = {}

for date in weatherdata:
    if date["date"][0:4] in years:
        years[date["date"][0:4]] += 1
    else:
        years[date["date"][0:4]] = 1


pprint.pp(years)