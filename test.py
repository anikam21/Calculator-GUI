# import tkinter as tk

# root = tk.Tk()

# test = tk.Label(root, text="red", bg="red", fg="white")
# test.pack(padx=5, pady=15, side=tk.LEFT)
# test = tk.Label(root, text="green", bg="green", fg="white")
# test.pack(padx=5, pady=20, side=tk.LEFT)
# test = tk.Label(root, text="purple", bg="purple", fg="white")
# test.pack(padx=5, pady=20, side=tk.LEFT)

# root.mainloop()

from tkinter import *
root = Tk()

Label(text="Position 1", width=10).grid(row=0, column=0)
Label(text="Position 2", width=10).grid(row=0, column=1)
Label(text="Position 3", width=10).grid(row=1, column=0)
Label(text="Position 4", width=10).grid(row=1, column=1)
root.mainloop()