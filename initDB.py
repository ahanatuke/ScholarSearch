import pymongo
from pymongo import MongoClient
import json
import os

def init_db(jsonFile, portNum):
    portNum = 'mongodb://localhost:27017/'  # temp todo remove this before submit
    # todo fix before submission
    jsonFile = 'db.json'
    connection = MongoClient(portNum)
    # connect to the server and will create a database named 291db
    # implemented in such a way that if it *is* in list_db_names, it just connects to that one, checks for dblp, if it exists, it drops it
    # i don't need to explain this all to you guys you're smart
    dbNames = connection.list_database_names()
    # afai can tell, there's no real difference between handling for 291db existing vs handling for it *not* existing,
    # might be worth removing this but also i am real loopy
    if '291db' not in dbNames:
        db = connection['291db']

        # If the collection exists, your program should drop it and create a new collection
        collectionsList = db.list_collection_names()  # Return a list of collections in '291db'

        if 'dblp' in collectionsList:
            col = db['dblp']
            col.drop()

        collection = db['dblp']

        #jsonFile = "./"+jsonFile #note program assumes .py files and file is in same directory, also ENTER EXTENSION
        importCmd = "mongoimport --db 291db --collection dblp --file "+ jsonFile

        os.system(importCmd)
        collection.create_index("year" )

        return collection
        # with open(jsonFile) as file:
        #     data = json.load(file)
        # print(data)
        # collection.insert_many(data)

    else:
        db = connection['291db']
        collectionsList = db.list_collection_names()

        if 'dblp' in collectionsList:
            col = db['dblp']
            col.drop()

        collection = db['dblp']
        importCmd = "mongoimport --db 291db --collection dblp --file " + jsonFile

        os.system(importCmd)
        collection.create_index("year" )
