# coding=utf-8
import math
import os

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
            py = Point(self.x - q.x, self.y - q.x)
            return py
        except TypeError:
            print 'Point Type Error'