from math import floor


def searchArticles(collection):
    print("Please enter in a keyword to search for authors."
          "\nHit ENTER to return back to the mainpage.")


    match = False
    while not match:
        print("Please enter in keywords for articles using spaces only.\nHit enter to go back to the main page.")
        uI = input("> ")
        if uI == '':
            return
        uI = uI.lower().split(' ')
        #allMatching = []
        # mongoDB here
        # TODO DONE retrieve all articles that match all those keywords (AND semantics)


        '''A keyword matches if it appears in any of title, authors, abstract, venue and year fields (the matches should 
        be case-insensitive) '''

        uiStr = '|'.join(uI)

        #uiStr = 'algorithm|object'

        # get one and add it into all matching
        #for i in range(len(uI)):
        results = collection.aggregate([
            {'$match' : {'$or':
                [
                {"title": {'$regex' : uiStr, '$options' : 'i'}},
                {"authors": {'$regex' : uiStr, '$options' : 'i'}},
                {"abstract": {'$regex' : uiStr, '$options' : 'i'}},
                {"venue": {'$regex' : uiStr, '$options' : 'i'}},
                {"year": {'$regex' : uiStr, '$options' : 'i'}} ]
             }
            },
            {'$project':
                 {
                    "title": 1,
                    "year": 1,
                    "venue": 1
                  }
             }
        ])
        allMatching = list(results)

        # TODO For each matching article, display the id, the title, the year and the venue fields

        # if mongoDB returns an entire column we can simply display the parts we want to show for now
        if allMatching[0] is None:
            print("No results found.")
        else:
            for i in range(len(allMatching)):
                print(str(i) + ':', allMatching[i]['_id'], ",", allMatching[i]['title'], ",", allMatching[i]['year'], ",", allMatching[i]['venue'])
            match = True


    # TODO Select an article to see all fields including the abstract and authors in addition to the fields shown before

    '''If the article is referenced by other articles, the id, the title, and the year of those references should be 
    also listed '''

    print("Select a number corresponding to an article to see the details:\nHit ENTER to go back to the main page\nHit E to exit ")
    # TODO fix query
    check = True
    while check:
        uI = input("> ").lower().strip()
        if uI == '':
            return
        elif uI == 'e':
            print("Exiting program...\nGoodbye.")
            exit()
        try:
            intuI = int(uI)
            if intuI < 0:
                raise Exception
            if intuI >= len(results):
                raise Exception
            check = False
        except:
            print("Invalid input, please try again.")

    allMatching[intuI]["_id"]
    result = collection.aggregate([
        {"$match":
             {"$text": {
                 "$search": "/"
             }}
         }
    ])
    # result = collection.find([
    #     {"__id" : selected}
    # ]).skip(selected - 1).limit(1)
    #
    # i = selected
    print(str(i) + ':', allMatching[i]['_id'], ",", allMatching[i]['title'], ",", allMatching[i]['year'], ",", allMatching[i]['venue'])

    # while loop:
    #     user_input = input("Choose an article by entering their index no. or enter 'q' to quit: ")
    #
    #     if user_input == 'q':
    #         loop = False
    #         return 0
    #     elif user_input.isdigit() == False:
    #         print('Invalid option')
    #         continue
    #
    #     elif if its valid userinput:
    #         print([int(user_input) - 1]['title']))
    #
    #         try:
    #             print('Title': results[int(user_input) - 1]['title']))
    #             except KeyError:
    #             print('Title: None')
    #
    #         try:
    #             print('Authors': results[int(user_input) - 1]['authors']))
    #             except KeyError:
    #             print('Authors: None')


    return



def addArticle(collection):
    abstract = None
    venue = None
    references = []
    n_citations = 0
    check = True

    while check:
        idInput = input("Add an id\nHit ENTER to go back to the main page\n> ").lower().strip()
        if idInput == '':
            return

        result = collection.find_one(
            {"id": idInput}
        )

        if result is not None:
            print("This id is already taken, please try again.")
        else:
            check = False
    check = True
    titleInput = input("Add a title\n>").lower().strip()
    authorsInput = input("Add the list of authors using spaces only\n>").lower().split()

    while check:
        if len(authorsInput) < 1:
            print("Please include at least one author.")
            input("Add the list of authors using spaces only\n>").lower().split()
        else:
            check = False

    check = True
    yearInput = input("Add the year for the article\n>").lower().strip()
    while check:
        try:
            yearInt = int(yearInput)
            check = False
        except:
            print("The year added is not a valid year, please try again.")
            year = input("Add the year for the article\n>").lower().strip()

    # TODO Add an article to the collection by providing a unique id, a title, a list of authors, and a year
    newArticle = {"id": idInput,
                  "title": titleInput,
                  "authors": authorsInput,
                  "year": yearInt,
                  "venue": venue,
                  "n_citation": n_citations,
                  "references": references,
                  "abstract": abstract
                  }
    collection.insert_one(newArticle)

    # TODO The fields abstract and venue should be set to null, references should be set to an empty array and
    #  n_citations should be set to zero
    # TODO test query

    return
