# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/16/2022
# Description: Recursive function that takes two integers and adds them to get their product

def multiply(num_one, num_two):
    """
    Takes 2 integer inputs and returns the product
        through recursive addition calls
    :param num_one: an integer
    :param num_two: another integer
    :return: the product of the two inputs
    """
    num_three = 0
    # print(f"Before the if: Num1 = {num_one}, Num2 = {num_two}, Num3 = {num_three}")
    if num_two != 0:
        num_three = num_one * num_two
        num_two -= 1
        # print(f"In the if: Num1 = {num_one}, Num2 = {num_two}, Num3 = {num_three}")
        multiply(num_one, num_two)
    return num_three


# final_answer = multiply(7, 5)
# print(final_answer)
