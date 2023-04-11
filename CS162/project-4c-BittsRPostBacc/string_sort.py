# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 01/30/2003
# Description: Sorts a list of strings, returns them in alphabetical order regardless of Capital letters


def string_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos].upper() > value.upper():
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value

    return a_list


# list_to_be_sorted = ["apple", "Orange", "zebra", "car", "Insertion"]
# print(string_sort(list_to_be_sorted))
