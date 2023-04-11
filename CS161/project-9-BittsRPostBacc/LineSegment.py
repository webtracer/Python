# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 11/20/2022
# Description: Creates Point and Line Segments and ultimately
# determines if the line segments are parallel or not

class Point:
    """
    Represents the x,y coordinates on the line segments
    """

    def __init__(self, x_coord, y_coord):
        """
        Constructor for the Point class
        :param x_coord: takes an integer as the x coordinate
        :param y_coord: takes an integer as the y coordinate
        """
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        """
        Getter for the x_coord
        :return: private member x_coord
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Getter for the y_coord
        :return: private member y_coord
        """
        return self._y_coord

    def distance_to(self, point):
        """
        returns the distance between the Point object calling
        and the point object passed
        :return:
        """
        # This is where the distance formula is used
        # d = ((x2-x1)**2+(y2-y1)**2) **.05
        distance = ((point.get_x_coord() - self._x_coord)**2+(point.get_y_coord()-self._y_coord)**2)**0.5
        return distance


class LineSegment:
    """
        Represents the combined endpoints that make a line segment
    """

    def __init__(self, endpoint_1, endpoint_2):
        """
        Constructor for LineSegment class
        :param endpoint_1: takes an endpoint and stores the Point objects
        :param endpoint_2: takes an endpoint and stores the Point objects
        """
        self._endpoint_1 = Point(endpoint_1.get_x_coord(), endpoint_1.get_y_coord())
        self._endpoint_2 = Point(endpoint_2.get_x_coord(), endpoint_2.get_y_coord())

    def get_endpoint_1(self):
        """
        Getter for endpoint_1
        :return:
        """
        return self._endpoint_1

    def get_endpoint_2(self):
        """
        Getter for endpoint_2
        :return:
        """
        return self._endpoint_2

    def length(self):
        """
        Gives the length between two line segments
        :return:
        """
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        """
        Returns the slope of line segments
        :return:
        """
        return (self._endpoint_2.get_y_coord()-self._endpoint_1.get_y_coord())/\
               (self._endpoint_2.get_x_coord()-self._endpoint_1.get_x_coord())

    def is_parallel_to(self, line_segment):
        """
        Determines if 2 line segments are parallel or not
        :param line_segment:
        :return:
        """
        if abs(self.slope() - line_segment.slope()) < 0.000001:
            return True
        else:
            return False

#
# point_1 = Point(0,2)
# point_2 = Point(2,0)
# print(point_1.distance_to(point_2))
# line_seg_1 = LineSegment(point_1,point_2)
# print(line_seg_1.length())
# print(line_seg_1.slope())
#
# point_3 = Point(0, 4)
# point_4 = Point(4, 0)
# line_seg_2 = LineSegment(point_3, point_4)
# print(line_seg_1.is_parallel_to(line_seg_2))
