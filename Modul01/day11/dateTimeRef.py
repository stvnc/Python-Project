import platform as pt
import datetime as dt

# system = pt.system()
# print(system)

currentDate = dt.datetime.now()
day = currentDate.strftime("%A")
date = currentDate.strftime("%d")
month = currentDate.strftime("%B")
year = currentDate.strftime("%Y")
hour = currentDate.strftime("%H")
minute = currentDate.strftime("%M")
second = currentDate.strftime("%S")