from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector

class User:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x600")
        self.root.title(" User Window")




if __name__=="__main__":
    root = Tk()
    app = User(root)
    app.root.mainloop()



from getpass import getpass
password = getpass()
print(password)
