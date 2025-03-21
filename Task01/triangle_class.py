class IncorrectTriangleSides(Exception):
    pass

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides("Sides must be positive")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise IncorrectTriangleSides("Invalid triangle sides")
    
    def triangle_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        else:
            return "nonequilateral"
    
    def perimeter(self):
        return self.a + self.b + self.c