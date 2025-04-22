import pytest
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.utils import calculate_area


def test_calculate_area_circle() -> None:
    c = Circle(3)
    assert calculate_area(c) == c.area()


def test_calculate_area_triangle() -> None:
    t = Triangle(3, 4, 5)
    assert calculate_area(t) == t.area()


def test_calculate_area_invalid() -> None:
    with pytest.raises(TypeError):
        calculate_area(123)
