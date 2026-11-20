# Week 1.6, Session 1: Task 3
import math
from point import Point
# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)


class Circle(Shape):

    def __init__(self, radius, position, colour="red"):
        super().__init__(position, colour)
        self.set_radius(radius)

    def set_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        if radius <= 0:
            raise ValueError("radius must be greater than zero")

        self.radius = radius

    def __str__(self):
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius