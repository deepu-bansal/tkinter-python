from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkinter import messagebox
from register import Register
from regeneratepassword import RegeneratePassword
from switchpage import Ft
import mysql.connector

root = Tk()
# lion = StringVar()
chec = StringVar()
passwd = Entry(textvariable=chec)
passwd.place(x=2, y=2)
lion = chec.get()
print(lion)


def troll():
    # lion = chec.get() + "deep"
    print(lion)


def func():
    troll()


btn = Button(text="click", command=func)
btn.place(x=10, y=100)

root.mainloop()
