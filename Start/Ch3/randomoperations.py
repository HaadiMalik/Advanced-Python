# Example file for Advanced Python: Hands On by Joe Marini

import json
import random
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# get the first 30 days in the dataset
month_data = weatherdata[0:30]

# TODO: the shuffle() function will randomly shuffle a list in-place
random.shuffle(month_data)

# TODO: use choice() and choices() to get random items, but beware that
# these functions can produce duplicate results
random_choice = random.choice(month_data)
random_choices = random.choices(month_data, k=3)

# TODO: the sample() function will choose random items with no duplicates
random_sample = random.sample(month_data, k=3)