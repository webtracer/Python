# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 02/13/2023
# Description: A recursive program to check if a list of integers is in descending/decreasing order

def is_decreasing(list_to_check, pos=0, it_decreased=False):
    """

    :param list_to_check: The list to check if it is decreasing in order
    :param pos: Position in the list, initialized to 0 at start
    :param it_decreased: Boolean to track if the list is decreasing
    :return: the value of it_decreased, or False if it is ever not decreasing
    """
    if pos == len(list_to_check):
        return it_decreased
    elif pos == 0:
        return is_decreasing(list_to_check, pos+1, it_decreased)
    elif list_to_check[pos] < list_to_check[pos-1]:
        it_decreased = True
        return is_decreasing(list_to_check, pos+1, it_decreased)
    else:
        it_decreased = False
        return it_decreased

#
# list_one = [5,4,3,1,2]
# list_two = [5,4,3,2,1]
# list_three = [2,1]
#
# print(is_decreasing(list_one))
