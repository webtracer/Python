# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 02/28/2023
# Description: A generator that returns a string sequence of digits that are sum values of the count of previous values

def count_seq():
    """
    A generator that returns a string sequence of digits that are sum values of the count of previous values
    :return: yields a string value
    """

    number = '2'     # Seed the string 2 to get started

    while True:     # For once an intentional infinite loop
        yield number   # Yield back the current 'number'
        next_iteration = ''       # Set the next string as empty

        while len(number) > 0:
            first_value = number[0]       # Pull the first value out
            count = 0                     # base digit count

            # Loop while number has values and first is the same as numbers first
            while len(number) > 0 and number[0] == first_value:
                count += 1  # Increment the counter
                number = number[1:]   # splice off the first value

            # Build the string value that is returned
            next_iteration = next_iteration + str(count) + first_value

        number = next_iteration  # Set number to the next_iteration


# my_gen = count_seq()
#
# for i in range(10):
#     print(next(my_gen))
