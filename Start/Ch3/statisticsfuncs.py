# Example file for Advanced Python: Hands On by Joe Marini
# Using the statistics package

import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# select the days from the summer months from all the years
summers = ["-06-","-07-","-08-"]
summer_months = [d for d in weatherdata if any([month in d['date'] for month in summers])]
print(f"Data for {len(summer_months)} summer days")

max_temps = [d['tmax'] for d in summer_months]
min_temps = [d['tmin'] for d in summer_months]

# TODO: calculate the mean for both min and max temperatures
mean_min = statistics.mean(min_temps)
mean_max = statistics.mean(max_temps)

# TODO: calculate the median values for min and max temperatures
median_min = statistics.median(min_temps)
median_max = statistics.median(max_temps)

# TODO: use the standard deviation function to find outlier temperatures
upper_outlier = mean_max + (statistics.stdev(max_temps) * 2)
lower_outlier = mean_min - (statistics.stdev(min_temps) * 2)