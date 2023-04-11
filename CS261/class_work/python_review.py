# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date:
# Description:

import math


def fahrToCels(fahr_temp):
    """

    :param fahr_temp: Fahrenheit temp to convert
    :return: celcius temp
    """
    # cels = fahr_temp -32 / 1.8
    # return cels
    return (fahr_temp - 32) / 1.8


print(fahrToCels(50))


# math functions
degrees = 120
x = math.sin(degrees / 360.0 * 2 * math.pi)
y = math.exp(math.log(x+1))
print(x)
print(y)

# simple repition
for i in range(4):
    print(i)


# Conditionals and Recursion
