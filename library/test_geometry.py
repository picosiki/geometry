import pytest
from geometry.figures import Circle, Triangle


def test_circle_area():
    c = Circle(1)
    assert round(c.area(), 5) == 3.14159


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert round(t.area(), 5) == 6.0


def test_right_triangle():
    t = Triangle(3, 4, 5)
    assert t.is_right()


def test_invalid_circle():
    with pytest.raises(ValueError):
        Circle(0)


def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
