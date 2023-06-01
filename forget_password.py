from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkinter import messagebox
from register import Register
from regeneratepassword import RegeneratePassword
from switchpage import Ft
import mysql.connector

class Forget_password:
    def __init__(self,root):
        self.root=root
        self.root.title(" Forgot Password")
        self.root.geometry("800x500")

        # setting favicona as logo of DRDO======================================================================
        self.root.iconbitmap(r"C:\Users\bansa\OneDrive\Pictures\drdo_icon.ico")

        # Creating frame ========================================================================
        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=800, height=500)

        global my_img
        my_img = Image.open("C:/Users/bansa/OneDrive/Pictures/drdo_white.jpg")
        my_img = my_img.resize((150, 150))
        my_img = ImageTk.PhotoImage(my_img)
        my_img_label = Label(frame, image=my_img, bd=0, borderwidth=0, border=0)
        my_img_label.place(x=310, y=5)

        # Row 4
        security_label = Label(frame, text="Select security question", font=("times new roman", 15, "bold"),
                               bg="lightgrey")
        security_label.place(x=30, y=280)
        combo_sec_label = Combobox(frame, font=("times new roman", 15, "bold"), state="readonly",
                                   textvariable=self.var_sequrityq)
        combo_sec_label["values"] = ("Select", "Your birth place", "your school name")
        combo_sec_label.place(x=30, y=310, width=250)
        combo_sec_label.current(0)
        # security_entry = Entry(frame, font=("times new roman", 15, "bold"), bg="white")
        # security_entry.place(x=30, y=310, width=250)

        Sec_ans_label = Label(frame, text="Security answer", font=("times new roman", 15, "bold"), bg="lightgrey")
        Sec_ans_label.place(x=300, y=280)
        Sec_ans_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.var_securitya)
        Sec_ans_entry.place(x=300, y=310, width=250)


if __name__=="__main__":
    root  = Tk()
    app = Forget_password(root)
    app.root.mainloop()