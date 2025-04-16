# app/calc.py

import tkinter as tk
from app.logic import CalculatorLogic

class CalculatorGUI:
    def __init__(self):
        self.logic = CalculatorLogic()
        self.window = tk.Tk()
        self.window.title("Kalkulator")
        
        self.entry = tk.Entry(self.window, width=40, borderwidth=5, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self._create_buttons()

        self.window.mainloop()

    def _create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            if text == '=':
                command = self.calculate
            else:
                command = lambda char=text: self.entry.insert(tk.END, char)
            tk.Button(self.window, text=text, width=9, height=2, command=command).grid(row=row, column=col)

        tk.Button(self.window, text='C', width=9, height=2, command=self.clear).grid(row=5, column=0, columnspan=4)

    def calculate(self):
        expression = self.entry.get()
        result = self.logic.safe_eval(expression)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(result))

    def clear(self):
        self.entry.delete(0, tk.END)

# Untuk menjalankan GUI langsung
if __name__ == '__main__':
    CalculatorGUI()
