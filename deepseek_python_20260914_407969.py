import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("320x480")
        self.root.configure(bg="#1e1e1e")
        
        self.expression = ""
        
        # Дисплей
        self.display = tk.Entry(
            root,
            font=("Arial", 28),
            bg="#2d2d2d",
            fg="white",
            bd=0,
            justify="right",
            insertbackground="white"
        )
        self.display.pack(fill="both", ipadymy=20, padx=10, pady=10)
        
        # Кнопки
        buttons = [
            ["C", "±", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "⌫"]
        ]
        
        frame = tk.Frame(root, bg="#1e1e1e")
        frame.pack(expand=True, fill="both", padx=5, pady=5)
        
        for i, row in enumerate(buttons):
            frame.rowconfigure(i, weight=1)
            for j, btn_text in enumerate(row):
                frame.columnconfigure(j, weight=1)
                color = "#ff9500" if btn_text in ["/", "*", "-", "+", "="] else "#505050"
                if btn_text == "C":
                    color = "#d32f2f"
                
                btn = tk.Button(
                    frame,
                    text=btn_text,
                    font=("Arial", 18, "bold"),
                    bg=color,
                    fg="white",
                    bd=0,
                    activebackground="#666666",
                    command=lambda t=btn_text: self.on_click(t)
                )
                btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
    
    def on_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1]
        elif char == "=":
            try:
                # Безопасное вычисление
                result = eval(self.expression, {"__builtins__": None}, {})
                self.expression = str(result)
            except ZeroDivisionError:
                self.expression = "Деление на 0"
            except Exception:
                self.expression = "Ошибка"
        elif char == "±":
            if self.expression:
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
        elif char == "%":
            try:
                self.expression = str(eval(self.expression, {"__builtins__": None}, {}) / 100)
            except Exception:
                self.expression = "Ошибка"
        else:
            self.expression += char
        
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()