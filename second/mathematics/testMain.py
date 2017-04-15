# coding=utf-8

from modules import statues as stX
from modules import point as pl
from modules import line as ll
from modules import circle as ce

def returnPoint():
    inputX, inputY = (raw_input('X:'), raw_input('Y:'))
    flagx, flagy = (inputJudge(inputX), inputJudge(inputY))
    if (flagx and flagy):
        p = pl.Point(float(inputX), float(inputY))
        print 'Success for created a PLC point.'
        return p
    else:
        print 'Create point failed, Please input correct value for location.'
        returnPoint()

def returnPCPoint(ra, an, anM):
    try:
        p = returnPoint()
        print 'Success for created a PLC point.'
        tmpP = p.establishPolarCoordinatePoint(ra, an, anM)
        return tmpP
    except TypeError:
        print 'Create point failed, Please input correct value for PC.'

def returnPRCLine(p1, p2):
    l = ll.Line(p1, p2)
    print 'Success for created a line.'
    return l

def returnPCLine(p1, length, angleMode, angle):
    try:
        l = ll.Line.establishPolarCoordinateLine(p1, length, angleMode, angle)
        print 'Success for created a PC line.'
        return l
    except ValueError:
        print 'Please input correct value for line.'

def returnCircle(center, radius):
    c = ce.Circle(center, radius)
    print 'Success for created a circle.'
    return c

def inputJudge(value):
    if (value != '' and value != '\n' and value != '\0'):
        return True
    else:
        return False

print 'create a line:'
pa = returnPoint()
pb = returnPoint()
l1 = returnPRCLine(pa, pb)
# print l1.angle
# print 'l1 lenth = %f' % l1.length
print 'create a circle:'
center = returnPoint()
ra = float(raw_input('Please input radius for circle:'))
c1 = returnCircle(center, ra)
hc = c1.returnHeightOnC(l1)
print 'hc = %f, radius = %f, l1angle = %f' % (hc, c1.radius, l1.angle)
stal = c1.lineStatuesCircle(l1)
print stX.lineStatuesDic[stal]

# print 'Create a PCPoint:'
# prcp = returnPoint()
# pcp = prcp.establishPolarCoordinatePoint(float(raw_input('Radius for PCP:')), raw_input('Angle mode input \'a\' or \'r\''), float(raw_input('Angle for round:')))
# print prcp.x, prcp.y, pcp.x, pcp.y
#
# print 'Create a PCLine:'
# lx = returnPCLine(prcp, float(raw_input('Radius for PCL:')), raw_input('Angle mode input \'a\' or \'r\''), float(raw_input('Angle for round:')))
# print lx.length, lx.angle, lx.endPoint.x, lx.endPoint.y

