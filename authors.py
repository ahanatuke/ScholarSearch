import venues
import pymongo

def searchAuthors(collection):
    # TODO Provide a keyword and see all authors whose names contain the keyword (the matches should be case-insensitive)
    print("Please enter in a keyword to search for authors."
          "\nHit ENTER to return back to the mainpage.")

    uI = input("> ")
    if uI == '':
        return
    uI = uI.lower().strip()

    # mongoDB here
    matchingResults = []
    # TODO For each author, list the author name and the number of publications
    #get all where some part of name matches with uI, group by the name and count publications

    results = collection.aggregate([
        {"$match": {
                "$text":
                {
                    "$search": "/"+uI+"/i",
                    "$caseSensitive": False
                }}
        },
        {"$unwind": "$authors"},
        {"$match":
             {"authors": {"$regex": "\\b"+uI+"\\b", "$options": 'i'} }
         },
        {
            "$group":
                {
                    "_id": "$authors",
                    "publications": {"$sum": 1}
                }
        }
    ])
    results = list(results)
    for item in results:
        print(item)

    print("Please select from 0 - ", len(results) - 1, "and select an author to look for.\nHit ENTER to leave\nE to exit")


    check = True
    while check:
        try:
            uI = input("> ")
            intuI = int(uI)
            uI = uI.lower().strip()
            if uI == '':
                return
            elif uI =='e':
                print("Exiting program...\nGoodbye.")
                exit()
            if intuI < 0:
                raise Exception
            if intuI >= len(results):
                raise Exception
            check = False
        except:
            print("Invalid input, please try again.")

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

    return
