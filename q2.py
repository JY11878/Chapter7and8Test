def average_calculation():
    # set the initial value for sum and count of numbers
    sum = 0
    nums = 0
    # use while loop to keep it executing
    while True:
        # get user input
        n = input("Enter a number ( to quit)")
        # set the sentinel value, when user input the special value, the while loop breaks
        if n == "":
            break
        # get the sum of user inputs, and the count of user inputs
        sum += float(n)
        nums += 1
    # if the user have input any number, calculate the average
    if nums > 0:
        avg = sum/nums
        print("The average of the number is", avg)

average_calculation()
