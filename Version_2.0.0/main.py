from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from keyboard import *
from pyautogui import *
import time
import webbrowser
import tkinter as tk
import shutil
import random
a = ""
file = ''
iconfile = ''
def open_file():
    global file
    file = filedialog.askopenfile(mode='rb', filetypes=[('Zip files', '*.zip')])

def lock():
    global file
    name = bee.get()
    se = be.get()
    a = file.read()
    pas = open("password.py","w")
    pas.write(f"qw = a.replace(b'PK', b\"{rann}\")")
    print(a)
    b = open(f"{name}.zip","wb")
    #b.write(f"b = open(f\"{name}.zip\",\"w\")\nb.write({a})")
    b.write(q)



def clear():
    try:
        na = be.get()
        space = open(f"{na}","w")
        space.write("")
    except:
        print('no clearer')
#========================================
avv = 0
avm = 0
avl = 0
consol = " "
onefile = ' '
ico = " "
ase = ''
#========================================

def radio(mm):
    global avv
    global consol
    avv = avv + mm
    if avv % 2 == 0:
        consol = " "
        f = Button(bg='white',bd=0,image=E_Button,command=lambda:radio(1)).place(x=125,y=210)
    else:
        f = Button(bg='white',bd=0,image=F_Button,command=lambda:radio(1)).place(x=125,y=210)
        consol = " --windowed"


def radio1(mm):
    global avm
    global onefile
    avm = avm + mm
    if avm % 2 == 0:
        onefile = ' '
        f = Button(bg='white',bd=0,image=E_Button,command=lambda:radio1(1)).place(x=125,y=180)
    else:
        onefile = ' --onefile'
        f = Button(bg='white',bd=0,image=F_Button,command=lambda:radio1(1)).place(x=125,y=180)

def had(m):
    if m == 2:
        radio(1)
    elif m == 3:
        icone(1)
    else:
        radio1(1)

def filep():
    sd = os.getcwd()+"\dist"
    webbrowser.open(sd)

def icone():
    global iconfile
    iconfile = filedialog.askopenfile(mode='r', filetypes=[('Icon', '*.ico')])
    iconfile = str(iconfile)
    print(iconfile)
    c = iconfile.find("name=\'")
    cl = iconfile.find(".ico\'")
    iconfile = iconfile[c+6:cl+4]
    if iconfile != None:
        ico = ' -i'

            

        




bgg = 'white'
win = Tk()
win.title('~ CPY ~')
win.geometry("689x500")
win.configure(bg="white")
win.resizable(0, 0)
rgifs = os.getcwd()


win.iconbitmap(f"{rgifs}\\data\\CPY.ico")
I_Entry = PhotoImage(file = f"{rgifs}\\data\\e.gif")
B_Button = PhotoImage(file =f"{rgifs}\\data\\btc.gif")
C_Button = PhotoImage(file =f"{rgifs}\\data\\btb.gif")
D_Button = PhotoImage(file =f"{rgifs}\\data\\rtc.gif")
E_Button = PhotoImage(file =f"{rgifs}\\data\\ro.gif")
F_Button = PhotoImage(file =f"{rgifs}\\data\\rn.gif")
G_Button = PhotoImage(file =f"{rgifs}\\data\\flp.gif")
H_Button = PhotoImage(file =f"{rgifs}\\data\\bti.gif")



a = Button(bg='white',bd=0,image=B_Button,command=open_file).place(x=290,y=170)
b = Button(bg='white',bd=0,image=C_Button,command=lock).place(x=290,y=230)
c = Button(bg='white',bd=0,image=D_Button,command=clear).place(x=290,y=290)
d = Button(bg='white',bd=0,image=E_Button,command=lambda:had(1)).place(x=125,y=180)
e = Button(bg='white',bd=0,image=E_Button,command=lambda : had(2)).place(x=125,y=210)
g = Button(bg='white',bd=0,image=H_Button,command=icone).place(x=20,y=245)
au = Button(bd=0,image=I_Entry).place(x=150,y=100)

bu = Button(padx=10,pady=150,bd=0,image=I_Entry).place(x=150,y=100)
bu = Button(padx=10,pady=150,bd=0,image=I_Entry).place(x=150,y=40)

al = Label(bg="white",width=55,background=bgg).place(x=145,y=80)
bl = Label(bg="white",width=55,background=bgg).place(x=145,y=140)
cl = Label(bg="white",height=3,background=bgg).place(x=145,y=100)
dl = Label(bg="white",height=3,background=bgg).place(x=535,y=100)

al = Label(bg="white",width=55,background=bgg).place(x=145,y=20)
bl = Label(bg="white",width=55,background=bgg).place(x=145,y=80)
cl = Label(bg="white",height=3,background=bgg).place(x=145,y=40)
dl = Label(bg="white",height=3,background=bgg).place(x=535,y=40)

e = Button(bg='white',bd=0,image=G_Button,command=filep).place(x=530,y=100)

el = Label(bg='white',fg='gray',text="Secure name:",font=('Cooper Black',10)).place(x=15,y=110)
el = Label(bg='white',fg='gray',text="Name new file:",font=('Cooper Black',10)).place(x=15,y=50)
fl = Label(bg='white',fg='gray',text="One file",font=('Cooper Black',10)).place(x=25,y=180)
gl = Label(bg='white',fg='gray',text="No console",font=('Cooper Black',10)).place(x=25,y=210)
#hl = Label(bg='white',fg='gray',text="Icon",font=('Cooper Black',10)).place(x=25,y=240)

be = Entry(win,bd=0,width=45,bg='#ede4e4')
bee = Entry(win,bd=0,width=45,bg='#ede4e4')
be.place(x=160,y=113)
bee.place(x=160,y=53)


win.mainloop()


#Import the required libraries

# from tkinter import *
# from tkinter import ttk

# #Create an instance of Tkinter Frame
# win = Tk()

# #Set the geometry
# win.geometry("700x250")

# # Define a function to return the Input data
# def get_data():
#    label.config(text= entry.get(), font= ('Helvetica 13'))

# #Create an Entry Widget
# entry = Entry(win, width= 42)
# entry.place(relx= .5, rely= .5, anchor= CENTER)


# #Inititalize a Label widget
# label= Label(win, text="", font=('Helvetica 13'))
# label.pack()

# #Create a Button to get the input data
# ttk.Button(win, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

# win.mainloop()