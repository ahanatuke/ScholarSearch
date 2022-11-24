import pymongo
from pymongo import MongoClient
import json
import itertools
import os


def listVenues(collection, db):

    print(
        "Enter the amount of top venues you would like to see\nHit ENTER to go back to the mainpage\nHit E to exit the program")

    uI = input("> ")
    check = True
    while check:
        try:
            if uI == '':
                return
            elif uI.lower() == 'e':
                print("Exiting program...\nGoodbye.")
                exit()
            intuI = int(uI)
            check = False
        except:
            print("The input is not a number, please try again\nEnter the amount of top venues you would like to see"
                  "\nHit ENTER to go back to the main page\nHit E to exit the program")
            uI = input("> ")

    a = db['venues']

    result = a.aggregate([
        {"$sort": {"n_references": -1}},
        {"$limit": intuI},
    ])
    result = list(result)

    #
    # i = 0


    # for item in result:
    #     r = collection.aggregate([
    #         {"$venues": item["_id"]},
    #     ])
    #     r = list(r)
    #     print(item, r)
    #     i += 1
    #     print(item)

    all_top_venues = list(collection.aggregate([{
        "$group": {
            "_id": "$venue",
            "count": {"$sum": 1},
        }
    }, {"$sort": {"count": -1}, }]))

    print(f"row | venue | count | n_ref")
    for i in range(1, int(uI)+1):
        itm = all_top_venues[i]
        for r in result:
            if r['_id'] == itm['_id']:
                n_ref = itm['n_references']
                break
        else: # no break
            n_ref = 0
        print(f"{i} | {itm['_id']} | {itm['count']} | {n_ref}")
