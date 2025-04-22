import pytest
import math
from shapes.circle import Circle


@pytest.mark.parametrize(
    "radius, expected", [(0, 0), (1, math.pi), (2.5, math.pi * 2.5**2)]
)
def test_area(radius, expected) -> None:
    c = Circle(radius)
    assert pytest.approx(c.area(), rel=1e-9) == expected


def test_negative_radius() -> None:
    with pytest.raises(ValueError):
        Circle(-1)
