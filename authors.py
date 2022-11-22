def searchAuthors(collection):
    print("Please enter in keywords to search for authors using spaces only ")
    uI = input("> ").lower().split()

    # mongoDB here
    # TODO Provide a keyword and see all authors whose names contain the keyword (the matches should be case-insensitive)
    results = collection.find({"name": '/'+uI+'/'})
    # TODO For each author, list the author name and the number of publications

    '''CONCEPT: 
    For every author in results: 
    SELECT a.name, SUM(*)
    FROM publications as p1, publications as p2
    WHERE a1.name = a2.name and paperID1 != paperID2 '''


    # TODO The user should be able to select an author and see the title, year and venue of all articles by that author
    '''The result should be sorted based on year with more recent articles shown first '''

    return