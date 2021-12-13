#import tkinter
#import time
from tkinter import *
from tkinter.ttk import *

from time import strftime

#create a UI
root = Tk()
#create a title
root.title("Clock")
#here we have to define a function to get our time
def time():
    string = strftime('%H:%M:%S %p') #hour,min,sec,am/pm
    label.config(text=string)
    label.after(1000,time)#set these make label

#create a lablel to store our clock
#first perameter will be root and second one is font
#font name and size and background and foreground will be set (*you have to download font
label = Label(root, font=("hello_almeida",80), background = "black", foreground ="cyan")
#now pack our label
label.pack(anchor='center')
time()#calling our time function

mainloop()