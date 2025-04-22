import math
from .base import Shape


class Circle(Shape):
    """Класс для расчёта площади круга."""

    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.radius: float = radius

    def area(self) -> float:
        """Возвращает площадь круга по формуле πr²."""
        return math.pi * self.radius**2
