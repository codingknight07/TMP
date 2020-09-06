import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import askyesno

#main window
root = Tk()
root.title('Signed-In')
root.iconbitmap('C:\ISRA\ISRA LOGO.ico')
root.geometry('350x350')
root.resizable(height = False, width=False)

dum_image = PhotoImage(file='avatar dummy.png')
dum_im_age = dum_image.subsample(2,2)

#first time window
dummy = Label(root, image = dum_im_age)
dummy.place(relx=0.5, rely=0.25, anchor=CENTER)

hey = Label(root, text='Hey Tushar!')
hey.configure(font=("Verdana",20))
hey.place(relx=0.5, rely=0.5, anchor=CENTER)

new = Label(root, text='Not Tushar?')
new.configure(font=("Verdana",9))
new.place(relx=0.4, rely=0.8, anchor=CENTER)
style = Style()
style.configure('an.TButton', font =('Verdana', 8, "bold"))

another_button = Button(root, text='Sign In', style='an.TButton')
another_button.place(relx=0.6, rely=0.8, anchor = CENTER)
another_button.config( width = 6)

mainloop()