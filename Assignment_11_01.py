import pandas as pd
import datetime

# a) Date time object for Jan 15 2012
dt_jan_15_2012 = pd.to_datetime('2012-01-15')
print("a) Date time object for Jan 15 2012:", dt_jan_15_2012)

# b) Specific date and time of 9:20 pm
dt_specific_time = pd.to_datetime('2012-01-15 21:20')
print("b) Specific date and time of 9:20 pm:", dt_specific_time)

# c) Local date and time
local_dt = pd.to_datetime(datetime.datetime.now())
print("c) Local date and time:", local_dt)

# d) A date without time
date_only = pd.to_datetime('2023-08-25').date()
print("d) A date without time:", date_only)

# e) Current date
current_date = pd.to_datetime('today').date()
print("e) Current date:", current_date)

# t) Time from a date time
dt = pd.to_datetime('2025-04-14 16:45:30')
time_only = dt.time()
print("t) Time from a date time:", time_only)

# g) Current local time
current_local_time = datetime.datetime.now().time()
print("g) Current local time:", current_local_time)
