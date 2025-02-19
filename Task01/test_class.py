import pytest
from triangle_class import Triangle, IncorrectTriangleSides

def test_equilateral():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == 'equilateral'
    assert t.perimeter() == 9

def test_isosceles():
    t = Triangle(3, 3, 4)
    assert t.triangle_type() == 'isosceles'
    assert t.perimeter() == 10

def test_invalid_sides():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 3)

def test_perimeter():
    t = Triangle(5, 5, 5)
    assert t.perimeter() == 15