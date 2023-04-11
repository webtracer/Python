# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 11/12/2022
# Description: takes a string and returns the number of unique letters in it

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
           "V", "W", "X", "Y", "Z"]


def count_letters(some_string):
    """
    count_letters takes a string and returns the number of unique letters in it
    No non-character values are counted
    :param some_string: random string text sent by the user
    :return: new_dict: Dictionary of the results
    """
    new_dict = {}

    for el in some_string:
        if el.upper() in letters:
            if el.upper() in new_dict:
                value = new_dict[el.upper()]
                new_dict.update({el.upper(): value + 1})
            else:
                new_dict[el.upper()] = 1

    return new_dict


# returned_dict = count_letters("Quis custodiet ipsos custodes?")
# print(returned_dict)