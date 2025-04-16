# app/logic.py

class CalculatorLogic:
    def safe_eval(self, expression):
        try:
            return eval(expression, {"__builtins__": None}, {})
        except Exception:
            return "Error"
