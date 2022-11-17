from pymongo import MongoClient
import json
from math import floor


def init_db():
    client = MongoClient("mongodb://localhost:27017/")  # TODO do we need to connect to lab machine
    db = client["291_proj2"]  # TODO do we need to take input for the name?

    collection = db['data']
    with open('file_name.json') as file:
        data = json.load(file)
    # print(clothes_data)
    collection.insert_many(data)


def articles():
    print("Please enter in keywords for articles using spaces only")
    uI = input("> ").lower().split()

    # mongoDB here
    return


def authors():
    print("Please enter in keywords to search for authors using spaces only ")
    uI = input("> ").lower().split()

    # mongoDB here
    return


def venues():
    print("Enter the amount of top venues you would like to see")
    uI = input("> ")
    check = True
    while check:
        try:
            uI = int(uI)
            check = True
        except:
            print("The input is not a number, please try again"
                  "Enter the amount of top venues you would like to see")
            uI = input("> ")
    # DB here
    return


def addArticle():
    abstract = None
    venue = None
    references = []
    n_citations = 0
    check = True


    id = input("Add an id\n> ").lower().strip()
    title = input("Add a title\n>").lower().strip()
    authors = input("Add the list of authors using spaces only\n>").lower().split()
    year = input("Add the year for the article\n>").lower().strip()

    while check:
        if len(authors) < 1:
            print("Please include at least one author.")
            input("Add the list of authors using spaces only\n>").lower().split()
        check = False
    while check:
        try:
            yearInt = int(year)
        except:
            print("The year added is not a valid year, please try again.")
            year = input("Add the year for the article\n>").lower().strip()
        check = False

    return


def main():
    print("To search for an article enter 'A'"
          "To search for an author enter 'U'"
          "To list venues within a range enter 'V' "
          "To add an article enter 'R'"
          "To quit enter 'Q'")
    done = False
    while done == False:
        uI = input("> ").lower().strip()
        if uI == 'a':
            pass
        elif uI == 'u':
            pass
        elif uI == 'v':
            pass
        elif uI == 'r':
            pass
        elif uI == 'q':
            print("Exiting program...")
            print("Goodbye")
            done = True
        else:
            print("Invalid input, try again.")
            uI = input("> ").lower().strip()

    return


main()
