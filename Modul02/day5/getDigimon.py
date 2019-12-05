import requests as rq
from bs4 import BeautifulSoup as bs
import json

url = rq.get('http://digidb.io/digimon-list/')
data = bs(url.content, 'html.parser')
count = 0
digiNameList = []
digiImageList = []
digiAttributeList = []
digiTempList = []
templateList = []
count = 0
numList = []
digimon = []
fullList = []

for i in data.find_all('th'):
    templateList.append(i.text)

for i in data.find_all('a', style='font-weight: bold;'):
    digiNameList.append(i.text)\

for i in data.find_all('img'):
    digiImageList.append(i.get('src'))

for i in data.find_all('center'):
    if count % 11 == 0 and count != 0:
        digiAttributeList.append(digiTempList)
        digiTempList = []
        digiTempList.append(i.text)
        count += 1
    else:
        digiTempList.append(i.text)
        count += 1

for i in range(1, int(count/11)+1):
    numList.append(i)

for i in range(len(digiNameList)):
    tempList = []
    tempList.append(int(i)+1)
    tempList.append(digiNameList[i])
    for j in range(11):
        tempList.append(digiAttributeList[i][j])
    print(tempList)
    digimon.append(tempList)

for i in range(len(digimon)):
    temp = dict(zip(templateList, digimon[i]))
    fullList.append(temp)

with open('digimonDb.json', 'w') as outfile:
    json.dump(fullList, outfile)

import csv
with open("digimonDb.csv", "w", newline="") as x:
    csvFile = csv.DictWriter(x, fieldnames = templateList)
    csvFile.writeheader()
    csvFile.writerows(fullList)


    
