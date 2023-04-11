# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 11/12/2022
# Description: takes two strings and pulls out the common words

def words_in_both(first_string, second_string):
    """
    words_in_both takes two strings and pulls out the common words
    :param first_string:
    :param second_string:
    :return: the set of common words
    """
    common_words = set()
    split_first = first_string.split()
    split_second = second_string.split()

    for item in split_first:
        if item.lower() in split_second:
            common_words.add(item.lower())
    for item in split_second:
        if item.lower() in split_first and item.lower() not in common_words:
            common_words.add(item.lower())

    return common_words
