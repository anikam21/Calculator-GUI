from tkinter import *
from tkinter import ttk
from button_functions import *

class window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("312x324")
        self.resizable(0, 0)
        self.title('CALCULATOR')
        self.expression = StringVar()
        self.create_frame()
        self.create_widgets()
        self.calculator_btns()

    def create_frame(self):
        ui_frame = Frame(self, width=312, height=50, bd=0, highlightbackground="black", 
                            highlightcolor="red", highlightthickness=2)
        ui_frame.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

        btns_frame = Frame(self, width=312, height=272.5, bg="grey")
        btns_frame.grid()

    def create_widgets(self):
        padding = {'padx': 5,  'pady': 5}

        # Entry
        expression_field = ttk.Entry(self, textvariable=self.expression)
        expression_field.grid(column=1, row=0, **padding)
        expression_field.focus()

    def calculator_btns(btns_frame):
        padding = {'padx': 1,  'pady': 1}
        # first row
        clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, 
                            bd = 0, bg = "#eee", cursor = "hand2", command = lambda: clear_button())
        clear.grid(row = 0, column = 0, columnspan = 3, **padding)
        divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, 
                            bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("/"))
        divide.grid(row = 0, column = 3, **padding)

        # second row
        # seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, 
        #                     bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(7))
        # seven.grid(row = 1, column = 0, padx = 1, pady = 1)
        
        # eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, 
        #                     bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(8))
        # eight.grid(row = 1, column = 1, padx = 1, pady = 1)
        
        # nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, 
        #                     bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(9))
        # nine.grid(row = 1, column = 2, padx = 1, pady = 1)
        # multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, 
        #                     bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("*"))
        # multiply.grid(row = 1, column = 3, padx = 1, pady = 1)

        # # third row
        # four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, 
        #                 bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(4))
        # four.grid(row = 2, column = 0, padx = 1, pady = 1)
        
        # five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, 
        #                 bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(5))
        # five.grid(row = 2, column = 1, padx = 1, pady = 1)
        
        # six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, 
        #                 bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(6))
        # six.grid(row = 2, column = 2, padx = 1, pady = 1)
        
        # minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, 
        #                 bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("-"))
        # minus.grid(row = 2, column = 3, padx = 1, pady = 1)
        
        # # fourth row
        # one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, 
        #                 bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(1))
        # one.grid(row = 3, column = 0, padx = 1, pady = 1)
        
        # two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, 
        #                 bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(2))
        # two.grid(row = 3, column = 1, padx = 1, pady = 1)
        
        # three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, 
        #                 bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(3))
        # three.grid(row = 3, column = 2, padx = 1, pady = 1)
        
        # plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, 
        #                 bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("+"))
        # plus.grid(row = 3, column = 3, padx = 1, pady = 1)


if __name__ == "__main__":
    app = window()
    app.mainloop()