# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/12/2022
# Description: Function definition of fall_distance function
import math


def fall_distance(time_in_seconds):
    """ function fallDistance
        Takes in a time value
        and returns the distance that
        an object falls in normal gravity
        during the time duration
    """
    distance = 0.0
    gravity = 9.8
    distance = (1/2)*gravity*(math.pow(time_in_seconds, 2))
    return distance


# dist = fall_distance(4.6)
# print(dist)
