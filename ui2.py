from tkinter import *
from tkinter import ttk
from button_functions import *

LIGHT_GREY = '#F5F5F5'
LABEL_COLOR = '#25265E'
WHITE = '#FFFFFF'
OFF_WHITE = '#F8FAFF'
LIGHT_BLUE = '#CCEDFF'

SMALL_FONT_SIZE = ('Arial', 16)
LARGE_FONT_SIZE = ('Arial', 40)
DIGIT_FONT_STYLE = ('Arial', 24, 'bold')
DEFAULT_FONT_STYLE = ('Arial', 20)

class window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('375x667')
        self.resizable(0, 0)
        self.title('CALCULATOR')

        self.output_expression = '0'
        self.current_expression = '0'
        
        self.display_frame = self.create_frame()
        self.output_label, self.current_label = self.create_display_label()

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }
        self.operations = {'/': '\u00F7',
                            '*': '\u00D7', '-': '-', '+': '+'}

        self.buttons_frame = self.create_button_frame()
        self.create_digit_btns()
        self.create_operator_btns()
        self.create_clear_btn()
        self.create_equals_btn()

    def create_frame(self):
        ui_frame = Frame(self, height=221, bg=LIGHT_GREY)
        ui_frame.pack(expand=True, fill="both")
        return ui_frame

    def create_button_frame(self):
        btns_frame = Frame(self)
        btns_frame.pack(expand=True, fill="both")
        return btns_frame

    def create_display_label(self):
        output_label = Label(self.display_frame, text=self.output_expression, anchor=E, 
                                bg=LIGHT_GREY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_SIZE)
        output_label.pack(expand=True, fill="both")

        current_label = Label(self.display_frame, text=self.current_expression, anchor=E, 
                                bg=LIGHT_GREY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_SIZE)
        current_label.pack(expand=True, fill="both")
        return  output_label, current_label

    def create_digit_btns(self):
        digits_dict = self.digits.items()
        for digit,grid_value in digits_dict:
            button = Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, 
                            font=DIGIT_FONT_STYLE, borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)

    def create_operator_btns(self):
        i = 0
        operator_dict = self.operations.items()
        for operator,symbol in operator_dict:
            button = Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, 
                            font=DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=i, column=4, sticky=NSEW)
            i+=1

    def create_clear_btn(self):
        button = Button(self.buttons_frame, text='C', bg=OFF_WHITE, fg=LABEL_COLOR, 
                            font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0, column=1, columnspan=3, sticky=NSEW)

    def create_equals_btn(self):
        button = Button(self.buttons_frame, text='=', bg=LIGHT_BLUE, fg=LABEL_COLOR, 
                            font=SMALL_FONT_SIZE , borderwidth=0)
        button.grid(row=4, column=3, columnspan=2, sticky=NSEW)


if __name__ == "__main__":
    app = window()
    app.mainloop()