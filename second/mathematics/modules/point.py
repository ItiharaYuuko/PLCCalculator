# coding=utf-8
import math


class Point:
    x = 0
    y = 0
    polarFlag = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.polarFlag = False

    def __add__(self, p):
        try:
            px = Point(p.x + self.x, p.y + self.y)
            return px
        except TypeError:
            print 'Point Type Error'

    def __sub__(self, q):
        try:
            py = Point(self.x - q.x, self.y - q.y)
            return py
        except TypeError:
            print 'Point Type Error'

    def establishPolarCoordinatePoint(self, radius, angleMode, angle):
        try:
            self.polarFlag = True
            angleValue = 0
            if (angleMode == 'a'):
                angleValue = angle
            elif (angleMode == 'r'):
                angleValue = math.degrees(angle)
            else:
                print 'Angle mode was error.'
            angleR = math.radians(angleValue)
            if (radius == 0):
                print 'Radius should not equal to 0.'
            else:
                x = radius * math.cos(angleR)
                y = radius * math.sin(angleR)
                tmpPoint = Point(x, y)
                rePoint = self + tmpPoint
                return rePoint
        except ValueError:
            print 'Arguments injected error.'
