import unittest
from task2 import square_equation



class TestSquareEquation(unittest.TestCase):

    def test_two_roots(self):
        self.assertEqual(square_equation(1, -7, 10), [2.0, 5.0])

    def test_one_root(self):
        self.assertEqual(square_equation(2, 0, 0), 0.0)

    def test_no_roots(self):
        self.assertIsNone(square_equation(1, 1, 1))


if __name__ == '__main__':
    unittest.main("-vv")