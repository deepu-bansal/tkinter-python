from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1000x600")

        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=1000, height=600)

        # ==============================================================================================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_sequrityq = StringVar()
        self.var_securitya = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        check_1 = IntVar()

        def register():
            passwd = password_entry.get()
            flag1 = flag2 = flag3 = flag4 = 0
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','@']
            cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

            for i in passwd:
                if i in numbers:
                    flag1 = 1
                if i in symbols:
                    flag2 = 1
                if i in cap_letters:
                    flag3 = 1
                if i in small_letters:
                    flag4 = 1

            flag_user = 0
            for i in userid_entry.get():
                if i in symbols:
                    flag_user = 1

            if (email_entry.get() == "" or fname_entry.get() == ""):
                messagebox.showerror("ERROR", "Please input all the data")
            elif (flag_user == 0 or len(userid_entry.get()) < 7):
                messagebox.showerror(" OOPS", "User ID must contain one symbol and have atleast a length of SEVEN")
            elif (len(contact_entry.get()) != 10):
                messagebox.showerror("ERROR", "Please ensure you have contact no. of ten digits")
            elif (len(passwd) < 8 or flag1 != 1 or flag2 != 1 or flag3 != 1 or flag4 != 1):
                messagebox.showerror("ERROR","Password should have alteast a length of 8 and must contain a number, smallcase letter, capitalcase letter and a symbol")
            elif (password_entry.get() != confirm_password_entry.get()):
                messagebox.showerror("ERROR", "Please type the same password while confirmation")
            # elif (check_1.get() == 0):
            #     messagebox.showerror("ERROR", "Please accept the terms and conditions")
            else:
                conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="my_data")
                my_cursor = conn.cursor()
                query = "select * from register_table where email=%s"
                value = (email_entry.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("ERROR", "User already exist")
                else:
                    my_cursor.execute("insert into register_table values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                      (fname_entry.get(),
                                       lname_entry.get(),
                                       contact_entry.get(),
                                       email_entry.get(),
                                       security_entry.get(),
                                       sec_ans_entry.get(),
                                       password_entry.get(),
                                       userid_entry.get()

                                       ))
                conn.commit()
                conn.close()
                messagebox.showinfo("success", "Registered successfully")
                # self.root.destroy()
        #
        # setting favicona as logo of DRDO======================================================================
        self.root.iconbitmap(r"C:\Users\bansa\OneDrive\Pictures\drdo_icon.ico")

        global my_img
        my_img = Image.open("C:/Users/bansa/OneDrive/Pictures/drdo_white.jpg")
        my_img = my_img.resize((150, 150))
        my_img = ImageTk.PhotoImage(my_img)
        my_img_label = Label(frame, image=my_img, bd=0, borderwidth=0, border=0)
        my_img_label.place(x=425, y=5)

        # ROW 1
        rgs_label = Label(frame, text="Register Here", font=("times new roman", 20, "bold"), bg="white", fg="#000066")
        rgs_label.place(x=420, y=170)

        # ROW 2
        fname_label = Label(frame, text="  First Name :", font=("times new roman", 15, "bold"), bg="white")
        fname_label.place(x=80, y=250)
        fname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.var_fname)
        fname_entry.place(x=220, y=250, width=230)

        lname_label = Label(frame, text="Last Name :", font=("times new roman", 15, "bold"), bg="white")
        lname_label.place(x=550, y=250)
        lname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.var_lname)
        lname_entry.place(x=720, y=250, width=230)

        # Row 3
        userid_label = Label(frame, text=" User ID :", font=("times new roman", 15, "bold"), bg="white")
        userid_label.place(x=110, y=300)
        userid_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.var_contact)
        userid_entry.place(x=220, y=300, width=230)

        email_label = Label(frame, text="Email :", font=("times new roman", 15, "bold"), bg="white")
        email_label.place(x=550, y=300)
        email_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.var_email)
        email_entry.place(x=720, y=300, width=230)

        # Row 4
        security_label = Label(frame, text="One Word Question :", font=("times new roman", 15, "bold"),
                               bg="white")
        security_label.place(x=10, y=350)
        security_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        security_entry.place(x=220, y=350, width=230)

        sec_ans_label = Label(frame, text="Answer :", font=("times new roman", 15, "bold"), bg="white")
        sec_ans_label.place(x=550, y=350)
        sec_ans_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.var_securitya)
        sec_ans_entry.place(x=720, y=350, width=230)

        # Row 5
        password_label = Label(frame, text="Password :", font=("times new roman", 15, "bold"),
                               bg="white")
        password_label.place(x=99, y=400)
        password_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.var_pass, show='*')
        password_entry.place(x=220, y=400, width=230)

        confirm_password_label = Label(frame, text="Retype Password :", font=("times new roman", 15, "bold"),
                                       bg="white")
        confirm_password_label.place(x=550, y=400)
        confirm_password_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')
        confirm_password_entry.place(x=720, y=400, width=230)

        contact_label = Label(frame, text="Contact :", font=("times new roman", 15, "bold"),
                              bg="white")
        contact_label.place(x=110, y=450)
        contact_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        contact_entry.place(x=220, y=450, width=230)

        def show_passwd():
            if password_entry.cget('show') == '*' and confirm_password_entry.cget("show") == '*':
                password_entry.config(show='')
                confirm_password_entry.config(show='')
            else:
                password_entry.config(show='*')
                confirm_password_entry.config(show='*')

        checkbutton = Checkbutton(frame, text="Show Password", font=("times new roman", 12, "bold"), bg="white",
                                  fg="black", onvalue=1,
                                  offvalue=0, command=show_passwd)
        checkbutton.place(x=550, y=450)

        # checkbutton = Checkbutton(frame, text="I agree the terms and conditions applied", bg="white", onvalue=1,
        #                           offvalue=0, variable=check_1)
        # checkbutton.place(x=30, y=460)

        register_button = Button(frame, text="REGISTER", font=("times new roman", 15, "bold"), bg="#000066",
                                 fg="white", activeforeground="white", activebackground="#000066", command=register)
        register_button.place(x=800, y=470)


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    app.root.mainloop()
