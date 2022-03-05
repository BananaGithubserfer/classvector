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
        if isinstance(other, Vector):
#            print("vector")
            return Vector(
                start_x=self.start_x * other.start_x,
                start_y=self.start_y * other.start_y,
                end_x=self.end_x * other.end_x,
                end_y=self.end_y * other.end_y,
        )

        elif isinstance(other, int):
#            print("int")
            return Vector(
                start_x=self.start_x * other,
                start_y=self.start_y * other,
                end_x=self.end_x * other,
                end_y=self.end_y * other,
        )


    def __imul__(self, other):
        self.start_x *= other.start_x
        self.start_y *= other.start_y
        self.end_x *= other.end_x
        self.end_y *= other.end_y
        return self

    def __truediv__(self, other: int | Vector):
        return Vector(
            start_x=self.start_x / other.start_x,
            start_y=self.start_y / other.start_y,
            end_x=self.end_x / other.end_x,
            end_y=self.end_y / other.end_y,
        )

    def __idiv__(self, other):
        self.start_x /= other.start_x
        self.start_y /= other.start_y
        self.end_x /= other.end_x
        self.end_y /= other.end_y
        return self

    def __sub__(self, other: Vector) -> Vector:
        return self + -other
