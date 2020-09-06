import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import askyesno

#main window
root = Tk()
root.title('ISRA')
root.iconbitmap('C:\ISRA\ISRA LOGO.ico')
root.geometry('350x350')
root.resizable(height = False, width=False)

#first time window
misc = Label(root, text='Login Here!')
misc.configure(font=("Verdana",20))
misc.place(relx=0.5, rely=0.1, anchor=CENTER)

un = Label(root, text='Username')
un.configure(font=("Verdana",10))
un.place(relx=0.5, rely=0.24, anchor=CENTER)

username_var = StringVar()

username_entry = Entry(root, textvariable = username_var)
username_entry.config(width = 35)
username_entry.place(relx=0.5,rely=0.3,anchor=CENTER)

pw = Label(root, text='Password')
pw.configure(font=("Verdana",10))
pw.place(relx=0.5, rely=0.4, anchor=CENTER)

password_var = StringVar()

password_entry = Entry(root, textvariable = password_var)
password_entry.config(width = 35)
password_entry.place(relx=0.5,rely=0.46,anchor=CENTER)

style = Style()
style.configure('TButton', font =('Verdana', 10, "bold"))
login_button = Button(root, text='Login', style='TButton', command = lambda : askyesno('Confirmation','Do you want to log in?'))

login_button.place(relx=0.5, rely=0.57, anchor = CENTER)
login_button.config( width = 15)

signup = Label(root, text='New User?')
signup.configure(font=("Verdana",9))
signup.place(relx=0.4, rely=0.8, anchor=CENTER)

style.configure('su.TButton', font =('Verdana', 8, "bold"))

signup_button = Button(root, text='Sign Up', style='su.TButton')
signup_button.place(relx=0.6, rely=0.8, anchor = CENTER)
signup_button.config( width = 7)

mainloop()