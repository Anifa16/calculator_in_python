import pytest

from calculator import add, divide, modulo, multiply, power, square_root, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(4, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(9, 3) == 0


def test_modulo_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot modulo by zero"):
        modulo(5, 0)


def test_square_root():
    assert square_root(9) == 3
    assert square_root(2.25) == 1.5


def test_square_root_negative_raises():
    with pytest.raises(ValueError, match="Cannot take square root of a negative number"):
        square_root(-1)
