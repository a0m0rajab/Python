from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter as tk
root = Tk()
frame = tk.Frame(root)
frame.pack()
text2 = Text(root, height=5, width=50)#size hesaplama
scroll = Scrollbar(root,command=text2.yview)#text2 her dafe cagirmasini
text2.configure(yscrollcommand=scroll.set)#nasil olacagini yazdim 
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic')) 
text2.tag_configure('big', font=('Verdana', 14))#cizge nasil olacagini bilter
text2.tag_configure('color', foreground='#476042', 
						font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later! "))
text2.insert(END,'         Google Image Downloader  ', 'big')
var = StringVar()
var1 = StringVar()#Choose Path
var2=StringVar()#Not if not seleceted you will got Default as stringini
label = Label( root, textvariable=var, relief=RAISED )#yazacak olna lab
label1 = Label( root, textvariable=var1, relief=RAISED )#Choose Path
label2 = Label( root, textvariable=var2, relief=RAISED )#Not if not seleceted you will got Default as
def callback():
    name= askdirectory() #dosya acmak icin  
    var.set(name)
text2.pack()
var1.set("Choose Path")
var2.set("Not if not seleceted you will got Default as ")
label1.pack(side=tk.LEFT)
Button(text='      FILE OPEN    ', command=callback, fg="red").pack(side=tk.LEFT)
label.pack(side=tk.LEFT)
#label2.pack()
mainloop()