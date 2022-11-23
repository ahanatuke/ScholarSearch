import pymongo
from pymongo import MongoClient
import json
import itertools
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
    if '291db' not in dbNames:  # TODO might not need this

        db = connection['291db']

        # If the collection exists, your program should drop it and create a new collection
        collectionsList = db.list_collection_names()  # Return a list of collections in '291db'

        if 'dblp' in collectionsList:
            col = db['dblp']
            col.drop()

        collection = db['dblp']

        #incase we cannot get mongoimport to load
        ''' 
        with open(jsonFile) as file:
            for item in file:
                part = json.load(item)
                collection.insert_one(part)
        
        ##OR##
        
        with open(jsonFile) as file:
            lenJson = len(file)    
            quarter = lenJson / 4
            start = 0
            end = quarter
            while end < lenJson
                fileData = json.load(itertools.islice(file.items(), start, end + 1 ))
                collection.insert_many(fileData)
                start = quarter
                end = quarter + quarter
        '''
        #jsonFile = "./"+jsonFile #note program assumes .py files and file is in same directory, also ENTER EXTENSION
        importCmd = "mongoimport --db 291db --collection dblp --file "+ jsonFile

        os.system(importCmd)
        collection.create_index("year" )
        return collection


        # with open(jsonFile) as file:
        #     data = json.load(file)
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
