# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/2/20200
# Description: Asks the user how many integers they want to enter
#              and then returns the min and max of the entered integers

# Get the user input for the number of integers they want to compare
print("How many integers would you like to enter?")
number_of_integers = input()

# Evaluate.  If the user enters 1 or 0, end execution otherwise lets compare
if number_of_integers == "":
    print("Error ... you did not enter anything.  Exiting....")
elif int(number_of_integers) == 1 or int(number_of_integers) == 0:
    print(f"The min and max of the number you entered is {number_of_integers}")
else:  # The user entered at least a 2
    print(f"Please enter {number_of_integers} integers.")
    largest = 0  # This will store the largest value
    smallest = 0   # This will store the smallest value
    count = int(number_of_integers)   # Used for while loop execution
    while count > 0:
        for number in number_of_integers:
            num = int(input())  # Get the users first integer
            if count == int(number_of_integers):  # This is only true the first time and sets initial min/max values
                smallest = num
                largest = num
            elif num > smallest:  # Each subsequent iteration compares smallest first
                if num > largest:  # If greater than smallest lets check the largest
                    largest = num
            else:  # current numer is the smallest
                smallest = num
            count -= 1  # Decrease while loop counter by 1
    # Return the results of the comparisons
    print("min: " + str(smallest))
    print("max: " + str(largest))
