from display_config import window
from tkinter import *

LIGHT_GREY = '#F5F5F5'
LABEL_COLOR = '#25265E'
WHITE = '#FFFFFF'
OFF_WHITE = '#F8FAFF'
LIGHT_BLUE = '#CCEDFF'

SMALL_FONT_SIZE = ('Arial', 16)
LARGE_FONT_SIZE = ('Arial', 40)
DIGIT_FONT_STYLE = ('Arial', 24, 'bold')
DEFAULT_FONT_STYLE = ('Arial', 20)

class calculatorButtons(window):
    def __init__(self):
        super().__init__()
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }

        self.operations = {'/': '\u00F7',
                            '*': '\u00D7', '-': '-', '+': '+'}
        
        self.output_expression = ""
        self.current_expression = ""

        self.create_digit_btns()
        self.create_operator_btns()
        self.create_clear_btn()
        self.create_equals_btn()

    def create_digit_btns(self):
        digits_dict = self.digits.items()
        for digit,grid_value in digits_dict:
            button = Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, 
                            font=DIGIT_FONT_STYLE, borderwidth=0, 
                            command= lambda x=digit : self.update_digit_with_clicks(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)

    def create_operator_btns(self):
        i = 0
        operator_dict = self.operations.items()
        for operator,symbol in operator_dict:
            button = Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, 
                            font=DEFAULT_FONT_STYLE, borderwidth=0, 
                            command= lambda x=operator : self.update_operator(x))
            button.grid(row=i, column=4, sticky=NSEW)
            i+=1

    def create_clear_btn(self):
        button = Button(self.buttons_frame, text='C', bg=OFF_WHITE, fg=LABEL_COLOR, 
                            font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0, column=1, columnspan=3, sticky=NSEW)

    def create_equals_btn(self):
        button = Button(self.buttons_frame, text='=', bg=LIGHT_BLUE, fg=LABEL_COLOR, 
                            font=SMALL_FONT_SIZE, borderwidth=0)
        button.grid(row=4, column=3, columnspan=2, sticky=NSEW)

    def update_digit_with_clicks(self, value):
        self.current_expression += str(value)
        self.update_current_label()

    def update_operator(self, operator):
        self.current_expression += operator
        self.output_expression += self.current_expression
        self.current_expression = ""
        self.update_current_label()
        self.update_output_label()

    def update_output_label(self):
        self.output_label.config(text=self.output_expression)

    def update_current_label(self):
        self.current_label.config(text=self.current_expression)

if __name__ == "__main__":
    app = calculatorButtons()
    app.mainloop()