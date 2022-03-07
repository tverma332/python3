import pytz # importing pytz
import datetime

# 1) all_timezones = This function returns a list of all the time-zones supported by Python’s pytz module

print(pytz.all_timezones)

# 2) pytz.timezone() = returns the timezone object by the name. And, the datetime.now() returns the date-time of that particular time-zone


utc = pytz.timezone('US/Pacific')

print(datetime.datetime.now(utc))