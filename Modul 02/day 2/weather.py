from datetime import datetime
from dateutil import tz
import requests

apiKey = "5e155ca16611b1d08678b090b42129c6"

userInput = input('Masukkan nama kota yang ingin dicek: ')

url = f"http://api.openweathermap.org/data/2.5/weather?q={userInput}&APPID={apiKey}"

data = requests.get(url)
weather = data.json()

sunrise = weather["sys"]["sunrise"]
sunset = weather["sys"]["sunset"]
temperature = weather["main"]["temp"]
print ('%0.2f' %(temperature - 273) ) #Karena suhunya dalam kelvin

myzone = tz.gettz(f"Asia/{userInput}")
currentTime = datetime.utcfromtimestamp(int(sunrise))
print (currentTime)

