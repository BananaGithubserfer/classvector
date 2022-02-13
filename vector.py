class Vector():
    def __init__(self, vecx, vecy):
        """give me y and x of 1st vector"""
        self._vecx = vecx
        self._vecy = vecy

    def getvec(self):
        """get vector"""
        return (self._vecx, self._vecy)

    def changevec(self, newvecx, newvecy):
        """give me new vector"""
        self._vecx = newvecx
        self._vecy = newvecy

    def __add__(self, other):
        """give me second vector"""
        return (self._vecx + other._vecx, self._vecy + other._vecy)

    def __sub__(self, other):
        """give me second vector"""
        return (self._vecx - other._vecx, self._vecy - other._vecy)

    def __mul__(self, num):
        """give me number to multiplication"""
        return ([self._vecx * num, self._vecy * num])

    def __truediv__(self, num):
        return(self._vecx // num, self._vecy // num)

    def __iadd__(self, other):
        """give me other vector"""
        self.vecx = self._vecx + other._vecx
        self.vecy = self._vecy + other._vecy

    def __isub__(self, other):
        """give me other vector"""
        self.vecx = self._vecx + -other._vecx
        self.vecy = self._vecy + -other._vecy

    def __imul__(self, num):
        """give me number"""
        self._vecx = self._vecx * num
        self._vecy = self._vecy * num

    def __idiv__(self, num):
        """give me a number"""
        self.vecx = self._vecx / num
        self.vecy = self._vecy / num

#x = Vector(22, 22)
#y = Vector(22, 22)

#print(x / 2)
