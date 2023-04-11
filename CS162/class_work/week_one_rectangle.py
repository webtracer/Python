class Rectangle:
    """

    """
    def __init__(self, height, width):
        self._height = height
        self._width = width

    def area(self):
        return self._height * self._width

    def perimeter(self):
        return self._height * 2 + self._width * 2

def main():
    rec_1 = Rectangle(3.4,7)
    print(rec_1.area())


if __name__ == '__main__':
    main()

