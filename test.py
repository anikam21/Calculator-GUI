import tkinter as tk

root = tk.Tk()
root.geometry("312x324")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

padding = {'padx': 0,  'pady': 0}
clear = tk.Button(root, text='Clear', command=lambda:print("Click"))
clear.config(height=2, width=30)
clear.grid(sticky='NW')

# divide = tk.Button(root, text='/', command=lambda:print("/"))
# clear.config(height=2, width=20)
# clear.grid(sticky='NE')

Label = tk.Label(root, text="Text")
Label.grid(row=1, column=2)

# for widget in root.winfo_children():
#     print(f"{widget.widgetName}:({ widget.grid_info()['row']}, {widget.grid_info()['column']})")

root.mainloop()