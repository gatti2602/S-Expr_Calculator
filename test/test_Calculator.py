import pytest
import Calculator


def test_passing_number_returns_number():
    assert Calculator.resolve("1234") == 1234


def test_add():
    assert Calculator.resolve("(add 1 2)") == 3


def test_multiply():
    assert Calculator.resolve("(multiply 2 3)") == 6


def test_multiple_levels():
    assert Calculator.resolve("(add 1 (multiply 2 3))") == 7
    assert Calculator.resolve("(multiply 3 (multiply (multiply 3 3) 3))") == 81
    assert Calculator.resolve("(multiply 2 (add (multiply 2 3) 8))") == 28


def test_multiple_params():
    assert Calculator.resolve("(add 1 2 3 4 (multiply 2 3 5))") == 40
