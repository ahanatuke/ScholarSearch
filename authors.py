import venues
import pymongo

def searchAuthors(collection):
    print("Please enter in a keyword to search for authors."
          "\nHit ENTER to return back to the main page.")

    uI = input("> ")
    if uI == '':
        return
    uI = uI.lower().strip()

    matchingResults = []

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

    if len(results) == 0:
        print("No matches found.")
        return
    i = 1
    for item in results:
        print(f"{i}: {item['_id']}, publications: {item['publications']}")  # TODO current: 0: {'_id': 'Jovan Dj. Golic', 'publications': 1} DONE
        i += 1

    print("Please select from 1 -", len(results), "and select an author to look for.\nHit ENTER to leave\nHit E to exit")

    check = True
    while check:
        uI = input("> ").lower().strip()
        if uI == '':
            return
        elif uI == 'e':
            print("Exiting program...\nGoodbye.")
            exit()
        try:
            intuI = int(uI) - 1
            if intuI < 0:
                raise Exception
            if intuI >= len(results):
                raise Exception
            check = False
        except:
            print("Invalid input, please try again.")

    author = results[intuI]["_id"]

    results = collection.aggregate([
        {"$match":{
            "$text": {
                "$search": "/" + author + "/i",
                "$caseSensitive": False
            }}
        },
        {"$match":
             {"authors": {"$regex": "\\b"+author+"\\b", "$options": 'i'},

              }
         },

        {"$sort":
             {"year": -1}
         }

    ])
    results = list(results)

    for item in results:  # TODO if there's a blank it'll print it instead of the mssg
        print(item.get("title", "No title available"))
        print(item.get("venue", "No venue available"))
        print(item.get("abstract", "No abstract available"))
        print(item.get("year", "No year available"))
    ''' current
    Vectorial fast correlation attacks.


    2004
    '''

    return

