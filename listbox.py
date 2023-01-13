from tkinter import *
from tkinter import ttk

#   THE PURPOSE OF THIS TEST IS TO CREATE ONE OF THOSE SIDE-BY-SIDE LISTBOX
#   WIDGETS WHERE YOU SELECT ITEMS ON THE LEFT LIST AND USE CLICKBUTTONS
#   TO MOVE ITEMS FROM THE LEFT LIST TO THE RIGHT, OR VICE VERSA TO DESELECT.
#   
#   SIDENOTE, I CANNOT FIND A CONSISTENT NAME ONLINE FOR THIS WIDGET.  IF I COULD
#   THEN I PROBABLY WOULD HAVE USED A PACKAGE THAT HAS IT AND WOULD NOT HAVE MADE THIS.

    # create and title GUI window
win = Tk()
win.title("List Box Stuff")

    # intruction header
win_instr = Label(win, text = "Select all that apply.\nDrag or hold CTRL to select multiple")

    # create first listbox for items available to be selected
    # (python list cannot be directly used in listbox object,
    # tkinter's stringvar object must be used as an intermediate)
lbox0_title = Label(win, text = "Available")
lbox0_scroll = Scrollbar(win)
lbox0_contents = []
lbox0_contents_obj = StringVar(value = lbox0_contents)
lbox0 = Listbox(win, selectmode = "extended", yscrollcommand = lbox0_scroll.set, listvariable = lbox0_contents_obj)
lbox0_scroll.config(command = lbox0.yview)

    # populate first listbox's contents list with test strings, 
    # and set that list into stringvar object
for i in range(25):
    lbox0_contents.append(f'Line_{str(i+1).zfill(2)}')
lbox0_contents_obj.set(lbox0_contents)

    # Create second list box for items that have been selected
lbox1_title = Label(win, text = "Selected")
lbox1_scroll = Scrollbar(win)
lbox1_contents = []
lbox1_contents_obj = StringVar(value = lbox1_contents)
lbox1 = Listbox(win, selectmode = "extended", yscrollcommand = lbox1_scroll.set, listvariable = lbox1_contents_obj)
lbox1_scroll.config(command = lbox1.yview)

    # define the function that moves strings between the two listboxes.
    # args are both bools
def move_items(deselect, move_all):
        ## ifelse to pick movement direction.
        ## Aliases the boxes' lists as 
        ## 'source' and 'destination' with Python's
        ## assignment logic.
    if deselect:
        source = lbox1
        source_contents = lbox1_contents
        dest = lbox0
        dest_contents = lbox0_contents    
    else:
        source = lbox0
        source_contents = lbox0_contents
        dest = lbox1
        dest_contents = lbox1_contents
        
        ## Ifelse for moving whole list
    if move_all:
        index_list = list(range(len(source_contents)))
    else:
        index_list = list(source.curselection())
        
        ## movement routine
    index_list.sort(reverse = True)
    for i in index_list:
        e = source_contents.pop(i)
        dest_contents.append(e)
        
        ## sort lists, update listboxes, clear selections
    lbox0_contents.sort()
    lbox1_contents.sort()    
    lbox0_contents_obj.set(lbox0_contents)
    lbox1_contents_obj.set(lbox1_contents)
    if lbox0.size() > 0:
        lbox0.selection_clear(0, lbox0.size() - 1)
    if lbox1.size() > 0:
        lbox1.selection_clear(0, lbox1.size() - 1)
        
    
    # Buttons to command movements.
    # (Command arg takes *function objects*, not *functions*. So if arguments
    # are used then lambdas are necessary.)
b_rightall = Button(text = ">>", command = lambda : move_items(False, True))
b_right = Button(text = ">", command = lambda : move_items(False, False))
b_left = Button(text = "<", command = lambda : move_items(True, False))
b_leftall = Button(text = "<<", command = lambda : move_items(True, True))

    # continue button (not used yet)
b_cont = Button(text = "Continue")
   
    # place elements on window with gridding
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

    # initiate loop
win.mainloop()