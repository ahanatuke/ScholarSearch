def searchArticles(collection):

    match = False
    while not match:
        print("Please enter in keywords for articles using spaces only."
              "\nHit enter to go back to the main page.")
        uI = input("> ")
        if uI == '':
            return
        uI = uI.lower().split(' ')
        uiStr = '|'.join(uI)

        results = collection.find(
            {"$text": {"$search": uiStr, "$caseSensitive": False}}
        )
        allMatching = list(results)

        if len(allMatching) == 0:
            print("No matches found.")
            return
        else:
            i = 1
            for item in allMatching:  # TODO will print blank space instead of '-'
                print(f"{i}: {item.get('_id', '-')}, {item.get('title', '-')}, {item.get('year', '-')}, {item.get('venue', '-')}")
                i += 1
            # for i in range(len(allMatching)):
            #     print(f"{i}: {allMatching[i].get('_id', '-')}, {allMatching[i].get('title', '-')}, {allMatching[i].get('year', '-')}, {allMatching[i].get('venue', '-')}")
                # print(str(i) + ':', allMatching[i]['_id'], ",", allMatching[i]['title'], ",", allMatching[i]['year'],
                #       ",", allMatching[i]['venue'])
            match = True

    check = True
    while check:
        valid = False
        print(
            "Select a number corresponding to an article to see the details:\n"
            "Hit ENTER to go back to the main page\nHit E to exit ")
        uI = input("> ").lower().strip()
        if uI == '':
            return
        if uI == 'e':
            print("Exiting program...\nGoodbye.")
            exit()
        try:
            intuI = int(uI) - 1
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
                print(field + ':', article["_id"])
            except Exception as e:
                print("Error: " + field.lower() + " cannot be found\n" + field + ": N/A")
            try:
                field = "Title"
                print(field + ':', article["title"])
            except Exception as e:
                print("Error: " + field.lower() + " cannot be found\n" + field + ": N/A")
            try:
                field = "Authors"
                print(field + ': ' + ', '.join(article["authors"]))
                # print(field + ':', article["authors"])  # TODO format better  current: Authors: ['Pranay Chaudhuri', 'Hussein Thompson'] DONE
            except Exception as e:
                print("Error: " + field.lower() + " cannot be found\n" + field + ": N/A")
            try:
                field = "Year"
                print(field + ':', article["year"])
            except Exception as e:
                print("Error: " + field.lower() + " cannot be found\n" + field + ": N/A")
            try:
                field = "Venue"
                print(field + ':', article["venue"])
            except Exception as e:
                print("Error: " + field.lower() + " cannot be found\n" + field + ": N/A")
            try:
                field = "n_citation"
                print(field + ':', article["n_citation"])
            except Exception as e:
                print("Error: " + field.lower() + " cannot be found\n" + field + ": N/A")
            try:
                field = "Referenced in"
                results = collection.find(
                    {"references": article["_id"]},
                    {"_id": 1, "title": 1, "year": 1}
                )
                results = list(results)
                print(field + ': ' + ', '.join(results))
                # for item in results:
                #    print(field + ':', *item)  # TODO format better  current: [] DONE
            except Exception as e:
                print("Error: " + field.lower() + " cannot be found\n" + field + ": N/A")

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
    titleInput = input("Add a title\nHit ENTER to exit\n> ").lower().strip()
    if titleInput == '':
        return
    authorsInput = input("Add the list of authors using spaces only\nHit ENTER to exit\n> ").lower().split()

    if len(authorsInput) < 1:
        return

    check = True
    yearInput = input("Add the year for the article\n> ").lower().strip()
    while check:
        try:
            yearInt = int(yearInput)
            check = False
        except:
            print("The year added is invalid, please try again.")
            yearInput = input("Add the year for the article\n> ").lower().strip()

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

    print(f"New article successfully added:\n"
          f"Id: {idInput}\n"
          f"Title: {titleInput}\n"
          f"Authors: {', '.join(authorsInput)}\n"
          f"Year: {yearInput}")

    return
