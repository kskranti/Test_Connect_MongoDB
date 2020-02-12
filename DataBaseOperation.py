import pymongo
from bson import ObjectId
import statistics


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['mydatabase']
mycol = mydb['customers']
print("Database connected")

def insert_data(data):

    """
    insert new data or collection
    :param data:
    :return:
    """
    document = mycol.insert_one(data)

    return document.inserted_id


def update_or_create(document_id, data):
    """
    :param document_id:
    :param data:
    :return: 
    """
    document = mycol.update_one({'_id':ObjectId(document_id)}, {"$set":data}, upsert=True)
    return document.acknowledged

def get_single_data(document_id):
    """
    :param document_id:
    :return:
    """
    data = mycol.find_one({'_id': ObjectId(document_id)})
    return data

def get_multiple_data():
    """
    
    :return: 
    """

    data = mycol.find()
    return list(data)


myclient.close()


#data = {"name": "Srinivas Patoju", "address": "Visakhapatnam"}
#id = insert_data(data)
#print(id)

#update_or_create('5d91dee8c37790d73e01d6f0',data)

#X = get_single_data('5d91dee8c37790d73e01d6f0')
X = get_multiple_data()
print(X)

