class Vector():
    def __init__(self, startx, starty, endx, endy):
        """give me y and x of 1st vector"""
        self.start = (startx, starty)
        self.end = (endx, endy)

    def getstart(self):
        """get vector"""
        return self.start

    def getend(self):
        return self.end

    def changevec(self, startx, starty, endx, endy):
        """give me new vector"""
        self.start = (startx, starty)
        self.end = (endx, endy)

    def __add__(self, other):
        """give me second vector"""
        return self.start[0], self.start[1], self.end[0] + other.end[0], self.end[1] + other.end[1]

    def __sub__(self, other):
        """give me second vector"""
        return self.start[0], self.start[1], self.end[0] - other.end[0], self.end[1] - other.end[1]

    def __mul__(self, num):
        """give me number to multiplication"""
        return self.start[0], self.start[1], self.end[0] * num, self.end[0] * num

    def __truediv__(self, num):
        return self.start[0], self.start[1], self.end[0] // num, self.end[1] // num

    def __iadd__(self, other):
        """give me other vector"""
        self.end = (self.end[0] + other.end[0], self.end[1] + other.end[1])
        return self

    def __isub__(self, other):
        """give me other vector"""
        self.end = (self.end[0] - other.end[0], self.end[1] - other.end[1])
        return self

    def __imul__(self, num):
        """give me number"""
        self.end = (self.end[0] * num, self.end[1] * num)
        return self

    def __itruediv__(self, num):
        """give me number"""
        self.end = (self.end[0] / num, self.end[1] / num)
        return self
