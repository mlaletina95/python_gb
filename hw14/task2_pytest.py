import pytest

from task2 import square_equation

def test_two_roots():
    assert square_equation(1, -7, 10) == [2.0, 5.0]


def test_one_root():
    assert square_equation(2, 0, 0) == 0.0


def test_no_roots():
    assert square_equation(1, 1, 1) is None


if __name__ == '__main__':
    pytest.main("-vv")