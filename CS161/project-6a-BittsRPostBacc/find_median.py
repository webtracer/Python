# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/23/2022
# Description: takes in a variable length number list
#         and returns the median value (middle value) of the list

def find_median (random_number_list):
    """ find_median takes in a variable length number list
        and returns the median value (middle value) of the list
    :param random_number_list: list of numbers from the user
    :return: list_median: the median value of the passed list
    """
    list_total_value = 0
    list_length = len(random_number_list)
    list_median = 0.0
    for item in random_number_list:
        list_total_value += item

    list_median = list_total_value / list_length

    return list_median


# some_nums = [13,7,-3,82,4]
# result = find_median(some_nums)

# print(result)

# different_nums = [2, 7, 10, 14.]
# result = find_median(different_nums)
# print(result)

# different_nums = [1, 2, 3, 4, 5]
# result = find_median(different_nums)
# print(result)
#
# different_nums = [1, 2, 3, 4, 5]
# result = find_median(different_nums[::-1])
# print(result)
