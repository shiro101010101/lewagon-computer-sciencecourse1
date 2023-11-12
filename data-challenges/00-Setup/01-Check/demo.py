"""Dummy challenge for Kitt Demo"""
"""Returns the area of the circle of given radius"""

import math

def circle_area(radius):
    if radius < 0:
        return 0
    else:
        return radius*radius*math.pi
