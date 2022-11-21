def venues():
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
    return