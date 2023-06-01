from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from getpass import getpass
from PIL import ImageTk, Image
from tkinter import messagebox
from register import Register
from regeneratepassword import RegeneratePassword
from switchpage import Ft
import mysql.connector

class Forgot_password:
    def __init__(self, root):
        self.root = root
        self.root.title(" Forgot Password")
        self.root.geometry("800x500")

        # setting favicona as logo of DRDO======================================================================
        self.root.iconbitmap(r"C:\Users\bansa\OneDrive\Pictures\drdo_icon.ico")

        # Creating frame ========================================================================
        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=800, height=500)

        # =====================================================================================

        global my_img
        my_img = Image.open("C:/Users/bansa/OneDrive/Pictures/drdo_white.jpg")
        my_img = my_img.resize((150, 150))
        my_img = ImageTk.PhotoImage(my_img)
        my_img_label = Label(frame, image=my_img, bd=0, borderwidth=0, border=0)
        my_img_label.place(x=310, y=5)


        label_userid = Label(frame,text="User Id : ",font=("times new roman", 15), width=20,bg="white")
        label_userid.place(x=150,y=190)
        entry_userid = ttk.Entry(frame, font=("times new roman", 15), width=20)
        entry_userid.place(x=300, y=190)

        label_question = Label(frame, text="One Word Question : ", font=("times new roman", 15), width=20, bg="white")
        label_question.place(x=100, y=230)
        entry_question = ttk.Entry(frame, font=("times new roman", 15), width=20)
        entry_question.place(x=300, y=230)

        label_answer = Label(frame,text="One Word Answer :",font=("times new roman", 15), width=20,bg="white")
        label_answer.place(x=100,y=270)
        entry_answer = ttk.Entry(frame, font=("times new roman", 15), width=20)
        entry_answer.place(x=300, y=270)

        label_email = Label(frame, text="Email :", font=("times new roman", 15), width=20, bg="white")
        label_email.place(x=149,y=310)
        entry_email = ttk.Entry(frame, font=("times new roman", 15), width=20)
        entry_email.place(x=300, y=310)

        def find_passwd():
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="my_data")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register_table where userid=%s and securityq=%s and securitya=%s and email=%s", (
                entry_userid.get(),
                entry_question.get(),
                entry_answer.get(),
                entry_email.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("ERROR", "Userid and password do not match. Please input the correct data.")
            else:
                # getid.set("")
                # getpass.set("")
                messagebox.showinfo(" Welcome ", "Your password is : " + row[6])
                # open_user()

        button_sendmail = Button(frame, text="OKAY", font=("times new roman", 15, "bold"), bg="#000066", fg="white",
                              activebackground="#000066", activeforeground="white",command=find_passwd)
        button_sendmail.place(x=335, y=350)














if __name__ == "__main__":
    root = Tk()
    app = Forgot_password(root)
    app.root.mainloop()