# Example file for Advanced Python: Hands On by Joe Marini
# Working with date values

import json
import datetime

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


# TODO: The datetime module converts strings into dates fairly easily
converted_date = datetime.date.fromisoformat(weatherdata[0]['date'])
print(f"From {weatherdata[0]['date']} to {converted_date}")

# TODO: Date objects give us information such as day of week (0=Monday, 6=Sunday)
print(converted_date.weekday())

# TODO: what was the warmest weekend day in the dataset?
is_weekend_day = lambda day: datetime.date.fromisoformat(day['date']).weekday() in [5, 6]
weekends = list(filter(is_weekend_day, weatherdata))
warmest_day = max(weekends, key=lambda d: d['tmax'])

print(warmest_day)

# The timedelta object provides an easy way of performing date math
# find the coldest day of the year and get the average temp for the following week
coldest_day = min(weatherdata, key=lambda d: d['tmin'])
# convert the date to a Python date
coldest_date = datetime.date.fromisoformat(coldest_day['date'])
# print(f"The coldest day of the year was {str(coldest_date)} ({coldest_day['tmin']})")

# TODO: Look up the next 7 days
avg_temp = 0.0
next_date = coldest_date

for _ in range(7):
    next_date += datetime.timedelta(days=1)
    # find the weather object for that date in the list
    wd = next((day for day in weatherdata if day['date'] == str(next_date)), None)
    avg_temp += (wd['tmin'] + wd['tmax']) / 2

avg_temp = avg_temp / 7
print(f"The average temp for the next 7 days was {avg_temp}")