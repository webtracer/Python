# Exercises

# #1
import math


def distance(dist_1_x, dist_1_y, dist_2_x, dist_2_y):
    dist = math.sqrt(((dist_2_x-dist_1_x)**2 + (dist_2_y-dist_1_y)**2))
    return dist


d = distance(3, 5, -1, 2)
print(d)

d2 = distance(0, 0, 0, 0)
print(d2)
