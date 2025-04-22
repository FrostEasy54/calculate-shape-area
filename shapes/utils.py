from .base import Shape


def calculate_area(shape: Shape) -> float:
    """Общая функция для вычисления площади любой фигуры."""
    if not isinstance(shape, Shape):
        raise TypeError("Аргумент должен быть экземпляром Shape")
    return shape.area()
