from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp

Window.clearcolor = (0.95, 0.95, 0.95, 1)


class Calculator(App):

    def build(self):
        self.title = "Calculator"

        root = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        self.display = TextInput(
            text="0",
            readonly=True,
            multiline=False,
            halign="right",
            font_size=dp(38),
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=(0.2, 0.2, 0.2, 1),
            padding=[dp(10), dp(18)]
        )

        root.add_widget(self.display)

        buttons = [
            ["C", "⌫", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", ""]
        ]

        grid = GridLayout(
            cols=4,
            spacing=dp(8),
            size_hint_y=0.75
        )

        for row in buttons:
            for text in row:
                if text == "":
                    grid.add_widget(BoxLayout())
                    continue

                button = Button(
                    text=text,
                    font_size=dp(25),
                    background_normal="",
                    background_color=(1, 1, 1, 1),
                    color=(0.1, 0.1, 0.1, 1)
                )

                button.bind(on_press=self.button_pressed)
                grid.add_widget(button)

        root.add_widget(grid)

        return root

    def button_pressed(self, instance):
        value = instance.text
        current = self.display.text

        if value == "C":
            self.display.text = "0"

        elif value == "⌫":
            self.display.text = current[:-1] or "0"

        elif value == "=":
            try:
                expression = current
                expression = expression.replace("×", "*")
                expression = expression.replace("÷", "/")
                expression = expression.replace("−", "-")
                expression = expression.replace("%", "/100")

                result = eval(expression, {"__builtins__": None}, {})

                if isinstance(result, float) and result.is_integer():
                    result = int(result)

                self.display.text = str(result)

            except Exception:
                self.display.text = "Error"

        else:
            if current == "0" or current == "Error":
                self.display.text = value
            else:
                self.display.text += value


if __name__ == "__main__":
    Calculator().run()