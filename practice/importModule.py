import platform as pt
import datetime as dt

system = pt.system()
print(system)

currentDate = dt.datetime.now()
day = currentDate.strftime("%A")
date = currentDate.strftime("%d")
month = currentDate.strftime("%B")
year = currentDate.strftime("%Y")
hour = currentDate.strftime("%H")
minute = currentDate.strftime("%M")
second = currentDate.strftime("%S")

print(currentDate.strftime("%A")) #String format time -> hari
print(currentDate.strftime("%B")) #bulan
print(currentDate.strftime("%Y")) # tahun
print(currentDate.strftime("%c")) # keseluruhan
print(currentDate.strftime("%H")) # 24 jam
print(currentDate.strftime("%I")) # 12 jam
print(currentDate.strftime("%p")) # am/pm
print(currentDate.strftime("%M")) # menit

