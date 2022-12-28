from tkinter import *
from tkinter import ttk

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
        self.output_expression = ""
        self.current_expression = ""
        
        self.display_frame = self.create_frame()
        self.output_label, self.current_label = self.create_display_label()

        self.buttons_frame = self.create_button_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

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
