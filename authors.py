import venues


def searchAuthors(collection):
    # TODO Provide a keyword and see all authors whose names contain the keyword (the matches should be case-insensitive)
    print("Please enter in keywords to search for authors using spaces only ")
    uI = input("> ").lower().split()

    # mongoDB here

    # TODO For each author, list the author name and the number of publications
    results = collection.find({"name": '/' + uI + '/'})
    '''CONCEPT: 
    For every author in results: 
    SELECT a.name, SUM(*)
    FROM article as a1, article as a2
    WHERE a1.name = a2.name and a1.id != a2.id '''

    print("Please select from 0 - ", len(results) - 1, "and select an author to look for")
    uI = input("> ")
    check = True
    while check:
        try:
            intuI = int(uI)
            if intuI < 0:
                raise Exception
            if intuI >= len(results):
                raise Exception
            check = False
        except:
            print("Invalid input, please try again.")

    # TODO The user should be able to select an author and see the title, year and venue of all articles by that author
    '''The result should be sorted based on year with more recent articles shown first '''

    ''' 
    CONCEPT: (needs work)
     
    SELECT *
    FROM article a
    WHERE (SELECT a.title, a.year, v.name
           FROM venue v
           WHERE 
           ORDER BY a.year)
    '''
    return
