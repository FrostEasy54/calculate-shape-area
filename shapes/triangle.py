import math
from .base import Shape


class Triangle(Shape):
    """Класс для расчёта площади треугольника и проверки прямого угла."""

    def __init__(self, a: float, b: float, c: float):
        sides: list[float] = sorted((a, b, c))
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("С указанными сторонами нельзя составить треугольник")
        self.a, self.b, self.c = sides

    def area(self) -> float:
        """Вычисляет площадь по формуле Герона."""
        s: float = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        """Проверяет, является ли треугольник прямоугольным (с учётом погрешности)."""
        return math.isclose(self.a**2 + self.b**2, self.c**2)
