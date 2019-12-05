import mysql.connector
import csv

db = mysql.connector.connect(
    host = 'localhost',
    port =  3306,
    user = 'root',
    passwd = 'vincent28',
    auth_plugin = 'mysql_native_password',
    database = 'digimon'
)
c = db.cursor()
# c.execute('create database digimon')
# c.execute('create table digiData(no text, Digimon text, Stage text, Type text, Attribute text, Memory text, Equip_Slots text, HP text, SP text, Atk text, Def text, Intl text, Spd text)')
# c.execute('alter table digimon modify column no int')

with open('digimonDb.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    digi = (list(csv_reader))

data = []

for i in digi:
    data.append(tuple(i.values()))

sqlQuery = "insert into digiData (no, Digimon, Stage, Type, Attribute, Memory, Equip_Slots, HP, SP, Atk, Def, Intl, Spd) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
c.executemany(sqlQuery, data)

db.commit()