import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleFunction(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(3, 3, 3), 'equilateral')
    
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(3, 3, 4), 'isosceles')
    
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), 'nonequilateral')
    
    def test_invalid_sides_negative(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 2)
    
    def test_invalid_sides_sum(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 3)

if __name__ == '__main__':
    unittest.main()