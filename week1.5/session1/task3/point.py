# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate): 
        # Add constructor here
        self.x = x_coordinate
        self.y = y_coordinate

    def distance(self):
        # Add distance() method here
        return math.hypot(self.x, self.y)
     
    # Add distance_to() method here
    
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
p = Point(1,2)
print(p.x)
print(p.y)