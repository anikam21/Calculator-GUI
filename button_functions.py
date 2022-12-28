from tkinter import *
from button_functions import calculatorButtons
from display_config import window

class buttonFunction(calculatorButtons):
    def __init__(self):
        super().__init__()
        self.current_expression = ""
        self.output_expression = ""

    def clear(self):
        self.current_expression = ""
        self.output_expression = ""

if __name__ == "__main__":
    button = buttonFunction()
    button.