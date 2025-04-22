import pytest
from shapes.triangle import Triangle


@pytest.mark.parametrize(
    "sides, expected_area, is_right",
    [((3, 4, 5), 6, True), ((2, 3, 4), pytest.approx(2.9047375), False)],
)
def test_triangle_properties(sides, expected_area, is_right) -> None:
    t = Triangle(*sides)
    assert pytest.approx(t.area(), rel=1e-6) == expected_area
    assert t.is_right() == is_right


def test_invalid_triangle() -> None:
    with pytest.raises(ValueError):
        Triangle(1, 1, 3)
