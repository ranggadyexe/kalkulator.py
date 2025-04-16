import pytest
from app.calc import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_safe_eval_addition(calc):
    assert calc.safe_eval("2+3") == 5

def test_safe_eval_subtraction(calc):
    assert calc.safe_eval("10-4") == 6

def test_safe_eval_multiplication(calc):
    assert calc.safe_eval("3*3") == 9

def test_safe_eval_division(calc):
    assert calc.safe_eval("8/2") == 4

def test_square(calc):
    calc.current_expression = "5"
    calc.square()
    assert calc.current_expression == "25.0"

def test_sqrt(calc):
    calc.current_expression = "9"
    calc.sqrt()
    assert calc.current_expression == "3.0"
