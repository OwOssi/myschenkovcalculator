from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        
        # Основной контейнер
        layout = GridLayout(cols=1, spacing=5, padding=10)
        
        # Дисплей
        self.display = Label(
            text="0",
            font_size=50,
            size_hint_y=0.3,
            color=(1, 1, 1, 1)
        )
        layout.add_widget(self.display)
        
        # Сетка кнопок
        buttons_grid = GridLayout(cols=4, spacing=5)
        
        buttons = [
            ["C", "±", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "⌫"]
        ]
        
        for row in buttons:
            for text in row:
                btn = Button(
                    text=text,
                    font_size=24,
                    background_color=self.get_color(text)
                )
                btn.bind(on_press=self.on_button_press)
                buttons_grid.add_widget(btn)
        
        layout.add_widget(buttons_grid)
        return layout
    
    def get_color(self, text):
        if text in ["/", "*", "-", "+", "="]:
            return (1, 0.58, 0, 1)  # Оранжевый
        elif text == "C":
            return (0.83, 0.18, 0.18, 1)  # Красный
        return (0.31, 0.31, 0.31, 1)  # Серый
    
    def on_button_press(self, instance):
        text = instance.text
        
        if text == "C":
            self.expression = ""
        elif text == "⌫":
            self.expression = self.expression[:-1]
        elif text == "=":
            try:
                result = eval(self.expression, {"__builtins__": None}, {})
                self.expression = str(result)
            except ZeroDivisionError:
                self.expression = "Деление на 0"
            except:
                self.expression = "Ошибка"
        elif text == "±":
            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            else:
                self.expression = "-" + self.expression
        elif text == "%":
            try:
                self.expression = str(eval(self.expression, {"__builtins__": None}, {}) / 100)
            except:
                self.expression = "Ошибка"
        else:
            self.expression += text
        
        self.display.text = self.expression if self.expression else "0"

if __name__ == "__main__":
    CalculatorApp().run()