"""
A date is not a data type of its own in Python but we can import a
module named "datetime" to work with dates.
"""
# Displaying current date using datetime module
import datetime as dt
a = dt.datetime.now()
h = dt.datetime.today()  #This method is also valid
print(f"{a}")
print(f"{h}")

# Returning year and name of weekday
print(a.year)
print(a.strftime("%A"))  #Name of weekday using strftime() which takes one parameter "format".

# Creating a date object
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a default value of 0, (None for timezone).
x = dt.datetime(2023, 6, 15, 21, 35, 54)
print(x)

# Displaying the name of the month
print(a.strftime("%B"))
print(x.strftime("%B"))

# Displaying the timezone
b = dt.datetime.now(dt.timezone.utc)
print(b.strftime("%Z"))
# Creating Indian timezone
td = dt.timezone(dt.timedelta(hours=5, minutes=30))
tz = dt.datetime.now(td)
print(tz.strftime("%Z"))





