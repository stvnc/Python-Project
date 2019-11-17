from datetime import datetime
from dateutil import tz
import requests

apiKey = "5e155ca16611b1d08678b090b42129c6"

continentDictionary = {
    1 : 'Asia',
    2 : 'Europe',
    3 : 'South America',
    4 : 'North America',
    5 : 'Africa',
    6 : 'Australia',
    7 : 'Antarctica'
}

print(continentDictionary)

continentInput = int(input('Pilih kontinen yang diinginkan: '))
continentValue = continentDictionary.get(continentInput)
userInput = input('Masukkan nama kota yang ingin dicek: ')

url = f"http://api.openweathermap.org/data/2.5/weather?q={userInput}&APPID={apiKey}"

data = requests.get(url)
weather = data.json()

sunrise = weather["sys"]["sunrise"]
sunset = weather["sys"]["sunset"]
temperature = weather["main"]["temp"]
print ('%0.2f' %(temperature - 273) ) #Karena suhunya dalam kelvin

myzone = tz.gettz(f"{continentValue}/{userInput}")
currentTime = datetime.utcfromtimestamp(int(sunrise))
print (currentTime)

