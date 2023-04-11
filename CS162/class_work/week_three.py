#  Week 3 notes and examples

# Inheritance and Composition
class Rectangle:
    """
    represents a geometric rectangle
    """
    def __init__(self,length, width):
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * self._length +2 * self._width


# Inheritance
class Square(Rectangle):
    """
    Represents a geometric square
    Inherits from Rectangle
    """
    def __init__(self, side):  # This is an override of the Parent class INIT method
        self._length = side
        self._width = side
        # The override can also be done this way
        # super().__init__(side,side)


class Squared(Rectangle):
    """
    Represents a geometric square
    Inherits from Rectangle
    """
    def __init__(self, side):
        super().__init__(side, side)
        # This method gives a temporary object of the parent class to use


# Composition rather than inheritance ... Cube and Square/Rectangle are similar but not the same
#   Square inherits from Rectangle because a Square IS A Rectangle, whereas a Cube HAS A Square (6 of them)
class Cube:
    """
    represents a geometric cube
    """
    def __init__(self, side):
        self.face = Square(side)  # face is a data member of type square

    def surface_area(self):
        return self.face.area() * 6

    def volume(self):
        return self.face.area() * self.face.get_length()

    def area(self):
        return self._side * 6


# Polymorphism - is when code can operate on objects of different types in the same way,
#  but with results specific to the actual object being operated on.

class Lawnmower:
    '''
    Represents a machine that cuts grass
    '''

    def start(self):
        print("Ready to cut grass...")


class Movie:
    '''
    represents a motion picture
    '''
    def start(self):
        print("Movie has started.")


# In the lecture the above two classes are imported from a different file
#   to be used by the below code

def start_things(thing_list):
    """Starts each thing in thing_list
        regardless of its actual object type, Python starts the correct one
    """
    for thing in thing_list:
        thing.start()


jeff = Lawnmower()
inception = Movie()

# A list of two different types of objects
stuff = [jeff, inception]
start_things(stuff)
stuff_one = [inception, jeff]
start_things(stuff_one)


# Overriding dunder ("magic") methods
# __str__ and __repr__
def __repr__(self):
    return "Rectangle(" + repr(self._length) + ", " + repr(self._width) + ")"


def __str__(self):
    return "A rectangle with a length of " + str(self._length) + " and a width of " + str(self._width)


my_rectangle = Rectangle(12, 24)
my_rectangle_two = Rectangle(12, 24)
my_square = Square(6)
my_cube = Cube(5)

print("This is what the normal call looks like")
print(my_rectangle.area())
print("This is what __repr__ looks like")
print(repr(my_rectangle))
print("And now for __str__")
print(str(my_rectangle))


def print_the_areas():
    print("Areas from a standalone function")
    print(my_rectangle.area())
    print(my_cube.area())
    print(my_square.area())


print_the_areas()

# __eq__
# Overriding __eq__ in a class enables you to use the == operator with objects of that class.
# Let's again use Rectangle class to illustrate. Remember that checking floats for exact equality doesn't
#   always work because of possible roundoff error.
import math


def __eq__(self, other):
    return math.isclose(self._length, other._length) and math.isclose(self._width, other._width)


if my_rectangle == my_rectangle_two:
    print(__eq__(my_rectangle_two))

