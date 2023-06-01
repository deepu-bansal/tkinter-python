from tkinter import *
from tkinter import ttk

root = Tk()


def create_new():
    global window
    window = Toplevel()


def close_new():
    window.destroy()


btn_open = ttk.Button(text="open a new window", command=create_new)
btn_open.pack()
btn_close = ttk.Button(text="Close a new window", command=close_new)
btn_close.pack()

root.mainloop()
