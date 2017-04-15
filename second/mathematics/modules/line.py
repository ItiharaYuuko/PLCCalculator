# coding=utf-8

from point import Point
import math


class Line:
    startPoint = Point(0, 0)
    endPoint = Point(0, 0)
    length = 0
    angle = 0

    def __init__(self, stP, edP):
        try:
            self.startPoint = stP
            self.endPoint = edP
            subPoint = self.endPoint - self.startPoint
            tmpX = float(pow(subPoint.x, 2))
            tmpY = float(pow(subPoint.y, 2))
            self.length = math.sqrt(tmpX + tmpY)
            print self.length
            if (tmpX == 0):
                if (tmpY > 0):
                    self.angle = 90
                elif (tmpY < 0):
                    self.angle = 270
                else:
                    raise ValueError('Can not create a line.')
            else:
                if (self.startPoint.x == self.endPoint.x):
                    self.angle = 90
                elif (self.startPoint.y == self.endPoint.y):
                    self.angle = 0
                else:
                    self.angle = math.degrees(math.atan(subPoint.x / subPoint.y))
        except TypeError:
            print 'Point type inject error.'

    @classmethod
    def establishPolarCoordinateLine(self, stP, length, angleMode, angle):
        try:
            if (angleMode == 'a'):
                self.angle = angle
            elif (angleMode == 'r'):
                self.angle = math.degrees(angle)
            else:
                print 'Angle mode was error.'
            self.startPoint = stP
            self.length = length
            rePoint = self.startPoint.establishPolarCoordinatePoint(length, angleMode, angle)
            self.endPoint = rePoint
            return self
        except ValueError:
            print 'Arguments injected error.'

    def inlineJudge(self, pointP):
        linX = Line(pointP, self.startPoint)
        linY = Line(pointP, self.endPoint)
        sumLen = linX.length + linY.length
        if (sumLen == self.length):
            return True
        else:
            return False