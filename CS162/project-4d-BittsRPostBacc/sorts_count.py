# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 01/31/2023
# Description: Program to count comparisons and exchanges in bubble and insertion sorts

# import random


def bubble_count(bubble_list):
    """
    Sorts a list in ascending order, and counts the number of comparisons and switches that are made
    :param bubble_list: a list to be sorted
    :return: bubble_comparison, bubble_exchange
    """

    # Variables to hold the comparison and exchange values - set to 0 to start
    bubble_comparison = 0
    bubble_exchange = 0

    for pass_num in range(len(bubble_list) - 1):
        for index in range(len(bubble_list) - 1 - pass_num):
            bubble_comparison += 1
            if bubble_list[index] > bubble_list[index + 1]:
                temp = bubble_list[index]
                bubble_list[index] = bubble_list[index + 1]
                bubble_exchange += 1
                bubble_list[index + 1] = temp

    # return f"There were {bubble_comparison} comparison and {bubble_exchange} exchanges"
    return bubble_comparison, bubble_exchange


def insertion_count(insertion_list):
    """
    Uses insertion sort algorithm to sort a list in ascending order, counting the number of comparisons and switches
        that are made in the process
    :param insertion_list: a list to be sorted
    :return: insert_compariosn, insert_exchange
    """

    # Variables to hold the comparison and exchange values - set to 0 to start
    insert_comparison = 0
    insert_exchange = 0

    for index in range(1, len(insertion_list)):
        value = insertion_list[index]
        pos = index - 1
        while pos >= 0 and insertion_list[pos] > value:
            insertion_list[pos + 1] = insertion_list[pos]
            insert_comparison += 1
            pos -= 1
            insert_exchange += 1
        insertion_list[pos + 1] = value

    # return f"There were {insert_comparison} comparison and {insert_exchange} exchanges"
    return insert_comparison, insert_exchange


# Function to generate a random list of 25 numbers
# def random_list():
#     """
#     generates and returns a random list of 25 integers
#     :return:
#     """
#     new_list = []
#     builder_list = []
#     i = 0
#
#     for x in range(1,25):
#         j = random.randint(1, 1000)
#         new_list.append(j)
#
#     return new_list


# first_test_list = [8, 7, 9, 5]
# second_test_list = [5, 7, 8, 2, 9]
# print(f"Original list is: {first_test_list}")
# print(insertion_count(first_test_list))
# print(f"After insertion sort list is: {first_test_list}")
# first_test_list = [8, 7, 9, 5]
# print(f"Original list is: {first_test_list}")
# print(bubble_count(first_test_list))
# print(f"After bubble sort list is: {first_test_list}")
# print(f"Second test list is: {second_test_list}")
# print(insertion_count(second_test_list))
# print(f"After insertion sort list is: {second_test_list}")
# second_test_list = [5, 7, 8, 2, 9]
# print(f"Second test list is: {second_test_list}")
# print(bubble_count(second_test_list))
# print(f"After bubble sort list is: {second_test_list}")

# generated_random_list = random_list()
# print(generated_random_list)
# print(f"The length of the random list is: {len(generated_random_list)}")
# print(insertion_count(generated_random_list))
# print(generated_random_list)
# generated_random_list = random_list()
# print(generated_random_list)
# print(f"The length of the random list is: {len(generated_random_list)}")
# print(bubble_count(generated_random_list))
# print(generated_random_list)
