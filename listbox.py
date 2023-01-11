from tkinter import *
from tkinter import ttk

win = Tk()
win.title("List Box Stuff")

win_instr = Label(win, text = "Select all that apply.\nDrag or hold CTRL to select multiple")
win_instr.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)

lbox0_title = Label(win, text = "Available")
lbox0_scroll = Scrollbar(win)
lbox0_contents = []
lbox0_contents_obj = StringVar(value = lbox0_contents)
lbox0 = Listbox(win, selectmode = "extended", yscrollcommand = lbox0_scroll.set, listvariable = lbox0_contents_obj)

for i in range(25):
    lbox0_contents.append(f'Line_{i+1}')
lbox0_contents_obj.set(lbox0_contents)

lbox1_title = Label(win, text = "Selected")
lbox1_scroll = Scrollbar(win)
lbox1_contents = []
lbox1_contents_obj = StringVar(value = lbox1_contents)
lbox1 = Listbox(win, selectmode = "extended", yscrollcommand = lbox1_scroll.set, listvariable = lbox1_contents_obj)

lbox0_scroll.config(command = lbox0.yview)
lbox1_scroll.config(command = lbox1.yview)

index_list = [1, 2]
def move_items_right():
    index_list.sort(reverse = True)
    for i in index_list:
        e = lbox0_contents.pop(i)
        lbox1_contents.append(e)
    lbox1_contents.sort()    
    lbox0_contents_obj.set(lbox0_contents)
    lbox1_contents_obj.set(lbox1_contents)
        

b_rightall = Button(text = ">>")
b_right = Button(text = ">", command = move_items_right)
b_left = Button(text = "<")
b_leftall = Button(text = "<<")

b_cont = Button(text = "Continue")


    
    


# place elements on window
win_instr.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)
lbox0_title.grid(row = 1, column = 0, padx = 5, pady = 5)
lbox0.grid(row = 2, column = 0, rowspan = 4, sticky = 'ew', padx = 5, pady = 5)
lbox0_scroll.grid(row = 2, column = 1, rowspan = 4, sticky = 'nsw')

b_rightall.grid(row = 2, column = 2, padx = 15)
b_right.grid(row = 3, column = 2)
b_left.grid(row = 4, column = 2)
b_leftall.grid(row = 5, column = 2)

lbox1_title.grid(row = 1, column = 3, padx = 5, pady = 5)
lbox1.grid(row = 2, column = 3, rowspan = 4, sticky = 'ew', padx = 5, pady = 5)
lbox1_scroll.grid(row = 2, column = 4, rowspan = 4, sticky = 'nsw')

b_cont.grid(row = 6, column = 3, columnspan = 2, pady = 20, padx = 5, sticky = 'ew')

win.mainloop()