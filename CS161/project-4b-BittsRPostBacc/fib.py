# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/13/2022
# Description: Fibonacci sequence value finder

def fib(start_num):
    """
        Function fib takes in an integer value
            and returns the integer value at that spot
                in the Fibonacci sequence.
    :param n: This is the number of digits into the sequence we are
                looking for the value of
    :return: num3 which contains the value of that spot in the sequence.

    Note: The commented print statements are from testing
    """
    num1 = 1  # 1st value in the Fibonacci sequence
    num2 = 1  # 2nd value in the Fibonacci sequence

    if start_num == 1:
        num3 = 0
    else:
        for i in range(2, start_num):
            num3 = num1 + num2
            # print(f"at the start a+b={num3}")
            num1 = num2
            # print(f"now a=b and a={num1}")
            num2 = num3
            # print(f"now b=c and b={num2}")
            # print(f"now the value of c is {num3}")
    return num3


# fib_num = fib(10)
# print(f"Final num is: {fib_num}")
