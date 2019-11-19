import requests as rq
from bs4 import BeautifulSoup as bs
import json
import csv

url = rq.get('http://digidb.io/digimon-list/')
data = bs(url.content, 'html.parser')
count = 0
newList = []
digiList = []
digiNameList = []
digiImageList = []
digiAttributeList = []
digiTempList = []
templateList = []
count = 0

for i in data.find_all('th'):
    templateList.append(i.text)
    print(i.text)

for i in data.find_all('a'):
    newList.append(i.get('href'))

for i in data.find_all('img'):
    digiImageList.append(i.get('src'))

for i in newList:
    if 'http://digidb.io/digimon-search/?request=' in str(i):
        digiList.append(i)

for i in data.find_all('center'):
    if count % 11 == 0 and count != 0:
        print(digiTempList)
        digiAttributeList.append(digiTempList)
        digiTempList = []
        digiTempList.append(i.text)
        count += 1
    else:
        digiTempList.append(i.text)
        count += 1

for i in digiList:
    try: 
        digiUrl = rq.get(i)
        digiData = bs(digiUrl.content, 'html.parser')
        digiName = digiData.find_all('title')
        tempList = []
        for i in digiName:
            tempList = i.text.split()
            digiNameList.append(str(tempList[0]))
    except ValueError:
        break

digimon = dict(zip(count, digiNameList, digiImageList, digiAttributeList))

with open('digimonDb.json', 'w') as outfile:
    json.dump(digimon, outfile)

with open("digimonDb.csv", "w", newline="") as outfile:
    csvFile = csv.DictWriter(outfile, fieldnames = templateList, delimiter =",")
    csvFile.writeheader()
    csvFile.writerows(digimon)

# for i in digimon:
#     print(i)


    
