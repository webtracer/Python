# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/12/2022
# Description: Hailstone code to calculate the math steps to get a value to 1 using
#       division by 2 or multiplication by 3 and adding 1

def hailstone(start_number):
    """
    function hailstone calculates the number of steps it takes to
    get a number result to the first value of 1:
        if the value is even, it is divided by 2
        if the value is odd, it is multiplied by 3 and has 1 added
    :param start_number: an integer value to calculate from
    :return: the final_answer is the number of steps it takes to get to 1
    """
    # variable final_answer keeps track of the steps it takes to get to 1
    final_answer = 0

    if start_number == 1:
        final_answer = 0
    else:
        while start_number != 1:
            if start_number % 2 == 0:
                # the start_number is even
                start_number = start_number / 2
                final_answer += 1
            else:
                # the start nunber is at least 3 and odd
                start_number = (start_number * 3) + 1
                final_answer += 1

    return final_answer


# answer = hailstone(1000)
# print(answer)
