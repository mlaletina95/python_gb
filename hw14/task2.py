import doctest
import math


def square_equation(a: float, b: float, c: float):
    """
    >>> square_equation(1, -7, 10)
    [2.0, 5.0]

    >>> square_equation(2, 0, 0)
    0.0

    >>> square_equation(1, 1, 1) is None
    True
    """
    # ax^2 + bx + c = 0
    d = b * b - 4 * a * c
    if d < 0:
        return None

    if d == 0:
        return -b / (2 * a)

    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    return [x1, x2]


if __name__ == '__main__':
    doctest.testmod(verbose=True)