# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/03/2022
# Description: A program that takes an integer input and returns the factors including 1 and itself

# Obtain input from user and assign it to a variable
num_to_factor = int(input("Please enter a positive integer: "))

# Validate that the user input is postive and greater than 0
if num_to_factor > 0:

    print(f"The factors of {num_to_factor} are:")

    # Seed a counter for both the while loop and the factoring
    count = 1

    while count <= num_to_factor:  # run until the counter exceeds the entered integer
        if num_to_factor % count == 0:
            print(count)

        count += 1  # Increase the counter for both the while look and the factoring math

