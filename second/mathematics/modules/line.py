# coding=utf-8

from point import Point
import math

class Line:
    startPoint = Point(0, 0)
    endPoint = Point(0, 0)

    def __init__(self, stP, edP):
        try:
            self.startPoint = stP
            self.endPoint =edP
        except TypeError:
            print 'Point type inject error.'

    def length(self):
        subPoint = self.endPoint - self.startPoint
        tmpX = float(pow(subPoint.x, 2))
        tmpY = float(pow(subPoint.y, 2))
        # print 'x = %f , y = %f' % (tmpX, tmpY)
        lenX = math.sqrt(tmpX + tmpY)
        return lenX

    def inlineJudge(self, pointP):
        linX = Line(pointP, self.startPoint)
        linY = Line(pointP, self.endPoint)
        sumLen = linX.length() + linY.length()
        if (sumLen == self.length()):
            return True
        else:
            return False