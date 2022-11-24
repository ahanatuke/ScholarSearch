import pymongo
from pymongo import MongoClient
import json
import itertools
import os

def listVenues(collection, db):
    print("Enter the amount of top venues you would like to see\nHit ENTER to go back to the mainpage\nHit E to exit the program")
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
                  "\nHit ENTER to go back to the mainpage\nHit E to exit the program")
            uI = input("> ")

    # TODO The user should be able to enter a number n and see a listing of top n venues
    a = db['venues']
    result = a.aggregate([
     {"$sort": {"n_references": -1}},
     {"$limit": intuI},
    ])
    result = list(result)
    print(result)
    for item in result:
        print(item)
    return




