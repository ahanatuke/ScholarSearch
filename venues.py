def listVenues():
    print("Enter the amount of top venues you would like to see")
    uI = input("> ")
    check = True
    while check:
        try:
            uI = int(uI)
            check = True
        except:
            print("The input is not a number, please try again"
                  "Enter the amount of top venues you would like to see")
            uI = input("> ")

    # DB here
    # TODO The user should be able to enter a number n and see a listing of top n venues

    # TODO For each venue, list the venue, the number of articles in that venue, and the number of articles that
    #  reference a paper in that venue

    # TODO Sort the result based on the number of papers that reference the venue with the top most cited venues
    #  shown first

    return