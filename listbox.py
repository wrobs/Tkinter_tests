from tkinter import *
from tkinter import ttk

win = Tk()
win.title("List Box Stuff")

lbox0_title = Label(win, text = "This is a listbox\n(Drag or hold control to select multiple)")
lbox0_title.grid(row = 0, column = 0, padx = 5, pady = 5)

lbox0 = Listbox(win, selectmode = "extended")
for i in range(25):
    lbox0.insert(END, f'Line_{i+1}')
lbox0.grid(row = 1, column = 0, padx = 5, pady = 5)