
from tkinter.font import BOLD
import webbrowser

import re

import sys

import os

import tkinter as tk

from tkinter import *

from tkinter import messagebox

import tkinter.filedialog

from PIL import Image, ImageTk

from pathlib import Path

global root

root = tk.Tk()

#window size
root.geometry("700x700")

#window title
root.title("azcrook's Program")

#Background Image For LogIn
Background_image = PhotoImage( file ="C:\\Users\\manny\\OneDrive\\Desktop\\AZBACKGROUNDTK.PNG")
BackGroundImage = tk.Label(root, image=Background_image)
BackGroundImage.place(y=0,x=0, width=600, height=400)
BackGroundImage.pack()

#Register page
def Register():
    global screen1
    

    

    screen1 = Toplevel(root)
    screen1.title('Register')
    screen1.geometry("700x400")

    #Background Image
    backgroundimage_Register = tk.Label(screen1, image=Background_image)
    backgroundimage_Register.place(y=0, x=0, width=700, height=400)
    backgroundimage_Register.focus()

    global username
    global email
    global password
    global username_entry
    global email_entry
    global password_entry
    username = StringVar()
    email = StringVar()
    password = StringVar()

    #Text Label on the left for information ETC...
    RLabel = Label (screen1, text='Please entry your information such as',bg='#1388CA', fg='white', highlightthickness=0, font=10,)
    RLabel.place(x=30,y=10)
    RLabel.focus()
    RLabel1 = Label(screen1, text='your Username, Email, and Password ',bg='#1388CA', fg='white', highlightthickness=0, font=10,)
    RLabel1.place(x=30,y=40)
    RLabel1.focus()
    RLabel2 = Label(screen1, text='on the right hand side of the screen.',bg='#1388CA', fg='white', highlightthickness=0, font=10,)
    RLabel2.place(x=30,y=70)
    RLabel2.focus()
    RLabel3 = Label(screen1, text='              All Info will be secure!',bg='#1388CA', fg='white', highlightthickness=0, font=10,)
    RLabel3.place(x=30,y=180)
    RLabel3.focus()

    #Username Register Label
    RuserL = Label (screen1,bd=0,  bg='#1388CA', fg='Black', highlightthickness=0, font=5, text='Username')
    RuserL.place(x=420, y=10, width=200, height=17)
    RuserL.focus()

    #Username Register Entry
    username_entry = Entry(screen1, textvariable=username, bd=0, bg='#76CBFC', fg='Black', highlightthickness=0, font='20',  )
    username_entry.place(x=420, y=27 ,width=200, height=30)
    username_entry.focus()

    #Email Register Label
    RemailL = Label (screen1, text='Email', bd=0,  bg='#1388CA', fg='Black', highlightthickness=0, font=5,)
    RemailL.place(x=420, y=70, width=200, height=17)
    RemailL.focus()

    #Email Register Entry
    email_entry = Entry(screen1, textvariable=email, bd=0, bg='#76CBFC', fg='Black', highlightthickness=0, font='20',)
    email_entry.place(x=420, y=87 ,width=200, height=30)
    email_entry.focus()

    #Password Register Label
    RpasswordL = Label(screen1,text='Password', bd=0,  bg='#1388CA', fg='Black', highlightthickness=0, font=5,)
    RpasswordL.place(x=420, y=130, width=200, height=17)
    RpasswordL.focus()

    #password Register Entry
    password_entry = Entry(screen1, textvariable=password, bd=0, bg='#76CBFC', fg='Black', highlightthickness=0, font='20',)
    password_entry.place(x=420, y=147 ,width=200, height=30)
    password_entry.focus()

    #Register Button when complete!
    Rbtn = Button(screen1, text='Register', command=register_user, bd=0, bg='#76CBFC', fg='Black', highlightthickness=0, font='20',)
    Rbtn.place(x=440, y=207, width=150, height=30)
    Rbtn.focus()

    

def register_user():
    username_info = username.get()
    email_info = email.get()
    password_info = password.get()

    if not username_info:
        tk.messagebox.showerror(title = 'Empty Field!', message = 'Please Enter Correct Username')
        return
    if not email_info:
        tk.messagebox.showerror(title = 'Empty Feild!', message = 'Please Enter Correct Email')
        return
    if not password_info:
        tk.messagebox.showerror(title = 'Empty Feild!', message = 'Please Enter Correct Password')
        return
    if None:
        tk.messagebox.showerror(title = 'Error!', message = 'Wrong User, Email, Password or Left Blank!')
        return

    file = open (username_info, "w")
    file.write(username_info+"\n")
    file.write(email_info+"\n")
    file.write(password_info)

    username_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

    #Text the the registaration is correct.
    RUL = Label(screen1, text='Registration Sucess! you can now close tab.', fg='green', bg='white')
    RUL.place(x=390, y=287 ,width=300, height=30)
    RUL.focus()



#Button Clicks inputs from Entry
def LogIn():
    User = User_entry.get()
    Email = Email_entry.get()
    Password = Password_entry.get()
    
    

    if not User:
        tk.messagebox.showerror(title = 'Empty Field!', message = 'Please Enter Correct Username')
        return
    if not Email:
        tk.messagebox.showerror(title = 'Empty Feild!', message = 'Please Enter Correct Email')
        return
    if not Password:
        tk.messagebox.showerror(title = 'Empty Feild!', message = 'Please Enter Correct Password')
        return
    if None:
        tk.messagebox.showerror(title = 'Error!', message = 'Wrong User, Email, Password or Left Blank!')
        return
    list_of_files = os.listdir()
    if User in list_of_files:
        file1 = open(User, 'r')
        verify = file1.read().splitlines()
        if Email in verify:
            print("Email Verified")
            if Password in verify:
                login_sucess()   
    else:
        tk.messagebox.showerror(title = 'Error!', message = 'User not found in our data base!')
 

def DRW():
    delete_root_window['state'] = 'disable'
    delete_root_window1['state'] = 'disable'
    TwitchVB['state'] = 'normal'
    YoutubeVB['state'] = 'normal'
    Spoofer['state'] = 'normal'
    unlockA['state'] = 'normal'

def disagree():
    root.destroy()
    
def ToS():
    toss = Toplevel(root)
    toss.title('Terms of Service')
    toss.geometry('300x300')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Twitch View Bot program
def TVB():
    print('Twitch View Bot')
    #BOT v1.1 Beta
#GUI imports
    
    import tkinter as tk
    from tkinter import filedialog, Text 
    import os
#bot imports
    import requests
    import sys
    import time
    import random
    from random import shuffle
    from streamlink import Streamlink
    from fake_useragent import UserAgent

    import linecache

    from threading import Thread



#the core of the whole procces
    root1 = Toplevel(root)
    root1.geometry("500x500")

    apps = []
    threadin = []
    proxi = []

    root1.title ("TTVBot v1.1 Beta")



#the functions of the values
    def addApp():
        thread_connect['state']= 'normal'
        openFile['text']= "Applied"
        openFile['state']= 'disabled'
        filename = filedialog.askopenfilename(initialdir="/",  title="select proxy list", 
            filetypes=(("azcrook knows all", "*.txt"),("all files", "*.*")))
        apps.append(filename)
        print(filename)
        for app in apps:
            label = tk.Label(frame, text=app, fg="black", bg="white")
            label.pack()
            label.place (x=10, y=100)
        for app in apps:
            text = open(filename, 'r' )
            info = text.read()
            proxy_textbox.insert(END, info)
            text.close()
        return filename
    
    def run():
    
        channel_url = proxi
        proxies_file = apps
        processes = []
        max_nb_of_threads = 1000

        all_proxies = []
        nb_of_proxies = 0

# Session creating for request
        ua = UserAgent()
        session = Streamlink()
        session.set_option("http-headers", {'User-Agent': ua.random, "Client-ID": "ewvlchtxgqq88ru9gmfp1gmyt6h2b93"})

        class ViewerBot:
            def print_exception(self):
                exc_type, exc_obj, tb = sys.exc_info()
                f = tb.tb_frame
                lineno = tb.tb_lineno
                filename = f.f_code.co_filename
                linecache.checkcache(filename)
                line = linecache.getline(filename, lineno, f.f_globals)
                print( 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))



            def get_proxies(self):
        # Reading the list of proxies
                global nb_of_proxies
                try:
                    lines = [line.rstrip("\n") for line in open(proxies_file)]
                except IOError as e:
                    print( "An error has occurred while trying to read the list of proxies: %s" % e.strerror)
                    sys.exit(1)

                nb_of_proxies = len(lines)
                return lines


            def get_url(self):
                url = ""
                try:
                    streams = session.streams(self.channel_url)
                    try:
                        url = streams['audio_only'].url
                        print( f"URL : {url[:30]}...\n")
                    except:
                        url = streams['worst'].url
                        print( f"URL : {url[:30]}...\n")

                except:
                    pass
                return url

            def open_url(self,proxy_data):
                try:
                    global all_proxies
                    headers = {'User-Agent': ua.random}
                    current_index = all_proxies.index(proxy_data)

                    if proxy_data['url'] == 100:
                        proxy_data['url'] = self.get_url()
                    current_url = proxy_data['url']
                    try:
                        if time.time() - proxy_data['time'] >= random.randint(1, 5):
                            current_proxy = {"http": proxy_data['proxy'], "https": proxy_data['proxy']}
                            with requests.Session() as s:
                                response = s.head(current_url, proxies=current_proxy, headers=headers)
                            print( f"Sent HEAD request with {current_proxy['http']} | {response.status_code} | {response.request} | {response}")
                            proxy_data['time'] = time.time()
                            all_proxies[current_index] = proxy_data
                    except:
                        print("Connection Error! BAD PROXY OR NO STREAM FOUND! Msg azcrook for help!")

                except (KeyboardInterrupt, SystemExit):
                    sys.exit()


            def mainmain(self):
                self.channel_url = "https://www.twitch.tv/" + sys.argv[1]
                proxies = self.get_proxies()
        
                for p in proxies:
                    all_proxies.append({'proxy': p, 'time': time.time(), 'url': ''})

                shuffle(all_proxies)
                list_of_all_proxies = all_proxies
                current_proxy_index = 0

                while True:
                    try:
                        for i in range(100, max_nb_of_threads):
                            threaded = Thread(target=self.open_url, args=(all_proxies[random.randint(0, len(all_proxies))],))
                            threaded.daemon = True  # This thread dies when main thread (only non-daemon thread) exits.
                            threaded.start()
                    except:
                        self.print_exception()
                    shuffle(all_proxies)
                    time.sleep(5)


        ViewerBot = ViewerBot()
        ViewerBot.mainmain() 
        
    def connect1():
        connect['text']= 'Connected'
        connect['state']= 'disabled'
        openFile['state']= 'normal'
        text = entry.get()
        proxi.append(text)
        print(text)
    
        for text in proxi:
            label = tk.Label(frame, fg="black", bg="white")
            label.pack()
            label.place (x=10, y=75)
        return text

    def threads1():
        thread_connect['text']= 'Connected'
        thread_connect['state']='disabled'
        runApps['state']= 'normal'
        text1 = threads.get()
        
        threadin.append(text1)
        print(text1)
    

        for app in apps:
            label1 = tk.Label(frame, text= text1, fg="black", bg="white")
            label1.pack()
            label1.place (x=225, y=220)
        return text1

    



    







#inputs and text boxs that the user can input
    canvas = tk.Canvas(root1, height=500, width=500, bg="#6441A4" )
    canvas.pack()

    frame = tk.Frame(root1, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#user name entry
    label = tk.Label(root1, text="Stream Username", bg="white", fg="black")
    label.pack()
    label.place (x=200, y=80)
    connect = tk.Button(root1, text="Connect", fg="white", bg="black", command=connect1, )
    connect.pack()
    connect.place (x=300, y=95)
    entry = tk.Entry(root1, text="Enter stream User here", fg="black", bg="grey", )
    entry.pack()
    entry.place (x=175, y=100)

#proxy list entry
    openFile = tk.Button(root1, text="Open Proxy List", padx=8, pady=3, fg="white", bg="black", command=addApp, compound="top", state=DISABLED)
    openFile.pack()
    openFile.place (x=80, y=400)
    proxy_textbox = Text(root1, width=17, height=12, fg="black", bg="grey", )
    proxy_textbox.pack()
    proxy_textbox.place (x=73, y=200)

#thread count entry
    threads = tk.Entry(root1, text="Enter thread count", fg="black", bg="grey",  )
    threads.pack()
    threads.place (x=280, y=205)
    label1 = tk.Label(root1, text="Enter thread count", bg="white", fg="black")
    label1.pack()
    label1.place (x=290, y=183)
    thread_connect = tk.Button(root1, text="connect", fg="white", bg="black", command=threads1, compound="top", state=DISABLED )
    thread_connect.pack()
    thread_connect.place (x=300, y=225)

#number of bots sent
    label2= tk.Label(root1, text="Bots Sent:", fg="black", bg="white", font=40)
    label2.pack()
    label2.place (x=260, y=383)

#Start the view bot
    runApps = tk.Button(root1, text="Start View Bot", padx=8, pady=3, fg="white", bg="black",command=run, state=DISABLED)
    runApps.pack()
    runApps.place (x=290, y=290)

    
    root1.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Youtube View Bot Program
def YTVB():
    print('Youtube View bot')

#HWID Spoofer Program
def Spoof():
    print('HWID Spoofer active')

def unlockAll():
    print('Unlock All tool for WZ 2.0')

#user has logged in sucessfully and now can use the program
def login_sucess():

    global delete_root_window1
    global lc3
    global delete_root_window
    global TwitchVB
    global YoutubeVB
    global Spoofer
    global unlockA

    #lc3 is the programs window for all of the apps
    lc3 = Toplevel (root)
    lc3.title('hacks/mods by azcrook')
    lc3.geometry("700x700")

    

    #background image
    backgroundimage_Register = tk.Label(lc3, image=Background_image)
    backgroundimage_Register.place(y=0, x=0, width=700, height=700)
    backgroundimage_Register.focus()

    #Label about the ToS
    Terms_of_Service = Label(lc3, text='By clicking agree you agree with the ToS', font='20', bg='#76CBFC', fg='white')
    Terms_of_Service.place(x=200,y=10)
    Terms_of_Service.focus()

    #Button that agrees with the terms and conditions
    delete_root_window = tk.Button(lc3, text='Agree', command=DRW)
    delete_root_window.place(x=10,y=10)
    delete_root_window.focus()

    #Button that disagrees with terms and conditions so it closes itself
    delete_root_window1 = Button(lc3, text='Disagree', command=disagree)
    delete_root_window1.place(x=60,y=10)
    delete_root_window1.focus()

    #TOS Button
    Terms_of = Button(lc3, text='ToS', command=ToS)
    Terms_of.place(x=660,y=10)
    Terms_of.focus()

    #TwitchViewBot Button
    TwitchVB = Button(lc3, text='Twitch View Bot', command=TVB, bd=1, bg='purple', fg='white', highlightthickness=0, font='20', state=DISABLED)
    TwitchVB.place(x=80,y=100, width=180, height=40)
    TwitchVB.focus()

    #YoutubeViewBot Button
    YoutubeVB = Button(lc3, text='Youtube View Bot', command=YTVB, bd=1, bg='red', fg='white', highlightthickness=0, font='20', state=DISABLED)
    YoutubeVB.place(x=80,y=200, width=180, height=40)
    YoutubeVB.focus()

    #Spoofer Button
    Spoofer = Button(lc3, text='HWID Spoofer', command=Spoof, bd=1, bg='black', fg='white', highlightthickness=0, font='20', state=DISABLED)
    Spoofer.place(x=80,y=300, width=180, height=40)
    Spoofer.focus()

    #Unlock All Tool for WZ 2.0
    unlockA = Button(lc3, text='UnlockAll WZ 2.0', command=unlockAll, bd=1, bg='green', fg='white', highlightthickness=0, font='20', state=DISABLED)
    unlockA.place(x=80,y=400, width=180, height=40)
    unlockA.focus()




#Username Entry
User_entry = Entry (bd=0, bg='#76CBFC', fg='Black', highlightthickness=0, font='20', )
User_entry.place (x=430, y=100, width=200, height=50)
User_entry.focus ()

#Email Entry
Email_entry = Entry (bd=0, bg='#76CBFC', fg='Black', highlightthickness=0, font='20', )
Email_entry.place (x=430, y=190, width=200, height=50)
Email_entry.focus ()

#Password Entry
Password_entry = Entry (bd=0, bg='#76CBFC', fg='Black', highlightthickness=0, font='20', show='*' )
Password_entry.place (x=430, y=280, width=200, height=50)
Password_entry.focus ()

#Button for User/Email/Pass Entry
Button1 = Button (bd=0, bg='#76CBFC', fg='Black', highlightthickness=0, font='20', text='Log In', command=LogIn)
Button1.place (x=453, y=350, width=150, height=30)
Button1.focus ()

#Username Entry Label
User_label = Label (bd=0, bg='#1388CA', fg='Black', highlightthickness=0, font=5, text='Username' )
User_label.place (x=430, y=90, width=200, height=17)
User_label.focus ()

#Email Entry Label
Email_label = Label (bd=0, bg='#1388CA', fg='Black', highlightthickness=0, font=5, text='Email' )
Email_label.place (x=430, y=180, width=200, height=17)
Email_label.focus ()

#Password Entry Label
Password_label = Label (bd=0, bg='#1388CA', fg='Black', highlightthickness=0, font=5, text='Password' )
Password_label.place (x=430, y=270, width=200, height=17)
Password_label.focus ()


#Button got Registery
Button2 = Button (bd=0, bg='#76CBFC', fg='Black', highlightthickness=0, font='20', text='Register', command=Register)
Button2.place (x=453, y=450, width=150, height=30)
Button2.focus ()

#top center of the title text of the login
infoL = Label (bd=0,bg='#76CBFC', fg='Black', highlightthickness=100, font=5, text='This is a sample text' )
infoL.place (x=250, y=10, width=200, height=25)
infoL.focus()

#Global so it gets the entries for all modules



root.mainloop()


