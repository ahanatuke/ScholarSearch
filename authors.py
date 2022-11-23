import venues
import pymongo

def searchAuthors(collection):
    # TODO Provide a keyword and see all authors whose names contain the keyword (the matches should be case-insensitive)
    print("Please enter in keywords to search for authors using spaces only. "
          "\nHit ENTER to return back to the mainpage.")

    uI = input("> ")
    if uI == '':
        return
    uI = uI.lower().split()

    # mongoDB here

    # TODO For each author, list the author name and the number of publications
    #get all where some part of name matches with uI, group by the name and count publications
    results = collection.aggregate([
        {
            "$match":
                {"name": '/' + uI + '/'}
        },
        {
            "$group":
                {
                    "_id": "name",
                    "publications": {"$count": {}}
                }
        }])

    print("Please select from 0 - ", len(results) - 1, "and select an author to look for.\nHit ENTER to leave\nE to exit")
    uI = input("> ").lower()

    check = True
    while check:
        try:
            if uI == '':
                return
            elif uI =='E':
                print("Exiting program...\nGoodbye.")
                exit()
            intuI = int(uI)
            if intuI < 0:
                raise Exception
            if intuI >= len(results):
                raise Exception
            check = False
        except:
            print("Invalid input, please try again.")
    '''CONCEPT: 
    For every author in results: 
    SELECT a.name, SUM(*)
    FROM article as a1, article as a2
    WHERE a1.name = a2.name and a1.id != a2.id '''

    author = results[uI][0]
    # TODO The user should be able to select an author and see the title, year and venue of all articles by that author
    '''The result should be sorted based on year with more recent articles shown first '''

    #get all of stuff that matches the authors name, group by year, and sort by year descending
    #see if it works and find a way to display title, year and venue only
    collection.aggregate([
        {"$match":
             {"authors": author}
         },
        {"$group":
             { "_id": "year" }
        },
        {"$sort":
            {"year", -1}
         }

    ])
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
