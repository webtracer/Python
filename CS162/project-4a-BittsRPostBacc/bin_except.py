# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 01/30/2023
# Description: Alter the exploration binary search function to raise a Target Not Found exception instead
#                   od returning -1 when the target is not found

# import random for random list building to test the function
# import random


class TargetNotFound(Exception):
    """
    Class for raising an exception when the sort doesn't find what it's looking for
    """
    pass


# The Binary search function from the exploration
def bin_except(a_list, target):
    """
    Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, returns -1, indicating the target value isn't in the list
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    # Alteration here to return the error rather than just -1
    return TargetNotFound("Target Not Found")


# Function to generate a random list of 25 numbers
# def random_list():
#     """
#     generates and returns a random list of 25 integers
#     :return:
#     """
#     new_list = []
#     builder_list = []
#     i = 0
#
#     for x in range(1,25):
#         j = random.randint(1, 1000)
#         new_list.append(j)
#
#     return new_list

# Create a list to send to the sorting function
# list_to_sort = random_list()
# Print the list to verify the target is not there
# print(list_to_sort)
# Call the binary seach function, passing the random list plus an integer to search for
# print(binary_search(list_to_sort, 2))
