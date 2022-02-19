class Vector():
    def __init__(self, vecx, vecy):
        """give me y and x of 1st vector"""
        self.vecx = vecx
        self.vecy = vecy

    def getvec(self):
        """get vector"""
        return self.vecx, self.vecy

    def changevec(self, newvecx, newvecy):
        """give me new vector"""
        self.vecx = newvecx
        self.vecy = newvecy

    def __add__(self, other):
        """give me second vector"""
        return self.vecx + other.vecx, self.vecy + other.vecy

    def __sub__(self, other):
        """give me second vector"""
        return self.vecx - other.vecx, self.vecy - other.vecy

    def __mul__(self, num):
        """give me number to multiplication"""
        return self.vecx * num, self.vecy * num

    def __truediv__(self, num):
        return self.vecx // num, self.vecy // num

    def __iadd__(self, other):
        """give me other vector"""
        self.vecx = self.vecx + other.vecx
        self.vecy = self.vecy + other.vecy
        return self

    def __isub__(self, other):
        """give me other vector"""
        self.vecx = self.vecx - other.vecx
        self.vecy = self.vecy - other.vecy
        return self


    def __imul__(self, num):
        """give me number"""
        self.vecx = self.vecx * num
        self.vecy = self.vecy * num
        return self

    def __idiv__(self, num):
        """give me number"""
#        print(self._vecy)
#        print(self._vecx)
        self.vecx = self.vecx / num
        self.vecy = self.vecy / num
        return self


#print(x.getvec())

#y+=y
#x = Vector(11, 11)
#y = Vector(11, 11)

#x-=y
#print(x)
