# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/30/22
# Description: Takes a list and reverses it without slicing

def reverse_list(value_list):
    """
    Takes a list and reverses it without slicing
    :param value_list: A list of values sent by the user
    :return: Nothing
    """
    second_value_list = []
    count = 0
    while count < len(value_list):
        second_value_list = second_value_list + [value_list[(len(value_list)-1)-count]]
        count = count + 1
    count = 0
    while count < len(second_value_list):
        value_list[count] = second_value_list[count]
        count = count + 1


# vals = [7, -3, 12, 9]
# reverse_list(vals)
# print(vals)  # This should print [9, 12, -3, 7]
