import tkinter as tk
from tkinter import ttk
from button_functions import *


class window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('CALCULATOR')
        self.geometry("312x324")
        self.resizable(0, 0)
        self.equation = tk.StringVar()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}
        ttk.Label(self, text='Name:').grid(column=0, row=0, **padding)

        # Entry
        expression_field = ttk.Entry(self, textvariable=self.equation)
        expression_field.grid(column=1, row=0, **padding)
        expression_field.focus()

        # Button
        seven_button = ttk.Button(self, text='7', command=self.calculator_buttons)
        seven_button.grid(column=2, row=0, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=1, columnspan=3, **padding)

    def submit(self):
        self.output_label.config(text=self.equation.get())

    def frame(self):
        buttons_frame = ttk.Frame(self, width= 312, height = 272.5, bg = 'grey')
        buttons_frame.pack()

    def calculator_buttons(self):
        seven = ttk.Button(self.frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, 
                            bg = "#fff", cursor = "hand2", command = lambda: click_button(7, self.equation)).grid(
                                row = 1, column = 0, padx = 1, pady = 1
                                ) 
        # clear = ttk.Button(self.frame, text = "Clear", fg = "black", width = 32, height = 3, bd = 0, 
        #                     bg = "#eee", cursor = "hand2", command = lambda: clear_button()).grid(
        #                         row = 0, column = 0, columnspan = 3, padx = 1, pady = 1
        #                         )
        # button1 =ttk.Button(self, text=' 1 ', fg='black', bg='red',
        #             command=lambda: click_button(1), height=1, width=7)


if __name__ == "__main__":
    app = window()
    app.mainloop()
        
