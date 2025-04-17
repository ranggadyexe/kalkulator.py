def safe_eval(expr):
    try:
        return str(eval(expr, {"__builtins__": {}}, {}))
    except Exception:
        return "Error"

def square(value):
    try:
        num = float(value)
        return str(num ** 2)
    except Exception:
        return "Error"

def sqrt(value):
    try:
        num = float(value)
        return str(num ** 0.5)
    except Exception:
        return "Error"
