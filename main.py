from pymongo import MongoClient
import json

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

    InId = input("Add an id\n> ")
    tId = input("Add a title\n>")

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
