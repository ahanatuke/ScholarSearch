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
        # allMatching = []
        # mongoDB here
        # TODO DONE retrieve all articles that match all those keywords (AND semantics)

        '''A keyword matches if it appears in any of title, authors, abstract, venue and year fields (the matches should 
        be case-insensitive) '''

        uiStr = '|'.join(uI)

        # uiStr = 'algorithm|object'

        # get one and add it into all matching
        # for i in range(len(uI)):
        results = collection.find(
            {"$text": {"$search": uiStr, "$caseSensitive": False}}
        )

        allMatching = list(results)

        # TODO For each matching article, display the id, the title, the year and the venue fields

        # if mongoDB returns an entire column we can simply display the parts we want to show for now
        if len(allMatching) == 0:
            print("No results found.")
            return
        else:
            for i in range(len(allMatching)):
                print(str(i) + ':', allMatching[i]['_id'], ",", allMatching[i]['title'], ",", allMatching[i]['year'],
                      ",", allMatching[i]['venue'])
            match = True

    # TODO Select an article to see all fields including the abstract and authors in addition to the fields shown before

    '''If the article is referenced by other articles, the id, the title, and the year of those references should be 
    also listed '''

    # TODO fix query
    check = True
    while check:
        valid = False
        print("Select a number corresponding to an article to see the details:\nHit ENTER to go back to the main page\nHit E to exit ")
        uI = input("> ").lower().strip()
        if uI == '':
            return
        if uI == 'e':
            print("Exiting program...\nGoodbye.")
            exit()
        try:
            intuI = int(uI)
            if intuI < 0:
                raise
            if intuI >= len(allMatching):
                raise
            valid = True
        except:
            print("Invalid input, please try again.")

        if valid:
            article = allMatching[intuI]
            try:
                field = "ID"
                print(field+':', article["_id"])
            except Exception as e:
                print("Error: "+field.lower()+" cannot be found\n"+field+": N/A")
            try:
                field = "Title"
                print(field+':', article["title"])
            except Exception as e:
                print("Error: "+field.lower()+" cannot be found\n"+field+": N/A")
            try:
                field = "Authors"
                print(field+':', article["authors"])
            except Exception as e:
                print("Error: "+field.lower()+" cannot be found\n"+field+": N/A")
            try:
                field = "Year"
                print(field+':', article["year"])
            except Exception as e:
                print("Error: "+field.lower()+" cannot be found\n"+field+": N/A")
            try:
                field = "Venue"
                print(field+':', article["venue"])
            except Exception as e:
                print("Error: "+field.lower()+" cannot be found\n"+field+": N/A")
            try:
                field = "n_citation"
                print(field+':', article["n_citation"])
            except Exception as e:
                print("Error: "+field.lower()+" cannot be found\n"+field+": N/A")
            try:
                field = "Referenced in: "
                results = collection.find(
                    {"references": article["_id"]},
                    {"_id": 1, "title": 1, "year": 1}
                )
                results = list(results)
                print(results)
                for item in results:
                    print(field + ':', item)
            except Exception as e:
                print("Error: " + field.lower() + " cannot be found\n" + field + ": N/A")
    # result = collection.find([
    #     {"__id" : selected}
    # ]).skip(selected - 1).limit(1)
    #
    # i = selected
    # print(str(i) + ':', allMatching[i]['_id'], ",", allMatching[i]['title'], ",", allMatching[i]['year'], ",", allMatching[i]['venue'])

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
    titleInput = input("Add a title\nHit ENTER to exit\n>").lower().strip()
    if titleInput == '':
        return
    authorsInput = input("Add the list of authors using spaces only\nHit ENTER to exit\n>").lower().split()

    if len(authorsInput) < 1:
        return

    check = True
    yearInput = input("Add the year for the article\n>").lower().strip()
    while check:
        try:
            yearInt = int(yearInput)
            check = False
        except:
            print("The year added is invalid, please try again.")
            yearInput = input("Add the year for the article\n>").lower().strip()

    # TODO Add an article to the collection by providing a unique id, a title, a list of authors, and a year
    newArticle = {"id": idInput,
                  "title": titleInput,
                  "authors": authorsInput,
                  "year": yearInput,
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
