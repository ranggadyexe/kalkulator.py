# tests/test_calc.py

from app.logic import safe_eval, square, sqrt

def test_safe_eval_addition():
    assert safe_eval("2 + 3") == 5

def test_safe_eval_subtraction():
    assert safe_eval("10 - 4") == 6

def test_safe_eval_multiplication():
    assert safe_eval("3 * 4") == 12

def test_safe_eval_division():
    assert safe_eval("8 / 2") == 4.0

def test_square():
    assert square("5") == 25.0

def test_sqrt():
    assert sqrt("9") == 3.0
