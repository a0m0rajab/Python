from tkinter import *
import tkinter.messagebox as tm
from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter as tk
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
         
        self.label_username = Label(self, text=" Path  ")
        self.label_password = Label(self, text="  Keyword  ")
        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")
        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)


        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Choose Path", command=self.callback)
        self.logbtn.grid(columnspan=2)
         
        self.pack()
        #var = StringVar()
    def callback(self):
        name= askdirectory() #dosya acmak icin  
        self.entry_username.insert(0,name)
        self.entry_username.grid(x=100)



root = Tk()
root.geometry("500x400")
lf = LoginFrame(root)
root.mainloop()
#https://stackoverflow.com/questions/28156719/how-can-i-integrate-tkinter-with-python-log-in-screen