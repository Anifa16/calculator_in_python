"""Tkinter GUI for the Python calculator."""

import tkinter as tk
from tkinter import ttk, messagebox

from calculator import add, subtract, multiply, divide, power, modulo, square_root


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calculator")
        self.geometry("360x240")
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        self.first_value = tk.StringVar()
        self.second_value = tk.StringVar()
        self.operation = tk.StringVar(value="+")
        self.result_value = tk.StringVar(value="Result will appear here")

        padding = {"padx": 10, "pady": 6}

        ttk.Label(self, text="First number:").grid(row=0, column=0, sticky="w", **padding)
        ttk.Entry(self, textvariable=self.first_value).grid(row=0, column=1, sticky="ew", **padding)

        ttk.Label(self, text="Second number:").grid(row=1, column=0, sticky="w", **padding)
        ttk.Entry(self, textvariable=self.second_value).grid(row=1, column=1, sticky="ew", **padding)

        ttk.Label(self, text="Operation:").grid(row=2, column=0, sticky="w", **padding)
        op_menu = ttk.Combobox(
            self,
            textvariable=self.operation,
            values=["+", "-", "*", "/", "^", "%", "√"],
            state="readonly",
            width=8,
        )
        op_menu.grid(row=2, column=1, sticky="w", **padding)

        ttk.Button(self, text="Calculate", command=self.calculate).grid(
            row=3, column=0, columnspan=2, sticky="ew", **padding
        )

        ttk.Label(self, textvariable=self.result_value, font=(None, 11, "bold")).grid(
            row=4, column=0, columnspan=2, sticky="ew", **padding
        )

        ttk.Button(self, text="Clear", command=self.clear_inputs).grid(
            row=5, column=0, columnspan=2, sticky="ew", **padding
        )

        self.columnconfigure(1, weight=1)

    def calculate(self):
        try:
            op = self.operation.get()
            first = float(self.first_value.get())
            if op == "√":
                result = square_root(first)
            else:
                second = float(self.second_value.get())
                if op == "+":
                    result = add(first, second)
                elif op == "-":
                    result = subtract(first, second)
                elif op == "*":
                    result = multiply(first, second)
                elif op == "/":
                    result = divide(first, second)
                elif op == "^":
                    result = power(first, second)
                elif op == "%":
                    result = modulo(first, second)
                else:
                    raise ValueError("Unsupported operation.")

            self.result_value.set(f"Result: {result}")
        except ValueError as exc:
            messagebox.showerror("Calculation error", str(exc))
        except Exception:
            messagebox.showerror("Calculation error", "Please enter valid numbers.")

    def clear_inputs(self):
        self.first_value.set("")
        self.second_value.set("")
        self.result_value.set("Result will appear here and you can check it too")


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
