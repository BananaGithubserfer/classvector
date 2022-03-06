from __future__ import annotations


class Vector:
    def __init__(self, start_x: float, start_y: float, end_x: float, end_y: float):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

    def __add__(self, other: Vector) -> Vector:
        """Сложили с другим вектор - вернули новый вектор"""
        return Vector(
            start_x=self.start_x + other.start_x,
            start_y=self.start_y + other.start_y,
            end_x=self.end_x + other.end_x,
            end_y=self.end_y + other.end_y,
        )

    def __iadd__(self, other: Vector) -> Vector:
        """Сложили с другим, вернули себя"""
        self.start_x += other.start_x
        self.start_y += other.start_y
        self.end_x += other.end_x
        self.end_y += other.end_y
        return self

    def __neg__(self) -> Vector:
        return Vector(-self.start_x, -self.start_y, -self.end_x, -self.end_y)

    def __str__(self):
        return f"({self.start_x}, {self.start_y}); ({self.end_x}, {self.end_y})"

    def __mul__(self, other: int | Vector):
        if isinstance(other, int):
            return Vector(
                start_x=self.start_x * other,
                start_y=self.start_y * other,
                end_x=self.end_x * other,
                end_y=self.end_y * other,
            )

        elif isinstance(other, Vector):
#            return Vector(
#            )
            raise Exception("not realized")
        else:
            raise Exception("bad type")



    def __imul__(self, other):
        if isinstance(other, int):
            self.start_x *= other
            self.start_y *= other
            self.end_x *= other
            self.end_y *= other
            return self
        elif isinstance(other, Vector):
            raise Exception("not realized")
        else:
            raise Exception("bad type")

    def __truediv__(self, other):
        if isinstance(other, int):
            return Vector(
                start_x=self.start_x / other,
                start_y=self.start_y / other,
                end_x=self.end_x / other,
                end_y=self.end_y / other,
            )

        elif isinstance(other, Vector):
            #            return Vector(
            #            )
            raise Exception("not realized")
        else:
            raise Exception("bad type")

    def __idiv__(self, other):
        if isinstance(other, int):
            self.start_x /= other
            self.start_y /= other
            self.end_x /= other
            self.end_y /= other
            return self
        elif isinstance(other, Vector):
            raise Exception("not realized")
        else:
            raise Exception("bad type")

    def __sub__(self, other):
        return self + -other

    def movevec(self, place):
        if isinstance(place, tuple):
           self.start_x = place(0)
           self.start_y = place(1)
           self.end_x = self.end_x - self.start_x + place(0)
           self.end_x = self.end_y - self.start_y + place(1)


        elif isinstance(place, Vector):
            self.start_x = place.end_x
            self.start_y = place.end_y
            self.end_x = self.end_x - self.start_x + place.end_x
            self.end_x = self.end_y - self.start_y + place.end_y
        else:
            raise Exception("bad type")