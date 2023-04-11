def is_subsequence(first_string, second_string):
    """
    Function takes two strings, one is a subsequence of letters,
        the second is the string to check if the first is actually a subsequence
    :param first_string: a string list containing a subsequence
    :param second_string: a string list to check the subsequence for
    :return: True or False of subsequence
    """

    # If the two strings are blank, return true because that is a subsequence
    if first_string == "" and second_string == "":
        return True
    # If the first string is done, and there are letters left in the second, it is a subsequence
    elif first_string == "" and len(second_string) > 0:
        return True

    # Check if the string to be checked is out of letters with left in the subsequence
    if second_string == "" and len(first_string) > 0:
        return False
    elif first_string[0] == second_string[0]: # Compare the first letters of each string
        return is_subsequence(first_string[1:], second_string[1:])  # call the function after slicing the first letter
    else:  # They don't match, slice the first letter off the string to be checked and call the function again
        return is_subsequence(first_string, second_string[1:])


# # string_one = "racecar"
# # string_one = "faceitious"
# # string_two = "aeiou"
# subsequence = "afoni"
# string = "California"
#
# # print(is_subsequence(string_one,string_two))
# # print(is_subsequence(string_two,string_one))
# print(is_subsequence(subsequence, string))
