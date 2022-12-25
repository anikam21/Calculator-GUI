from tkinter import *
from tkinter import  ttk

expression = ""
# equation = StringVar()

def click_button(num, equation):
    """Function to click calculator buttons"""
    global expression 
    expression  = expression  + str(num)
    equation.set(expression)


def equalpress(equation):
    """Function to output the answer"""
    try:
        global expression 
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("ERROR")
        expression = ""

# Function to clear the contents
# of text entry box
def clear_button(equation):
    global expression
    expression = ""
    equation.set("")
    
# def configure_gui(gui):
#     """GUI settings"""
#     frame_buttons = ttk.Frame(gui, padding=270)
#     frame_buttons.grid()
#     ttk.Label(frame_buttons).grid(column=0, row=0)
#     ttk.Button(frame_buttons, text="Quit", command=gui.destroy).grid(column=0, row=0)
#     gui.configure(background="light grey")
#     gui.title("Calculator")
#     gui.geometry("270x270")
#     gui.mainloop()

# click_button(7) 