from tkinter import *
from tkinter import ttk
window = Tk()
window.title("welcome to registeration form")
window.geometry('450x300')
window.configure(background  = "blue")
a = Label(window ,text = "first name").grid(row = 0,column = 0)
b = Label(window ,text = "last name").grid(row = 1,column = 0)
c = Label(window ,text = "email id").grid(row = 2,column = 0)
d = Label(window ,text = "contact number").grid(row = 3,column = 0)
a1= Entry(window). grid(row = 0,column = 1)
b1= Entry(window). grid(row = 1,column = 1)
c1= Entry(window). grid(row = 2,column = 1)
d1= Entry(window). grid(row = 3,column = 1)
def clicked():
    res ="welcome to" + text.get()
    Lbl.configure(text= res)
btn = ttk.Button(window ,text='submit').grid(row=4,column=0)
window.mainloop()