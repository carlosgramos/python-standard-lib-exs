#Datetime module part 1
from datetime import datetime, timedelta
import calendar

#Create a datetime object
now = datetime.now()

#Return YYYY-MM-DD
print("Date: " + str(now.date()))

print("Year: " + str(now.year))
print("Month: " + str(now.month))
print("Day: " + str(now.day))
print("Hour: " + str(now.hour))
print("Minute: " + str(now.minute))
print("Second: " + str(now.second))

#Retrun HH:MM:SS.MS
print("Time: " + str(now.time()))

#Formatting date display with "Shift Time"
# %a -> Mon
# %A -> Monday
# %d -> 10
# %b -> Jan
# %B -> January
# %m -> 01

print(now.strftime("%a %A %d"))
print(now.strftime("%b %B %m"))

#Putting it all together
print(now.strftime("%a %B %d")) 

#Formatting time with "Shift Time"
# %H -> hours
# %M -> minutes
# %S -> seconds
# %p -> AM or PM

print(now.strftime("%H:%M:%S %p"))

#Formatting year
# %y - 17
# %Y - 2017
print(now.strftime("%y %Y"))

#Using the timedelta. NOTE: a datetime object is returned
testDate = now + timedelta(days=2)
firstCourseDate = now - timedelta(weeks=3)

print("Two days ago: " + str(testDate.date()))
print("Three weeks ago: " + str(firstCourseDate.date()))

#Comparing time
if testDate > firstCourseDate:
    print("Comparison works!")

#Working with Calendars
cal = calendar.month(2001, 10)
print(cal)

#Determine dates in the future. NOTE: counting begins on Mondays, not Sundays
cal2 = calendar.weekday(2001, 10, 11)
print(cal2)

#Determine leap year
print(calendar.isleap(1999))