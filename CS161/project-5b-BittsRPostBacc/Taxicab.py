# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date:
# Description:

class Taxicab:
    """
    Represents a taxi cab and it's movement
    Each cab object has an x and y coordinate
    and all cab objects start with an odometer of 0
    """
    def __init__(self, x_coord, y_coord, odometer=0):
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = odometer

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def get_odometer(self):
        return self._odometer

    def move_x(self, x_coord):
        """
        Moves the cab along the x-axis
        :param x_coord: Number of units to move along x (positive or negative)
        :return: the updated x-coordinate after moving from the beginning position
        """
        if x_coord > 0:
            self._odometer += x_coord
            self._x_coord += x_coord
            return self._x_coord
        elif x_coord < 0:
            self._odometer += (-x_coord)
            self._x_coord += x_coord
            return self._x_coord
        else:
            return self._x_coord

    def move_y(self, y_coord):
        """
        Moves the cab along the y-axis
        :param y_coord: Number of units to move up or down y  (positive or negative)
        :return: the updated y-coordinate after moving from the beginning position
        """
        if y_coord > 0:
            self._odometer += y_coord
            self._y_coord += y_coord
            return self._y_coord
        elif y_coord < 0:
            self._odometer += (-y_coord)
            self._y_coord += y_coord
            return self._y_coord
        else:
            return self._y_coord


# cab = Taxicab(5, -8)       # creates a Taxicab object at coordinates (5, -8)
# print(f"The current coordinates are: x: {cab.get_x_coord()} and y: {cab.get_y_coord()}")
# cab.move_x(3)             # moves cab 3 units "right"
# print(f"The current coordinates are: x: {cab.get_x_coord()} and y: {cab.get_y_coord()}")
# cab.move_y(-4)           # moves cab 4 units "down"
# print(f"The current coordinates are: x: {cab.get_x_coord()} and y: {cab.get_y_coord()}")
# cab.move_x(-1)             # moves cab 1 unit "left"
# print(f"The current coordinates are: x: {cab.get_x_coord()} and y: {cab.get_y_coord()}")
# print(cab.get_odometer())  # prints the current odometer reading
# At this point the cab has traveled 3 + 4 + 1 = 8 units and is now at coordinates (7, -12)
# print(f"The current coordinates are: x: {cab.get_x_coord()} and y: {cab.get_y_coord()}")