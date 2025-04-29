import math
from .interfaces import Shape
from .utils import is_right_triangle


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        sides = sorted([a, b, c])
        if any(side <= 0 for side in sides):
            raise ValueError("Sides must be positive")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Invalid triangle sides")
        self.a, self.b, self.c = sides

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        return is_right_triangle(self.a, self.b, self.c)
