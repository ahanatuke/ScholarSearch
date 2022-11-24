

def listVenues(collection):
    print("Enter the amount of top venues you would like to see\nHit ENTER to go back to the mainpage\nHit E to exit the program")
    uI = input("> ")
    check = True
    while check:
        try:
            if uI == '':
                return
            elif uI.lower() == 'e':
                print("Exiting program...\nGoodbye.")
                exit()
            intuI = int(uI)
            check = True
        except:
            print("The input is not a number, please try again\nEnter the amount of top venues you would like to see"
                  "\nHit ENTER to go back to the mainpage\nHit E to exit the program")
            uI = input("> ")

    # TODO The user should be able to enter a number n and see a listing of top n venues
    ''' result = collection.aggregate([
     {"$lookup": {"from": "dblp", "localField": "id", "foreignField": "references", "as": "venueSelect"}},
     {"$unwind": {"path": "$venueSelect"}},
     {"$group": {"_id": "$venue", "venueIDRef": {"$addToSet": "$venueSelect.id"}}},
     {"$project": {"_id": 1, "n_references": {"$size": "$refSize"}}},
     {"$sort": {"n_references": -1}},
     {"$limit": intuI},
 ])

 for item in result:
     print(item)'''
    return




