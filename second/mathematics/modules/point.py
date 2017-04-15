# coding=utf-8
import math

class Point :
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def establishPolarCoordinatePoint(self, radius, angle, angleMode):
        try:
            angleValue = 0
            if (angleMode == 'a'):
                angleValue = angle
            elif (angleMode == 'r'):
                angleValue = angle * 180
            else:
                print 'Angle mode was error.'

            if (radius == 0):
                print 'Radius should not equal to 0.'
            else:
                x = radius * math.cos(angleValue)
                y = radius * math.sin(angleValue)
                tmpPoint = Point(x, y)
                rePoint = self + tmpPoint
                return rePoint
        except ValueError:
            print 'Arguments injected error.'