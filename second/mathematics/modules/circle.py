# coding=utf-8

import math
import statues
from line import Line
from point import Point

pi = math.pi

def squareRoot(x):
    return math.sqrt(x)

class Circle:
    center = Point(0,0)
    radius = 0

    def __init__(self, centerPoint, radius):
        try:
            self.center = centerPoint
            self.radius = radius
        except TypeError:
            print 'Point type error or radius type error.'

    def square(self):
        return pi * pow(self.radius, 2)

    def circle(self):
        return 2 * pi * self.radius

    def pointStatuesOnCircle(self, pointP):
        sta = statues.PointCircleStatues()
        tmpLen = Line(self.center, pointP).length()
        if (tmpLen < self.radius):
            return sta.inCircle
        elif (tmpLen == self.radius):
            return sta.onCircle
        else:
            return sta.outCircle

    def lineStatuesCircle(self, lineC):
        try:
            centerTmp = self.center
            psta = statues.PointCircleStatues()
            lsta = statues.LineCircleStatues()
            lineA = Line(centerTmp, lineC.startPoint)
            lineB = Line(centerTmp, lineC.endPoint)
            q = (lineA.length() + lineB.length() + lineC.length()) / 2
            hC = 2 / lineC.length() * squareRoot(q * (q - lineA.length()) * (q - lineB.length()) * (q - lineC.length()))
            lcStaPointA = self.pointStatuesOnCircle(lineC.startPoint)
            lcStaPointB = self.pointStatuesOnCircle(lineC.endPoint)
            pointA = lineC.startPoint
            pointB = lineC.endPoint
            if (hC < self.radius):
                if ((lcStaPointA == psta.inCircle) and (lcStaPointB == psta.inCircle)):
                    return lsta.inCircle
                elif ((lcStaPointA == psta.inCircle) and (lcStaPointB == psta.outCircle)) or ((lcStaPointA == psta.outCircle) and (lcStaPointB == psta.inCircle)):
                    return lsta.drawCircle
                elif ((lcStaPointA == psta.outCircle) and (lcStaPointB == psta.outCircle)):
                    return lsta.crossCircle
                elif ((hC == 0) and (((pointA.x == centerTmp.x) and (pointA.y == centerTmp.y))) or ((pointB.x == centerTmp.x) and (pointB.y == centerTmp.y))):
                    return lsta.isRadius
                elif ((lcStaPointA == psta.onCircle) and (lcStaPointB == psta.onCircle)):
                    if (lineC.length() == self.radius):
                        return lsta.isDiameter
                    else:
                        return lsta.isChord
                else:
                    return lsta.statueError
            elif (hC == self.radius):
                if ((lcStaPointA == psta.onCircle) or (lcStaPointB == psta.onCircle)):
                    return lsta.cutCircle
                elif ((lcStaPointA == psta.outCircle) and (lcStaPointB == psta.outCircle)):
                    return lsta.cutCircle
                else:
                    return lsta.statueError
        except TypeError:
            print 'Line Type Error.'