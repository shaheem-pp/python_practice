import time, calendar, datetime

localtime = time.localtime(time.time())
year = localtime.tm_year
month = localtime.tm_mon
day = localtime.tm_mday
hour = localtime.tm_hour
minute = localtime.tm_min
second = localtime.tm_sec

if hour > 12:
    hour = hour - 12
    am_pm = "PM"
else:
    am_pm = "AM"

print("The current date and time is %d/%d/%d %d:%d:%d %s" % (day, month, year, hour, minute, second, am_pm))

cal = calendar.month(year, month)
print("")
print(cal)

leap = calendar.isleap(year)
if leap:
    print("This is a leap year")
else:
    print("This is not a leap year")
