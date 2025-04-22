from abc import ABC, abstractmethod


class Shape(ABC):
    """Абстрактный базовый класс для фигур."""

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры."""
        pass
