from pymongo import MongoClient
import json


def init_db():
    client = MongoClient("mongodb://localhost:27017/")  # TODO do we need to connect to lab machine
    db = client["291_proj2"]  # TODO do we need to take input for the name?

    collection = db['data']
    with open('file_name.json') as file:  # TODO make for loop to change file names
        data = json.load(file)
    # print(data)
    collection.insert_many(data)
