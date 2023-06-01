from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from getpass import getpass
from PIL import ImageTk, Image
from tkinter import messagebox
from register import Register
from forgot_password import Forgot_password
from switchpage import Ft
import mysql.connector

def open_user():
    window = Toplevel()
    new = Ft(window)
def open_register():
    window = Toplevel()
    new = Register(window)


def open_forgotpassword():
    window = Toplevel()
    new = Forgot_password(window)


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.root.title("LOGIN WINDOW")

        # setting favicona as logo of DRDO======================================================================
        self.root.iconbitmap(r"C:\Users\bansa\OneDrive\Pictures\drdo_icon.ico")

        # Creating frame ========================================================================
        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=800, height=500)

        # Setting Drdo image at the top
        global my_img
        my_img = Image.open("C:/Users/bansa/OneDrive/Pictures/drdo_white.jpg")
        my_img = my_img.resize((150, 150))
        my_img = ImageTk.PhotoImage(my_img)
        my_img_label = Label(frame, image=my_img, bd=0, borderwidth=0, border=0)
        my_img_label.place(x=310, y=5)

        # Heading Of LOGIN=========================================================================================
        heading_label = Label(frame, text="LOGIN HERE", font=("times new roman", 15, "bold"), fg="#000066", bg="white")
        heading_label.place(x=320, y=170)

        getid = StringVar()
        getpass = StringVar()

        # Labeling and inputs
        id_label = Label(frame, text="USER ID : ", font=("times new roman", 15, "bold"), bg="white")
        id_label.place(x=194, y=250)
        id_entry = ttk.Entry(frame, font=("times new roman", 15), width=20, textvariable=getid )
        id_entry.place(x=300, y=250)

        password_label = Label(frame, text="PASSWORD : ", font=("times new roman", 15, "bold"), bg="white")
        password_label.place(x=159, y=300)
        password_entry = ttk.Entry(frame, font=("times new roman", 15), width=20, textvariable=getpass,show='*')
        password_entry.place(x=300, y=300)


        def show_passwd():
            if password_entry.cget('show')=='*':
                password_entry.config(show='')
            else:
                password_entry.config(show='*')

        checkbutton = Checkbutton(frame, text="Show Password",font=("times new roman", 12, "bold"), bg="white",fg="black", onvalue=1,
                                  offvalue=0,command=show_passwd)
        checkbutton.place(x=520, y=302)



        def login():

                conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="my_data")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register_table where userid=%s and password=%s", (
                    getid.get(),
                    getpass.get()
                ))
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("ERROR", "Userid and password do not match. Please input the correct data.")
                else:
                    getid.set("")
                    getpass.set("")
                    messagebox.showinfo(" Welcome ", "Welocme to our portal")
                    open_user()


        # Login button
        login_button = Button(frame, text="LOGIN", font=("times new roman", 15, "bold"), bg="#000066", fg="white",
                              activebackground="#000066", activeforeground="white", command=login)
        login_button.place(x=335, y=350)

        # Button to register
        btn = Button(text="Register", bg="orange", bd=0, fg="white", font=( "times new roman",15,"bold"),
                     activebackground="white", activeforeground="blue", command=open_register)
        btn.place(x=250, y=400)
        # forgot password
        btn = Button(text="Forgot Password", bg="orange", bd=0, fg="white", font=( "times new roman",15,"bold"),
                     activebackground="white", activeforeground="blue", command=open_forgotpassword)
        btn.place(x=350, y=400)


if __name__ == "__main__":
    root = Tk()
    app = Login(root)

    app.root.mainloop()
