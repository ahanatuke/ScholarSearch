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

    # DB here
    # TODO The user should be able to enter a number n and see a listing of top n venues
    '''
    select venue, count(distinct id)
    from article
    group by venue;
    '''
    #https://stackoverflow.com/questions/24761266/select-group-by-count-and-distinct-count-in-same-mongodb-query/24770233#24770233
    collection.aggregate([
        {"$match":
            {"venue": {"$ne": "null"}}
         },

        {"$group":  {
            "_id":
                {
                    "venue": "$venue",
                    "id": "$id"
                },
            }},

        {"$group": {
            "_id": {
                "venue": "$_id.venue",
                "id": "$_id.id"
            },
            "distinctID": {"$sum": 1}
        }},



        {"$sort": "$._id.id"},
        {"$limit": intuI}
    ])

    # TODO For each venue, list the venue, the number of articles in that venue, and the number of articles that
    #  reference a paper in that venue
    '''
    select a2.venue, count(distinct a1.id)
    from article a1, article a2
    where a1.reference=a2.id
    group by a2.venue
    order by count(*) desc
    '''
    # TODO Sort the result based on the number of papers that reference the venue with the top most cited venues
    #  shown first

    return