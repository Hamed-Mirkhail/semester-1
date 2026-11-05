# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        if not isinstance(width, int) or not isinstance(height, int):
           raise TypeError("width and height has to be an integer")
        if width <= 0 or height <= 0:
            raise ValueError("should be greater than 0")
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        """return true if equal"""
        return self.width == self.height
    def area(self):
        """ return area in rectangle"""
        return self.width * self.height
    def perimeter(self):
        """ return area in rectangle"""
        return 2 * (self.width + self.height)
        """return perimeter in rectangle"""
    # (See README.md for details of what they should do)