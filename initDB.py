from pymongo import MongoClient
import json


def init_db(jsonFile, portNum):
    portNum = 'mongodb://localhost:27017/'  # temp todo remove this before submit
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
        # this will never work afaiu, as if 291db doesn't exist as a db, it can't have the collection dblp
        # todo add an elif statement that covers the other case
        if 'dblp' in collectionsList:
            col = db['dblp']
            col.drop()

        collection = db['dblp']

        # TODO connect mongoimport to the MongoDB instance
        """
        mongoimport - -uri
        'mongodb+srv://mycluster-ABCDE.azure.mongodb.net/test?retryWrites=true&w=majority'
        --username = 'MYUSERNAME'
        --password = 'SECRETPASSWORD'
        """

        # TODO Process it as one-row-at-a time, and not to fully load the file into memory
        """
        mongoimport -db '291db' -collection 'dblp' --type=json --file jsonFile
        
        mongoimport --db 291db -- collection dblp --type=json --batchSize 1  --file jsonFile 
        TAKEN FROM: https://dev.to/miladr0/import-large-json-file-into-mongodb-using-mongoimport-34ai

        """
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
        #todo populate db
