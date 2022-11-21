from math import floor


def searchArticles():
    print("Please enter in keywords for articles using spaces only")
    uI = input("> ").lower().split()

    # mongoDB here
    # TODO retrieve all articles that match all those keywords (AND semantics)
    '''A keyword matches if it appears in any of title, authors, abstract, venue and year fields (the matches should 
    be case-insensitive) '''

    # TODO For each matching article, display the id, the title, the year and the venue fields

    # TODO Select an article to see all fields including the abstract and the authors in addition to the fields shown before
    '''If the article is referenced by other articles, the id, the title, and the year of those references should be 
    also listed '''

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

    # TODO Add an article to the collection by providing a unique id, a title, a list of authors, and a year

    # TODO The fields abstract and venue should be set to null, references should be set to an empty array and
    #  n_citations should be set to zero

    return
