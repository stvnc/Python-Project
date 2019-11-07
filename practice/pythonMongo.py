import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["customers"]

mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.find_one()

print(x)

