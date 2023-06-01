from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkinter import messagebox
from register import Register

class RegeneratePassword:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.root.title("REGENERATE PASSWORD")

        # setting favicona as logo of DRDO======================================================================
        self.root.iconbitmap(r"C:\Users\bansa\OneDrive\Pictures\drdo_icon.ico")

        # Creating frame ========================================================================
        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=800, height=500)

        # Heading Of LOGIN=========================================================================================
        heading_label = Label(frame,text="REGENERATE PASSWORD", font=("times new roman",15,"bold"),fg="black",bg="white")
        heading_label.place(x=270,y=140)

        # Labeling and inputs
        id_label = Label(frame,text="ID : ",font=("times new roman", 15, "bold"),bg="white")
        id_label.place(x=252, y=200)
        id_entry = ttk.Entry(frame,font=("times new roman", 15),width=20)
        id_entry.place(x=300, y=200)

        password_label = Label(frame,text="Old Password  : ",font=("times new roman", 15, "bold"),bg="white")
        password_label.place(x=152, y=250)
        password_entry = ttk.Entry(frame, font=("times new roman", 15), width=20)
        password_entry.place(x=300, y=250)

        newpassword_label = Label(frame, text="New Password   :", font=("times new roman", 15, "bold"), bg="white")
        newpassword_label.place(x=140, y=300)
        newpassword_entry = ttk.Entry(frame, font=("times new roman", 15), width=20)
        newpassword_entry.place(x=300, y=300)

        reenterpassword_label = Label(frame, text="Retype Password  : ", font=("times new roman", 15, "bold"), bg="white")
        reenterpassword_label.place(x=120, y=350)
        reenterpassword_entry = ttk.Entry(frame, font=("times new roman", 15), width=20)
        reenterpassword_entry.place(x=300, y=350)


        #Login button
        login_button = Button(frame,text="APPLY",font=("times new roman", 15, "bold"),bg="#000066",fg="white",activebackground="#000066",activeforeground="white")
        login_button.place(x=335,y=400)

if __name__=="__main__":
    root = Tk()
    app = RegeneratePassword(root)
    app.root.mainloop()