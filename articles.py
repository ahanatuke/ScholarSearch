from math import floor


def articles():
    print("Please enter in keywords for articles using spaces only")
    uI = input("> ").lower().split()

    # mongoDB here
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
