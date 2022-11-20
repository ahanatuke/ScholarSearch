from pymongo import MongoClient
import json


def init_db(jsonFile, portNum):
    portNum = 'mongodb://localhost:27017/'  # temp
    connection = MongoClient(portNum)
    # connect to the server and will create a database named 291db (if it does not exist -- then what??)
    dbNames = connection.list_database_names()
    if '291db' not in dbNames:
        db = connection['291db']

        # If the collection exists, your program should drop it and create a new collection
        list_of_collections = db.list_collection_names()  # Return a list of collections in '291db'
        if 'dblp' in list_of_collections:
            col = db['dblp']
            col.drop()

        collection = db['dblp']

        # TODO Process it as one-row-at-a time, and not to fully load the file into memory
        with open('file_name.json') as file:
            data = json.load(file)
        # print(data)
        collection.insert_many(data)

    else:
        print('Database 291db already exists.\n Exiting program...')
        exit()
