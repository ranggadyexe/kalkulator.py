# app/logic.py

import math

def safe_eval(expression):
    try:
        return eval(expression)
    except Exception:
        return 0

def square(x):
    try:
        return float(x) ** 2
    except Exception:
        return 0

def sqrt(x):
    try:
        return math.sqrt(float(x))
    except Exception:
        return 0
