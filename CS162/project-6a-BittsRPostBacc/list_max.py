# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 02/13/2023
# Description: Program for a recursive function to find the maximum value in a list

def list_max(list_to_check, pos = 0, list_max_value = 0):
    """
    Recursive function that takes a list, initializes a position counter to 0
        and initializes the max value in the list to 0 as well, and recursively
        returns the lists max value
    :param list_to_check: the list sent to get the Max value of
    :return: list_max_value - the maximum value of the list
    """
    if pos == len(list_to_check):
        return list_max_value
    elif list_max_value < list_to_check[pos]:
        list_max_value = list_to_check[pos]
        return list_max(list_to_check, pos + 1, list_max_value)
    elif list_max_value >= list_to_check[pos]:
        return list_max(list_to_check, pos + 1, list_max_value)


# list_one = [1,4,5,6,3,2]
# list_two = [5]
# print(list_max(list_two))
