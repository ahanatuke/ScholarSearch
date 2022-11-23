from pymongo import MongoClient
import json


def init_db(jsonFile, portNum):
    portNum = 'mongodb://localhost:27017/'  # temp
    connection = MongoClient(portNum)
    # connect to the server and will create a database named 291db TODO (if it does not exist -- then what??)
    dbNames = connection.list_database_names()
    if '291db' not in dbNames:  # TODO might not need this
        db = connection['291db']

        # If the collection exists, your program should drop it and create a new collection
        collectionsList = db.list_collection_names()  # Return a list of collections in '291db'
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
        print('Database 291db already exists.\n Exiting program...')
        exit()
