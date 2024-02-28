# GUI (Graphical User Interface) module and methods
from tkinter import Tk, Button, Entry, Label, messagebox

root = Tk()

# Block Title

root.title("Registration Block")
root.geometry("350x300")

name_label = Label(text="Username")
name_label.pack()

# Username Text Input

user_name = Entry()
user_name.pack()

email_label = Label(text="Email address")
email_label.pack()

# Email Text Input

email_address = Entry()
email_address.pack()

pass_label = Label(text="Create a password")
pass_label.pack()

# Password Text Input

password = Entry(show="*")
password.pack()


def show_password():
    if password.cget("show") == "":
        password.config(show="*")
        show_btn.config(text="Show")
    else:
        password.config(show="")
        show_btn.config(text="Hide")


show_btn = Button(root, text="Show", command=show_password)
show_btn.pack()


def click():
    email_domains = ['mail.ru', 'gmail.com', 'yandex.com', 'yahoo.com']

    password_content = password.get()
    email_content = email_address.get()
    user_name_content = user_name.get()

    entered_domain = email_content.split('@')[-1]

    if entered_domain not in email_domains:
        messagebox.showerror("Email Error", "Invalid Email Address.")
#   else:
#      email_status = Label(text="Email Succeeded.", foreground="green")
#      email_status.pack()

    if password_content == "":
        messagebox.showerror("Password Error:", "Enter your new password.")
    elif len(password_content) <= 5:
        messagebox.showerror("Password Error:", "Password must have more than 5 characters.")
#     else:
#         password_status = Label(text="Password successfully created.", foreground="green")
#         password_status.pack()

    if user_name_content == "":
        messagebox.showerror("Username Error", "Enter Your Name.")

    if entered_domain in email_domains and len(password_content) > 5 and user_name_content != "":
        messagebox.showinfo("Successful", "Registration completed successfully.")


reg_btn = Button(root, text="Registrate", command=click)
reg_btn.pack()

root.mainloop()
