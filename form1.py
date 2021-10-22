from tkinter import *
from tkinter import ttk
window = Tk()
window.title("welcome to our page")
window.geometry('500x400')
window.configure(background = "black")
ttk.Button(window,text="hello,manoj").grid()
window.mainloop()