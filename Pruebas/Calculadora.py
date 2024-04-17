import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica")

        # Crear la pantalla de la calculadora
        self.display = tk.Entry(master, width=30, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

        # Crear los botones de la calculadora
        buttons = [
            'sin', 'cos', 'tan', 'log', 'ln', '√',
            '7', '8', '9', '/', 'C', 'CE',
            '4', '5', '6', '*', '(', ')',
            '1', '2', '3', '-', '^', '%',
            '0', '.', '+', '='
        ]
        row = 1
        col = 0
        for button in buttons:
            if button == '=':
                tk.Button(master, text=button, width=5, height=2, command=self.evaluate).grid(row=row, column=col, padx=5, pady=5)
            elif button == 'C':
                tk.Button(master, text=button, width=5, height=2, command=self.clear).grid(row=row, column=col, padx=5, pady=5)
            elif button == 'CE':
                tk.Button(master, text=button, width=5, height=2, command=self.clear_entry).grid(row=row, column=col, padx=5, pady=5)
            elif button == 'sin':
                tk.Button(master, text=button, width=5, height=2, command=lambda: self.add_to_display('math.sin(')).grid(row=row, column=col, padx=5, pady=5)
            elif button == 'cos':
                tk.Button(master, text=button, width=5, height=2, command=lambda: self.add_to_display('math.cos(')).grid(row=row, column=col, padx=5, pady=5)
            elif button == 'tan':
                tk.Button(master, text=button, width=5, height=2, command=lambda: self.add_to_display('math.tan(')).grid(row=row, column=col, padx=5, pady=5)
            else:
                tk.Button(master, text=button, width=5, height=2, command=lambda x=button: self.add_to_display(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 5:
                col = 0
                row += 1

    def add_to_display(self, value):
        self.display.insert(tk.END, value)

    def clear(self):
        self.display.delete(0, tk.END)

    def clear_entry(self):
        self.display.delete(len(self.display.get())-1, tk.END)

    def evaluate(self):
        try:
            expression = self.display.get()
            result = str(eval(expression))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

root = tk.Tk()
calculator = ScientificCalculator(root)
root.mainloop()