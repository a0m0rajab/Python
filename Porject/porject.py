from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter as tk
root = Tk()
frame = tk.Frame(root)
root.geometry("500x400")
text2 = Text(root, height=5, width=50)#size hesaplama
scroll = Scrollbar(root,command=text2.yview)#text2 her dafe cagirmasini
text2.configure(yscrollcommand=scroll.set)#nasil olacagini yazdim 
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic')) 
text2.tag_configure('big', font=('Verdana', 14))#cizge nasil olacagini bilter
text2.tag_configure('color', foreground='#476042', font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later! "))
text2.insert(END,'         Google Image Downloader  ', 'big')


var = StringVar()
var3 = StringVar()#key word 
var1 = StringVar()#Choose Path
var2=StringVar()#Not if not seleceted you will got Default as stringini
var4=StringVar()
keywordvar=StringVar()


keywordlabel= Label( root, textvariable=keywordvar, relief=RAISED )#yazacak olna lab
label = Label( root, textvariable=var, relief=RAISED )#yazacak olna lab
label1 = Label( root, textvariable=var1, relief=RAISED )#Choose Path
label2 = Label( root, textvariable=var2, relief=RAISED )#Not if not seleceted you will got Default as
label3 = Label( root, textvariable=var3, relief=RAISED )#Not if not seleceted you will got Default as
label4= Label( root, textvariable=var4, relief=RAISED )#key  word





def callback():
    name= askdirectory() #dosya acmak icin  
    var.set(name)

text2.pack()

def test():
    
	keywordvar.set("Hello word")


var1.set("Choose Path")
var3.set(" Key word ")
label1.place(y=90)
Button(text="Path", command=callback, fg="red").pack()
label.pack()


label3.place(y=130)
Button(text=' key word ', command=test, fg="green").pack()
keywordlabel.pack()
mainloop()