import pymongo
from pymongo import MongoClient
import json
import itertools
import os

def init_db(jsonFile, portNum):
    #portNum = 'mongodb://localhost:27017/'
    #jsonFile = 'db.json'
    connection = MongoClient(portNum)

    db = connection['291db']

    collectionsList = db.list_collection_names()
    if 'dblp' in collectionsList:
        db.dblp.drop()

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
    collection.create_index([('references', 1)])
    collection.create_index([('venues', 1)])


    db.drop_collection('venues')
    collection.aggregate([
        {'$lookup': {"from": "dblp","localField": "id","foreignField": "references","as": "ref"}},
        {"$unwind": "$ref"},
        {"$group": {"_id": "$venue","venueIDRef": {"$addToSet": "$ref.id"}}},
        {"$match":{"_id": {"$ne": ''}}},
        {"$project": {"_id": 1, "n_references": {"$size": "$venueIDRef"}}},
        {"$out": "venues"}

    ])

    return collection, db
