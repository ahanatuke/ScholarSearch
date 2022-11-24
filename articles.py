from math import floor


def searchArticles(collection):

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

        uiStr = 'algorithm|object'
        # UNIONS: https://medium.com/idomongodb/mongodb-unions-cb102d6d37ea

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
                print(str(i) + ':', results[i][0], results[i][1], results[i][4], results[i][3])
            match = True


    # TODO Select an article to see all fields including the abstract and authors in addition to the fields shown before

    '''If the article is referenced by other articles, the id, the title, and the year of those references should be 
    also listed '''

    print("Select a number corresponding to an article to see the details:")
    selected = int(input('> '))
    # TODO fix query
    # result = collection.find([
    #     {"__id" : selected}
    # ]).skip(selected - 1).limit(1)
    #
    # result = list(result)
    # for item in result:
    #     print(item)

    # TODO print the specific list and get the year of every reference
    uI = input("Please select a number from 0 -", len(allMatching) - 1, "to select an article.\nHit enter to leave\nE to exit")
    check = True
    while check:
        try:
            if uI == '':
                return
            elif uI == 'E':
                print("Exiting program...\nGoodbye.")
                exit()
            intuI = int(uI)
            if intuI < 0:
                raise Exception
            if intuI >= len(allMatching):
                raise Exception
            check = False
        except:
            print("Invalid input, please try again.")



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

        result = collection.find(
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
    collection.insertOne(newArticle)

    # TODO The fields abstract and venue should be set to null, references should be set to an empty array and
    #  n_citations should be set to zero
    # TODO test query
    collection.insert_many(
        {"abstract": None},  # set to NULL
        {"venue": None},  # set to NULL
        {"reference": []},  # set to empty array
        {"n_citations": 0}  # set to 0
    )

    return
