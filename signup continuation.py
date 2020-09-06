import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import askyesnocancel
from tkinter import filedialog
from PIL import ImageTk,Image
import sqlite3

#main window
root = Tk()
root.title('Sign Up')
root.iconbitmap('C:\ISRA\ISRA LOGO.ico')
root.geometry('350x350')
root.resizable(height = False, width=False)

#edit profile picture window
def select_profile():
    root.filename = filedialog.askopenfilename(initialdir = "/Pictures", title = 'Select a file', filetype = (('png files', '.png'), ("jpg files", '.jpg'), ("jpeg files", '.jpeg')))
    newimage = Image.open(root.filename)
    resize_newimage = newimage.resize((95,85), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resize_newimage)
    userprofile.configure(image = new_image)

userimage = Image.open("ONLY LOGO.png")
resize_userimage = userimage.resize((95,85), Image.ANTIALIAS)
user_image = ImageTk.PhotoImage(resize_userimage)

dummyimage = Image.open("avatar dummy.png")
resize_dummyimage = dummyimage.resize((95,85), Image.ANTIALIAS)
dummy_image = ImageTk.PhotoImage(resize_dummyimage)

def profile_change():
    result = askyesnocancel('Edit profile picture', 'Press Yes to change, No to remove and Cancel to abort.', icon = 'info')
    if result == False:
        userprofile.configure(image = dummy_image)
    elif result == True:
        select_profile()
        

#userprofile = Button(root, height=100, width=80)
userprofile = Button(root, width=17, image = user_image, command = profile_change)
userprofile.place(relx=0.5, rely=0.15, anchor=CENTER)

un = Label(root, text='Enter your Username')
un.configure(font=("Verdana",10))
un.place(relx=0.5, rely=0.35, anchor=CENTER)

username_var = StringVar()

username_entry = Entry(root, textvariable = username_var)
username_entry.config(width = 25)
username_entry.place(relx=0.5,rely=0.41,anchor=CENTER)

eg = Label(root, text='for eg: gargtushar')
eg.configure(font=("Verdana",7))
eg.place(relx=0.5, rely=0.47, anchor=CENTER)

pw = Label(root, text='Enter your Password')
pw.configure(font=("Verdana",10))
pw.place(relx=0.5, rely=0.53, anchor=CENTER)

password_var = StringVar()

password_entry = Entry(root, textvariable = password_var)
password_entry.config(width = 25)
password_entry.place(relx=0.5,rely=0.59,anchor=CENTER)

pwconf = Label(root, text='Confirm Password')
pwconf.configure(font=("Verdana",10))
pwconf.place(relx=0.5, rely=0.69, anchor=CENTER)

pwdconf_var = StringVar()

pwdconf_entry = Entry(root, textvariable = pwdconf_var, show = "*")
pwdconf_entry.config(width = 25)
pwdconf_entry.place(relx=0.5,rely=0.75,anchor=CENTER)

style = Style()
style.configure('su.TButton', font =('Verdana', 10, "bold"))

signup_button = Button(root, text='Sign Up', style='su.TButton')
signup_button.place(relx=0.5, rely=0.87, anchor = CENTER)
signup_button.config( width = 7)

mainloop()