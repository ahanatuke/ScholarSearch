import initDB as store
import articles
import authors
import venues


def main():

    jsonFile = input('Please enter a json file name: ').strip() + '.json'
    portNum = 'mongodb://localhost:' + input('Please enter a port number: ').strip() + '/'

    collection = store.init_db(jsonFile, portNum)

    print(collection)
    done = False
    while not done:
        print("To search for an article enter 'A\n"
              "To search for an author enter 'U'\n"
              "To list venues within a range enter 'V'\n"
              "To add an article enter 'R'\n"
              "To quit enter 'Q'")
        uI = input("> ").lower().strip()
        if uI == 'a':
            articles.searchArticles(collection)
            pass
        elif uI == 'u':
            authors.searchAuthors(collection)
            pass
        elif uI == 'v':
            venues.listVenues(collection)
            pass
        elif uI == 'r':
            articles.addArticle(collection)
            pass
        elif uI == 'q':
            print("Exiting program...")
            print("Goodbye")
            done = True
        else:
            print("Invalid input, try again.")
            uI = input("> ").lower().strip()

    return


main()
