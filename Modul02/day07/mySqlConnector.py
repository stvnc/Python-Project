import mysql.connector
import numpy as np
import pandas as pd
from decimal import Decimal
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    host = 'localhost',
    port =  3306,
    user = 'root',
    passwd = 'vincent28',
    auth_plugin = 'mysql_native_password',
    database = 'world'
)
print(db)

c = db.cursor()
countryQuery = 'select country.continent as Benua, sum(country.Population) as Total from country group by country.continent'
c.execute(countryQuery)

newList = list(c.fetchall())
print(newList)
dataList = []
continentData = []
populationData = []

for i in newList:
    dataList.append(list(map(str, list(i))))

for i in range(len(dataList)):
    for j in range(i):
        if j == 1:
            populationData.append(int(dataList[i][j]))
        else:
            continentData.append(str(dataList[i][j]))

for i in populationData:
    print(i)

for i in continentData:
    print(i)

        
        
print(dataList)





# c = db.cursor()
# sql = 'insert into karyawan(nama, gaji) values (%s, %s)'
# val = ('Andi', 15000000)
# c.execute(sql, val)
# db.commit()
# # print(c.fetchall())
# print(c.rowcount, 'Data tersimpan')