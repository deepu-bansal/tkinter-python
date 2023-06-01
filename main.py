from tkinter import *
from password_generate import Pass_generate
window = Tk()
window.config(padx=20,pady=20)


def pass_do():
    input_password.insert(0,Pass_generate())

label_firstname = Label(text="Firstname")
label_firstname.grid(row=0,column=0)
label_lastname = Label(text="Lastname")
label_lastname.grid(row=1,column=0)
label_email = Label(text="Email")
label_email.grid(row=2,column=0)
label_password= Label(text="Password")
label_password.grid(row=3,column=0)
label_form_new_group = Label(text="Form a New Group")
label_form_new_group.grid(row=4,column=0)


input_firstname = Entry();
input_firstname.grid(row=0,column=1)
input_lastname = Entry()
input_lastname.grid(row=1,column=1)
input_email = Entry()
input_email.grid(row=2,column=1)
input_password= Entry()
input_password.grid(row=3,column=1)

button_form_new_group = Button(text="New Group")
button_form_new_group.grid(row=4,column=1)
button_regenerate_password = Button(text="Regenerate Password",command=pass_do)
button_regenerate_password.grid(row=3,column=2)
button_register = Button(text="Register")
button_register.grid(row=5,column=2)

window.mainloop()