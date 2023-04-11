# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/30/22
# Description: Take a list of number and mutate the list to contain the squares

def square_list(number_list):
    """
    Take a list of numbers and mutates the list
        to contain the squares of the original list
    :param number_list:
    :return: nothing
    """
    count = 0
    while count < len(number_list):
        number_list[count] = number_list[count]**2
        count = count + 1


# nums = [7, -3, 12, 9]
# square_list(nums)
# print(nums)  # This should print [49, 9, 144, 81]
