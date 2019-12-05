import xlrd
import json
import csv

file = xlrd.open_workbook('contohFile.xlsx')
sheet = file.sheet_by_index(0)
print(sheet.nrows, sheet.ncols)

templateList = []
dataList = []
newDict = {}

for i in range(sheet.ncols):
    templateList.append(sheet.cell_value(0, i))
print(templateList)

for i in range(1, sheet.nrows):
    newList = []
    for j in range(sheet.ncols):
        newList.append(sheet.cell_value(i,j))
        print(sheet.cell_value(i,j))
    newDict = dict(zip(templateList, newList))
    dataList.append(newDict)
print(dataList)

with open('file.json', 'w') as outfile:
    json.dump(dataList, outfile)

with open("file.csv", "w", newline="") as x:
    csvFile = csv.DictWriter(x, fieldnames = templateList, delimiter =",")
    csvFile.writeheader()
    csvFile.writerows(dataList)



