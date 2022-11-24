import pymongo
from pymongo import MongoClient
import json
import itertools
import os

def init_db(jsonFile, portNum):
    # TODO remove hard codes before submission
    #portNum = 'mongodb://localhost:27017/'
    #jsonFile = 'db.json'
    connection = MongoClient(portNum)
    # connect to the server and will create a database named 291db
    # implemented in such a way that if it *is* in list_db_names, it just connects to that one, checks for dblp, if it exists, it drops it
    # I don't need to explain this all to you guys you're smart
    # dbNames = connection.list_database_names()

    # afai can tell, there's no real difference between handling for 291db existing vs handling for it *not* existing,
    # might be worth removing this, but also I am real loopy
    # if '291db' not in dbNames:  # TODO might not need this

    db = connection['291db']

    # If the collection exists, your program should drop it and create a new collection
    collectionsList = db.list_collection_names()  # Return a list of collections in '291db'

    if 'dblp' in collectionsList:
        col = db['dblp']
        col.drop()

    collection = db['dblp']




    #jsonFile = "./"+jsonFile #note program assumes .py files and file is in same directory, also ENTER EXTENSION
    importCmd = "mongoimport --db 291db --collection dblp --type=json --file " + jsonFile

    os.system(importCmd)

    collection.update_many(
        {"year":
             {"$type": 16}
         },
        [{"$set":
             {"year": {"$toString": "$year"} }
         }]
    )

    collection.create_index(
        [
            ("title", "text"),
            ("authors", "text"),
            ("abstract", "text"),
            ("venue", "text"),
            ("year", "text")
        ]

    )

    collection.aggregate([
        {"$match": {"_id": {"ne": ''} } },
        {"$lookup":  {"from": "dblp",
                      "localField": "id",
                      "foreignField": "references",
                      "as": "ref"}},
        {"$unwind": "$ref"},
        {"$group": {"_id": "$venue",
                    "venueIDRef": {"$addToSet": "$ref.id"}}},
        {"$project": {"_id": 1, "n_references": {"$size": "$venueIDRef"}}},
        {"$out": "venues"}

    ])
    return collection
