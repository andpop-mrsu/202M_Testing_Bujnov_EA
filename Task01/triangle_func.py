class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
    """
    Определяет тип треугольника по длинам сторон.
    
    Примеры:
    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 3, 4)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(0, 0, 0)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Sides must be positive
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Sum of any two sides must be greater than the third
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Sides must be positive")
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise IncorrectTriangleSides("Sum of any two sides must be greater than the third")
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"