import pymongo
dburl = 'mongodb://localhost:27017/'
mymongo = pymongo.MongoClient(dburl)

dbs = mymongo.list_database_names()
print(dbs)

dbName = 'pymongodb'
colName = 'colmong'
myDb =mymongo[dbName]
myCol = myDb[colName]

allDataQuery = list(myCol.find()) #Query untuk menampilkan keseluruhan data
ageQuery = list(myCol.find({'usia' : {'$gt': 20}})) #Query untuk menampilkan data dengan usia diatas 20

oneData = {'nama':'Deni', 'usia':18, 'kota':'Kediri'}

myData = [
    {'nama':'Deni', 'usia':18, 'kota':'Kediri'},
    {'nama':'Egin', 'usia':22, 'kota':'Jaka n rta'},
    {'nama':'Ferry', 'usia':22, 'kota':'Jakarta'}
]

# insertOneQuery = myCol.insert_one(oneData) #Untuk memasukkan satu data, apabila ingin memasukkan banyak menggunakan insert_many()
# inserManyQuery = myCol.insert_many(myData) #Untuk memasukkan banyak data
# removeOneQuery = myCol.delete_one({'name': 'Deni'}) #Menghapus Deni dari database
# removeManyQuery = myCol.delete_many({'name': 'Ferry'})

listNama = ['Audi', 'Egin', 'Ferry']
findNamaQuery = list(myCol.find({'nama': {'$in': listNama}}))
# sortQuery = list(myCol.find().sort('name'))

dataToUpdate = {'nama': 'Andi'}
newData = {'nama': 'Youngman'}

# myCol.update_one(dataToUpdate, {'$set':newData})

# print(allDataQuery)
# print(findNamaQuery)
# print(findNamaQuery)

data = {'$and': [
    {'usia' : {'$gt': 17}},
    {'usia' : {'$lt': 23}}
]}

import datetime
import pytz

# myCol.insert_one({
#     'nama':'Deni', 'waktu': datetime.datetime.utcnow()
# })



# myCol.update_many(data, {'$set': newData})
budiQuery = myCol.find({'nama':'Budi'}, {'waktu':1})
print(list(budiQuery)[0]['waktu'])

    