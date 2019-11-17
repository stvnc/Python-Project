import requests
import json
import xlsxwriter
import csv

url = "https://jsonplaceholder.typicode.com/users"
data = requests.get(url)
# print(data.json())
# for i in data.json():
#     print(i['name'], 'di Jl.', i['address']['street'])


userInput = str(input('Masukkan nama team yang ingin dicari: '))
baseUrl = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={userInput}'

data = requests.get(baseUrl)
playerData = data.json()['player']
header = ["Name", "Position", "Age", "Country"]
name = []
position = []
age = []
country = []
combination = []
playerList = []

for i in playerData:
    name.append(i['strPlayer'])
    position.append(i['strPosition'])
    age.append(2019 - int(i["dateBorn"][:4]))
    country.append(i['strNationality'])
combination = list(zip(name, position, age, country))

for i in range(len(combination)):
    curDict = dict(zip(header, combination[i]))
    playerList.append(curDict)

#create csv
with open(f'{userInput}.csv', "w", newline = "") as x:
    column = header
    a = csv.DictWriter(x, fieldnames = column, delimiter = ",")
    a.writeheader()
    a.writerows(playerList)

#create json
with open (f'{userInput}.json', "w") as y:
    json.dump(playerList,y)

#create excel
newfile = xlsxwriter.Workbook(f"{userInput}.xlsx")
newsheet = newfile.add_worksheet("Player Data")
for i in range(len(header)):
    newsheet.write(0, i, header[i])
for i in range(len(combination)):
    for j in range(len(header)):
        newsheet.write(i+1, j, combination[i][j])
newfile.close()




