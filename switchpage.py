#Youtube link: https://www.youtube.com/watch?v=95tJO7XJlko

import tkinter
from tkinter import *

class Ft:
    def __init__(self,root):
        root.geometry("500x400")
        root.title("Tkinter Hub")

        def delete_pages():
            for frame in main_frame.winfo_children():
                frame.destroy()

        def hide_indicate():
            home_indicate.config(bg="#c3c3c3")
            menu_indicate.config(bg="#c3c3c3")
            contact_indicate.config(bg="#c3c3c3")
            about_indicate.config(bg="#c3c3c3")

        def home_page():
            home_frame = Frame(main_frame)
            lb = Label(home_frame,text="This is home page.")
            lb.pack()
            home_frame.pack(pady=20,padx=20)
        def menu_page():
            menu_frame = Frame(main_frame)
            lb = Label(menu_frame,text="This is menu page.")
            lb.pack()
            menu_frame.pack(pady=20,padx=20)
        def contact_page():
            contact_frame = Frame(main_frame)
            lb = Label(contact_frame,text="This is contact page.")
            lb.pack()
            contact_frame.pack(pady=20,padx=20)
        def about_page():
            about_frame = Frame(main_frame)
            lb = Label(about_frame,text="This is about page.")
            lb.pack()
            about_frame.pack(pady=20,padx=20)


        def indicate(lb,page):
            hide_indicate()
            lb.config(bg="blue")
            delete_pages()
            page()

        options_frame = Frame(root,bg="#c3c3c3")
        options_frame.pack(side=LEFT)
        options_frame.pack_propagate(False)
        options_frame.configure(width=100,height=400)

        home_btn = Button(options_frame,text="Home" , font=("bold",15),bg="#c3c3c3",fg="#158aff",bd=0,command=lambda : indicate(home_indicate,home_page))
        home_btn.place(x=10, y=50)
        home_indicate = Label(options_frame,text="",bg="#c3c3c3")
        home_indicate.place(x=3,y=50,width=5,height=40)

        menu_btn = Button(options_frame,text="Menu" , font=("bold",15),bg="#c3c3c3",fg="#158aff",bd=0,command=lambda : indicate(menu_indicate,menu_page))
        menu_btn.place(x=10, y=100)
        menu_indicate = Label(options_frame,text="",bg="#c3c3c3")
        menu_indicate.place(x=3,y=100,width=5,height=40)

        contact_btn = Button(options_frame,text="Contacts" , font=("bold",15),bg="#c3c3c3",fg="#158aff",bd=0,command=lambda : indicate(contact_indicate,contact_page))
        contact_btn.place(x=10, y=150)
        contact_indicate = Label(options_frame,text="",bg="#c3c3c3")
        contact_indicate.place(x=3,y=150,width=5,height=40)

        about_btn = Button(options_frame,text="About", font=("bold",15),bg="#c3c3c3",fg="#158aff",bd=0,command=lambda : indicate(about_indicate,about_page))
        about_btn.place(x=10, y=200)
        about_indicate = Label(options_frame,text="",bg="#c3c3c3")
        about_indicate.place(x=3,y=200,width=5,height=40)


        main_frame = Frame(root,highlightbackground="black",highlightthickness=2)
        main_frame.pack(side=LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(width=500,height=400)

if __name__=="__main__":
    root = Tk()
    app = Ft(root)
    app,root.mainloop()
