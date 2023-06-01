from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("155x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\bansa\OneDrive\Pictures\Dog glasses pic for dp.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\bansa\OneDrive\Pictures\Dog glasses pic for dp.jpg")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("Times new roman", 20, "bold"), bg="black")
        get_str.place(x=95, y=100)

        # labels
        username = lbl = Label(frame, text="Username", font=("Times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("Times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=("Times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtuser = ttk.Entry(frame, font=("Times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=250, width=270)

        # ------------------------Icon Images--------------------------------

        img2 = Image.open(r"C:\Users\bansa\OneDrive\Pictures\Dog glasses pic for dp.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\bansa\OneDrive\Pictures\Dog glasses pic for dp.jpg")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=395, width=25, height=25)

        # ---------login button----------------------
        loginbtn = Button(frame, command=Login_Window, text="Login", font=("Times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # ---------Register button----------------------
        registerinbtn = Button(frame, text="New User Register", font=("Times new roman", 10, "bold"), borderwidth=0,fg="white", bg="black", activeforeground="white", activebackground="black")
        registerinbtn.place(x=15, y=350, width=160)

        # ----------Forgetbutton----------------------
        registerinbtn = Button(frame, text="Forget Password", font=("Times new roman", 10, "bold"), borderwidth=0,fg="white", bg="black", activeforeground="white", activebackground="black")
        registerinbtn.place(x=10, y=370, width=160, height=35)

        # ----------------------login function---------


def login(self):
    if ((self.txtuser.get() == "") or (self.txtpasss.get() == "")):
        messagebox.showerror("Error", "All field required")

    elif (self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu"):
        messagebox.showinfo("Success"), "Welcome to code with Prerana"
    else:
        messagebox.showerror("Invalid", " Invalid Username & Password")




if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
