import math

def safe_eval(expr):
    try:
        return eval(expr, {"__builtins__": None, "sqrt": math.sqrt})
    except:
        return "Error"

def square(x):
    try:
        return float(x) ** 2
    except:
        return "Error"

def sqrt(x):
    try:
        return math.sqrt(float(x))
    except:
        return "Error"
