# Week 1.6, Session 1: Task 3
import math
from point import Point
# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
class Circle:

    def __init__(Self, radius, centre, colour = "red" ):
        self.set_radius(radius)
        self.centre = centre
        self.colour = colour

    def set_radius(self, radius):
         if not isinstance(radius(int, float)):
             raise TypeError("radius must be a number")

         if radius <= 0:
             raise ValueError("radius must be greater than zero")

             self.radius = radius

    def __str__(self):
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2.0 * math.pi * self.radius






