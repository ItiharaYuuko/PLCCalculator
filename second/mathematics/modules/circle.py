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
            if (radius):
                raise ValueError('Circles radius should not equal to 0')
        except TypeError:
            print 'Point type error or radius type error.'

    def square(self):
        return pi * pow(self.radius, 2)

    def circle(self):
        return 2 * pi * self.radius

    def pointStatuesOnCircle(self, pointP):
        try:
            sta = statues.PointCircleStatues()
            tmpLen = Line(self.center, pointP).length
            if (tmpLen < self.radius):
                return sta.inCircle
            elif (tmpLen == self.radius):
                return sta.onCircle
            else:
                return sta.outCircle
        except TypeError:
            print 'Point type error.'

    def returnHeightOnC(self, lineC):
        try:
            centerTmp = self.center
            lineA = Line(centerTmp, lineC.startPoint)
            lineB = Line(centerTmp, lineC.endPoint)
            q = (lineA.length + lineB.length + lineC.length) / 2
            hC = 2 / lineC.length * squareRoot(q * (q - lineA.length) * (q - lineB.length) * (q - lineC.length))
            return hC
        except TypeError:
            print 'Please inject a correct line type.'

    def lineStatuesCircle(self, lineC):
        try:
            psta = statues.PointCircleStatues()
            lsta = statues.LineCircleStatues()
            hC = self.returnHeightOnC(lineC)
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
                elif ((hC == 0) and (((pointA.x == self.center.x) and (pointA.y == self.center.y))) or ((pointB.x == self.center.x) and (pointB.y == self.center.y))):
                    return lsta.isRadius
                elif ((lcStaPointA == psta.onCircle) and (lcStaPointB == psta.onCircle)):
                    if (lineC.length == self.radius):
                        return lsta.isDiameter
                    else:
                        return lsta.isChord
                else:
                    return lsta.statueError
            elif (hC == self.radius):
                if ((lcStaPointA == psta.onCircle) or (lcStaPointB == psta.onCircle)):
                    return lsta.cutCircle
                elif ((lcStaPointA == psta.outCircle) and (lcStaPointB == psta.outCircle)):
                    onCircleCount = 0
                    includePointRangeX = range(int(pointB.x - pointA.x))
                    includePointRangeY = range(int(pointB.y - pointA.y))
                    # for (x, y) in (includePointRangeX, includePointRangeY):
                    #     print (x, y)
                    #     tmpPoint = Point(x,y)
                    #     if (self.pointStatuesOnCircle(tmpPoint) == psta.onCircle):
                    #         onCircleCount += 1
                    #     else:
                    #         continue
                    print includePointRangeX
                    if (onCircleCount == 1):
                        return lsta.cutCircle
                    else:
                        return lsta.statueError
                else:
                    return lsta.statueError
            else:
                return lsta.overCircle
        except TypeError:
            print 'Line Type Error.'