class Vector():
    def __init__(self, vec1):
    """give me 1st vector"""
        self.__vec = vec1

    def getvec(self):
        """get self.vector"""
        return (self.__vec)

    def changevec(self, newvec):
        """give me new vector"""
        self.__vec = newvec

    def sum(self, vec2):
        """give me second vector"""
        return([self.__vec[0] + vec2[0], self.__vec[1] + vec2[1]])

    def dif(self, vec2):
        """give me second vector"""
        return([self.__vec[0] + -vec2[0], self.__vec[1] + -vec2[1]])

    def mult(self, num):
        """give me number to multiplication"""
        return ([self.__vec[0]*num, self.__vec[1]*num])
