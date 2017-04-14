# coding=utf-8

from modules import statues as stX
from modules import point as pl
from modules import line as ll
from modules import circle as ce

def returnPoint():
    p = pl.Point(float(raw_input('x:')), float(raw_input('y:')))
    print 'Success for created a point.'
    return p

def returnLine(p1, p2):
    l = ll.Line(p1, p2)
    print 'Success for created a line.'
    return l

def returnCircle(center, radius):
    c = ce.Circle(center, radius)
    print 'Success for created a circle.'
    return c

print 'create a line:'
pa = returnPoint()
pb = returnPoint()
l1 = returnLine(pa, pb)
print 'l1 lenth = %f' % l1.length()
print 'create a circle:'
center = returnPoint()
ra = int(raw_input('Please input radius for circle:'))
c1 = returnCircle(center, ra)
stal = c1.lineStatuesCircle(l1)
print stal
