# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 01/30/2023
# Description: A file that creates a class for boxes, creates box objects, then sorts them
#               from the greatest box volume to the least


class Box:
    """
    Class for storing Box objects
    """

    def __init__(self, length, width, height):
        """
        Constructor for the Box Class
        :param length: a float for the box length
        :param width: a float for the box width
        :param height: a float for the box height
        """
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """
        Getter for the box length
        :return: box length
        """
        return self._length

    def get_width(self):
        """
        Getter for the box width
        :return: box width
        """
        return self._width

    def get_height(self):
        """
        Getter for the box height
        :return: box height
        """
        return self._height

    def volume(self):
        """
        Function to return the volume of the box - length x width x height
        :return: box volume
        """
        return self._height * self._width * self._length


def box_sort(list_of_boxes):
    """
    An insertion sort to sort a list of Box objects by their volume from the greatest volume to least
    :param list_of_boxes: a list of Box objects
    :return: sorted list of Box objects
    """
    for index in range(0, len(list_of_boxes)):
        value = list_of_boxes[index]
        position = index -1
        while position >= 0 and Box.volume(value) > Box.volume(list_of_boxes[position]):
            list_of_boxes[position + 1] = list_of_boxes[position]
            position -= 1
        list_of_boxes[position + 1] = value

    return list_of_boxes


# b1 = Box(3.4, 19.8, 2.1)
# b2 = Box(1.0, 1.0, 1.0)
# b3 = Box(8.2, 8.2, 4.5)
# print(f"Box 1 volume is {Box.volume(b1)}")
# print(f"Box 2 volume is {Box.volume(b2)}")
# print(f"Box 3 volume is {Box.volume(b3)}")
# box_list = [b1, b2, b3]
# print(f"Box list before sort: {box_list}")
# print(box_sort(box_list))
