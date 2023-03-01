import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
from Lock_Unlock import *
import shutil
import webbrowser
file = ""
timer = 0
def choose():
    global file
    file = filedialog.askopenfile(mode='rb', filetypes=[('Zip files', '*.zip')])
def lockorunlock(name,pasword,file):
    if timer == 0:
        zbyner.lizer(1, name, pasword, file)
    else:
        zbyner.lizer(0, name, pasword, file)
def action():
    global timer
    if timer == 1:
        Button(bg='white',bd=0,image=E_Button,command=action).place(x=290,y=350)
        timer = 0
    else:
        timer = 1
        Button(bg='white',bd=0,image=F_Button,command=action).place(x=290,y=350)      
def deleted():
    a = tk.messagebox.askyesno("Delete","Delete All Data?")
    if a == True:
        shutil.rmtree('files')
        time.sleep(.2)
        os.makedirs('files')
bgg = 'white'
win = Tk()
win.title('Zbyner')
win.geometry("689x500")
win.configure(bg="white")
win.resizable(0, 0)
rgifs = os.getcwd()
win.iconbitmap(f"{rgifs}\\data\\zbyner.ico")
I_Entry = PhotoImage(file = f"{rgifs}\\data\\e.gif")
B_Button = PhotoImage(file =f"{rgifs}\\data\\btc.gif")
C_Button = PhotoImage(file =f"{rgifs}\\data\\btb.gif")
D_Button = PhotoImage(file =f"{rgifs}\\data\\rtc.gif")
E_Button = PhotoImage(file =f"{rgifs}\\data\\ro.gif")
F_Button = PhotoImage(file =f"{rgifs}\\data\\rn.gif")
G_Button = PhotoImage(file =f"{rgifs}\\data\\flp.gif")
a = Button(bg='white',bd=0,image=B_Button,command=lambda:lockorunlock(bee.get(), be.get(), file)).place(x=290,y=170)
b = Button(bg='white',bd=0,image=C_Button,command=choose).place(x=290,y=230)
c = Button(bg='white',bd=0,image=D_Button,command=deleted).place(x=290,y=290)
g = Button(bg='white',bd=0,image=E_Button,command=action).place(x=290,y=350)
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
e = Button(bg='white',bd=0,image=G_Button,command=lambda:webbrowser.open(".\\files")).place(x=530,y=100)
el = Label(bg='white',fg='gray',text="Secure name:",font=('Cooper Black',10)).place(x=15,y=110)
el = Label(bg='white',fg='gray',text="Name new file:",font=('Cooper Black',10)).place(x=15,y=50)
be = Entry(win,bd=0,width=60,bg='#ede4e4')
bee = Entry(win,bd=0,width=60,bg='#ede4e4')
be.place(x=160,y=113)
bee.place(x=160,y=53)
win.mainloop()