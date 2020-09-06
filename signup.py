import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import askyesno
from tkcalendar import *
import threading
from tkinter.messagebox import askyesno

l = [0]
m = [0]
n = [0]
o = [0]
p = [0]

#main window
root = Tk()
root.title('Sign Up')
root.iconbitmap('C:\ISRA\ISRA LOGO.ico')
root.geometry('600x680')
root.resizable(height = True, width=False)

#main window scroll
#form_scroll = tk.Scrollbar(orient="vertical")
#form_scroll.grid(row = 1, column = 5, sticky = 'ns', in_ = root)

#root.config(yscrollcommand = form_scroll.set)
#form_scroll.config(command = root.yview)

#New account label
na = Label(root, text='New Account!', font=("Verdana",25, "bold"))
na.grid(row = 1, column = 1, columnspan=2, padx = 15, pady = 15)

#logo label
logopic = PhotoImage(file = 'ISRA LOGO.png')
logophoto = logopic.subsample(2,2)

logo_photo = Label(root)
logo_photo.config(image = logophoto)
logo_photo.grid(row = 1, column = 4, rowspan = 2)

#personal info label
head1 = Label(root, text='Personal Information', font=("Verdana",11, "bold"))
head1.grid(row = 2, column = 1, columnspan=2, padx = 5, pady = 15)

#name input
first_name = StringVar()
firstname = Label(root, text = 'First Name', font = ("Verdana", 11))
firstname.grid(row = 3, column = 1, padx=5, pady=5)

firstname_entry = Entry(root, textvariable = first_name)
firstname_entry.config(width = 25)
firstname_entry.grid(row = 3, column = 2)

last_name = StringVar()
lastname = Label(root, text = 'Last Name', font = ("Verdana", 11))
lastname.grid(row = 3, column = 3, padx=5, pady=5)

lastname_entry = Entry(root, textvariable = last_name)
lastname_entry.config(width = 25)
lastname_entry.grid(row = 3, column = 4)

#date of birth input
dob = Label(root, text = 'Date of Birth', font = ("Verdana", 11))
dob.grid(row = 4, column = 1, padx=5)

def birthdate():
    date = Tk()
    date.title('Date of Birth')
    date.iconbitmap('C:\ISRA\ISRA LOGO.ico')
    date.resizable(height = False, width=False)
    
    cal = Calendar(date, selectmode = "day", year=2020, month=1, day=1)
    cal.pack(fill = "both", expand = True)
    
    date_of_birth = StringVar()
    date_of_birth = cal.get_date()
    
    style = Style()
    style.configure('ok.TButton', font =('Verdana', "bold"))
    Ok_button = Button(date, text='Ok', style='ok.TButton', command = date.destroy)
    Ok_button.pack(side = 'bottom')
    
    dob_entry.config(textvariable = date_of_birth)

    date.mainloop()
 
f_dob = Frame(root)
f_dob.grid(row = 4, column = 2, padx=5, pady=5)

dob_entry = Entry(f_dob)
dob_entry.config(width = 17)
dob_entry.pack(side = 'left')

style = Style()
style.configure('dob.TButton', font =('Verdana', 8, "bold"))
dob_button = Button(f_dob, text='DOB', style='dob.TButton', command = birthdate)
dob_button.config(width = 5)
dob_button.pack(side='right')

#gender input
gender = Label(root, text = 'Gender', font = ("Verdana", 11))
gender.grid(row = 4, column = 3, padx=5, pady=5)

gen_der = StringVar() 
genderchoosen = Combobox(root, width = 22, textvariable = gen_der)
genderchoosen['values'] = ('Male', 'Female', 'Others') 
  
genderchoosen.grid(column = 4, row = 4) 
genderchoosen.current()

#email input
email_ID_pi = StringVar()
emailID_pi = Label(root, text = 'E-Mail ID', font = ("Verdana", 11))
emailID_pi.grid(row = 5, column = 1, padx=5, pady=5)

emailId_pi_entry = Entry(root, textvariable = email_ID_pi)
emailId_pi_entry.config(width = 25)
emailId_pi_entry.grid(row = 5, column = 2)

#phone number input
contact_no = StringVar()
contactno = Label(root, text = 'Contact No.', font = ("Verdana", 11))
contactno.grid(row = 5, column = 3, padx=5, pady=5)

contactno_entry = Entry(root, textvariabl = contact_no)
contactno_entry.config(width = 25)
contactno_entry.grid(row = 5, column = 4)

#bot credentials heading
head2 = Label(root, text='Social Media Credentials', font=("Verdana",11, "bold"))
head2.grid(row = 6, column = 1, columnspan=2, padx = 5, pady = 15)

#asking for email management
femail = Frame(root)
femail.grid(row = 7, column = 1, columnspan = 2, padx=5, pady=5)

emailask = Label(femail, text = 'Want me to manage your emails?', font = ("Verdana", 9))
emailask.pack(side = "left")
def email_ask_yes():
    emailId_entry['state'] = "Normal"
    emailPwd_entry['state'] = "Normal"
    
def email_ask_no():
    emailId_entry['state'] = "disabled"
    emailPwd_entry['state'] = "disabled"
    
def email_ask(i):
    if i==0 :
        l[0]=1
        threading.Thread(target=email_ask_yes).start()
        l[0]=1
        emailask_button.configure(text = "No")
    else : 
        l[0]=0
        emailask_button.configure(text = "Yes")
        l[0]=0
        threading.Thread(target=email_ask_no).start()

style = Style()
style.configure('email.TButton', font =('Verdana', 7, "bold"))
emailask_button = Button(femail, text='Yes', style='email.TButton', command = lambda:email_ask(l[0]))
emailask_button.config(width = 5)
emailask_button.pack(side='right')

email_ID = StringVar()
emailID = Label(root, text = 'E-Mail ID', font = ("Verdana", 11))
emailID.grid(row = 8, column = 1, padx=5, pady=5)

emailId_entry = Entry(root, textvariable = email_ID, state = "disabled")
emailId_entry.config(width = 25)
emailId_entry.grid(row = 8, column = 2)

email_Pwd = StringVar()
emailPwd = Label(root, text = 'Password', font = ("Verdana", 11))
emailPwd.grid(row = 8, column = 3, padx=5, pady=5)

emailPwd_entry = Entry(root, textvariable = email_Pwd, state = "disabled")
emailPwd_entry.config(width = 25)
emailPwd_entry.grid(row = 8, column = 4)

#asking for facebook management
ffb = Frame(root)
ffb.grid(row = 9, column = 1, columnspan = 2, padx=5, pady=5)

fbask = Label(ffb, text = 'Want me to manage your Facebook?', font = ("Verdana", 9))
fbask.pack(side = "left")

def fb_ask_yes():
    fbId_entry['state'] = "Normal"
    fbPwd_entry['state'] = "Normal"
    
def fb_ask_no():
    fbId_entry['state'] = "disabled"
    fbPwd_entry['state'] = "disabled"
    
def fb_ask(i):
    if i==0 :
        m[0]=1
        threading.Thread(target=fb_ask_yes).start()
        m[0]=1
        fbask_button.configure(text = "No")
    else : 
        m[0]=0
        fbask_button.configure(text = "Yes")
        m[0]=0
        threading.Thread(target=fb_ask_no).start()

style = Style()
style.configure('fb.TButton', font =('Verdana', 7, "bold"))
fbask_button = Button(ffb, text='Yes', style='fb.TButton', command = lambda:fb_ask(m[0]))
fbask_button.config(width = 5)
fbask_button.pack(side='right')

fb_ID = StringVar()
fbID = Label(root, text = 'Facebook ID', font = ("Verdana", 11))
fbID.grid(row = 10, column = 1, padx=5, pady=5)

fbId_entry = Entry(root, textvariable = fb_ID, state = "disabled")
fbId_entry.config(width = 25)
fbId_entry.grid(row = 10, column = 2)

fb_Pwd = StringVar()
fbPwd = Label(root, text = 'Password', font = ("Verdana", 11))
fbPwd.grid(row = 10, column = 3, padx=5, pady=5)

fbPwd_entry = Entry(root, textvariable = fb_Pwd, state = "disabled")
fbPwd_entry.config(width = 25)
fbPwd_entry.grid(row = 10, column = 4)

#asking for instagram management
finsta = Frame(root)
finsta.grid(row = 11, column = 1, columnspan = 2, padx=5, pady=5)

instaask = Label(finsta, text = 'Want me to manage your Instagram?', font = ("Verdana", 9))
instaask.pack(side = "left")

def insta_ask_yes():
    instaID_entry['state'] = "Normal"
    instaPwd_entry['state'] = "Normal"
    
def insta_ask_no():
    instaID_entry['state'] = "disabled"
    instaPwd_entry['state'] = "disabled"
    
def insta_ask(i):
    if i==0 :
        n[0]=1
        threading.Thread(target=insta_ask_yes).start()
        n[0]=1
        instaask_button.configure(text = "No")
    else : 
        n[0]=0
        instaask_button.configure(text = "Yes")
        n[0]=0
        threading.Thread(target=insta_ask_no).start()

style = Style()
style.configure('insta.TButton', font =('Verdana', 7, "bold"))
instaask_button = Button(finsta, text='Yes', style='insta.TButton', command = lambda:insta_ask(n[0]))
instaask_button.config(width = 5)
instaask_button.pack(side='right')

insta_ID = StringVar()
instaID = Label(root, text = 'Instagram ID', font = ("Verdana", 11))
instaID.grid(row = 12, column = 1, padx=5, pady=5)

instaID_entry = Entry(root, textvariable = insta_ID, state = "disabled")
instaID_entry.config(width = 25)
instaID_entry.grid(row = 12, column = 2)

insta_Pwd = StringVar()
instaPwd = Label(root, text = 'Password', font = ("Verdana", 11))
instaPwd.grid(row = 12, column = 3, padx=5, pady=5)

instaPwd_entry = Entry(root, textvariable = insta_Pwd, state = "disabled")
instaPwd_entry.config(width = 25)
instaPwd_entry.grid(row = 12, column = 4)

#asking for twitter management
ftweet = Frame(root)
ftweet.grid(row = 13, column = 1, columnspan = 2, padx=5, pady=5)

tweetask = Label(ftweet, text = 'Want me to manage your Twitter?', font = ("Verdana", 9))
tweetask.pack(side = "left")

def tweet_ask_yes():
    twitterID_entry['state'] = "Normal"
    twitterPwd_entry['state'] = "Normal"
    
def tweet_ask_no():
    twitterID_entry['state'] = "disabled"
    twitterPwd_entry['state'] = "disabled"
    
def tweet_ask(i):
    if i==0 :
        o[0]=1
        threading.Thread(target=tweet_ask_yes).start()
        o[0]=1
        tweetask_button.configure(text = "No")
    else : 
        o[0]=0
        tweetask_button.configure(text = "Yes")
        o[0]=0
        threading.Thread(target=tweet_ask_no).start()

style = Style()
style.configure('tw.TButton', font =('Verdana', 7, "bold"))
tweetask_button = Button(ftweet, text='Yes', style='tw.TButton', command = lambda:tweet_ask(o[0]))
tweetask_button.config(width = 5)
tweetask_button.pack(side='right')

twitter_ID = StringVar()
twitterID = Label(root, text = 'Twitter ID', font = ("Verdana", 11))
twitterID.grid(row = 14, column = 1, padx=5, pady=5)

twitterID_entry = Entry(root, textvariable = twitter_ID, state = "disabled")
twitterID_entry.config(width = 25)
twitterID_entry.grid(row = 14, column = 2)

twitter_Pwd = StringVar()
twitterPwd = Label(root, text = 'Password', font = ("Verdana", 11))
twitterPwd.grid(row = 14, column = 3, padx=5, pady=5)

twitterPwd_entry = Entry(root, textvariable = twitter_Pwd, state = "disabled")
twitterPwd_entry.config(width = 25)
twitterPwd_entry.grid(row = 14, column = 4)

#whatsapp_ID = StringVar()
#whatsappID = Label(root, text = 'WhatsApp No.', font = ("Verdana", 11))
#whatsappID.grid(row = 12, column = 1, padx=5, pady=5)

#whatsappId_entry = Entry(root, textvariable = whatsapp_ID, state = "disabled")
#whatsappId_entry.config(width = 25)
#whatsappId_entry.grid(row = 12, column = 2)

#email_Pwd = StringVar()
#emailPwd = Label(root, text = 'First Name', font = ("Verdana", 11))
#emailPwd.grid(row = 4, column = 3, padx=5)

#emailPwd_entry = Entry(root, textvariable = email_ID)
#emailPwd_entry.config(width = 25)
#emailPwd_entry.grid(row = 4, column = 4)

#asking for linkedin management
flinkedin = Frame(root)
flinkedin.grid(row = 15, column = 1, columnspan = 2, padx=5, pady=5)

linkedinask = Label(flinkedin, text = 'Want me to manage your LinkedIn?', font = ("Verdana", 9))
linkedinask.pack(side = "left")

def linkedin_ask_yes():
    linkedinId_entry['state'] = "Normal"
    linkedinPwd_entry['state'] = "Normal"
    
def linkedin_ask_no():
    linkedinId_entry['state'] = "disabled"
    linkedinPwd_entry['state'] = "disabled"
    
def linkedin_ask(i):
    if i==0 :
        p[0]=1
        threading.Thread(target=linkedin_ask_yes).start()
        p[0]=1
        linkedinask_button.configure(text = "No")
    else : 
        p[0]=0
        linkedinask_button.configure(text = "Yes")
        p[0]=0
        threading.Thread(target=linkedin_ask_no).start()

style = Style()
style.configure('linked.TButton', font =('Verdana', 7, "bold"))
linkedinask_button = Button(flinkedin, text='Yes', style='linked.TButton', command = lambda:linkedin_ask(p[0]))
linkedinask_button.config(width = 5)
linkedinask_button.pack(side='right')

linkedin_ID = StringVar()
linkedinID = Label(root, text = 'LinkedIn ID', font = ("Verdana", 11))
linkedinID.grid(row = 16, column = 1, padx=5, pady=5)

linkedinId_entry = Entry(root, textvariable = linkedin_ID, state = "disabled")
linkedinId_entry.config(width = 25)
linkedinId_entry.grid(row = 16, column = 2)

linkedin_Pwd = StringVar()
linkedinPwd = Label(root, text = 'Password', font = ("Verdana", 11))
linkedinPwd.grid(row = 16, column = 3, padx=5, pady=5)

linkedinPwd_entry = Entry(root, textvariable = linkedin_Pwd, state = "disabled")
linkedinPwd_entry.config(width = 25)
linkedinPwd_entry.grid(row = 16, column = 4)


style = Style()
style.configure('submit.TButton', font =('Verdana', 11, "bold"))
submit_button = Button(root, text='Submit', style='submit.TButton', command = lambda: askyesno('Confirmation!', 'Do you want to submit your information?'))
submit_button.config(width = 15)
submit_button.grid(row = 17, column = 2, columnspan=2, padx=10, pady =20)

root.mainloop()