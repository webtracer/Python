# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/23/2022
# Description: Take a list of names and adds the surname Kardashian
#                to any name that beings with a K

def add_surname(name_list):
    """ add_surname takes a list of first names, and if they start with "K"
            it appends Kardashian (with a space between) and returns the
            Kardashian only list
    :param name_list: A list of first names submitted by the user
    :return: completed_name_list: the list of "K" names with Kardashian appended
    """
    completed_name_list = []
    for name in name_list:
        if "K" in name[0:1]:
            completed_name_list = completed_name_list + [name + " Kardashian"]

    return completed_name_list


# list_of_names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
# print(add_surname(list_of_names))
