from tkinter import *

def clicked():
    b.grid_forget()

w = Tk()
w.title('@')
w.geometry('650x500')
b = Button(w, command=clicked)
b.grid()
w.mainloop()