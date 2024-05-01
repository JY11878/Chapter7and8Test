# def the function
def leap_year(year):
    # write the nesting loop
    # first condition
    if year % 4 == 0:
        # second condition
        if year % 100 == 0:
            # third condition
            if year % 400 == 0:
                # if all three condition are satisfied
                print(year, "is leap")
            else:
                # if the third condition are not satisfied
                print(year, "is not leap")
        else:
            # if the first condition satisfied, but second isn't
            print(year, "is leap")
    # if the all three condition are not satisfied
    else:
        print(year, "is not leap")

# call the function and get the user input
leap_year(int(input("Enter a year: ")))