import pymongo
connection = pymongo.MongoClient('mongodb://localhost:27017/')
database = connection['mydb_01']
collection = database['mycol_01']
data = {'Name':"Kranti"}
collection.insert_one(data)

