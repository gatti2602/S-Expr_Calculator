import pytest
from Calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_passing_number_returns_number(calculator):
    assert calculator.resolve("1234") == 1234


def test_add(calculator):
    assert calculator.resolve("(add 1 2)") == 3


def test_multiply(calculator):
    assert calculator.resolve("(multiply 2 3)") == 6


def test_multiple_levels(calculator):
    assert calculator.resolve("(add 1 (multiply 2 3))" == 7)

