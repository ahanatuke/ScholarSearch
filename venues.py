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
    '''
    select venue, count(distinct id)
    from article
    group by venue;
    '''

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