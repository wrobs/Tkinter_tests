from tkinter import *
from tkinter import ttk

#  Issue: I want to create a function that opens a secondary window, user interacts with it, user closes it,
#  and on closing pass info back to the primary window/app  This is a demonstration of the issue I've been having
#  Cause?: best I can tell, the destroy() command in addwin exits the window but does not break the loop, because any 
#  commands after addwin() is called do not execute (or try to) until primary window is closed.  I'm about to put my head
#  through a wall troubleshooting/tinkering with this.
# #########################################################

#  addwin(): This function is intended to open a secondary window with a click counter button and
#  a continue button.  on continue it's supposed to close the window and return the counted value
def addwin(x):
    cont = True
    amt = x
    win = Toplevel()
    win.title('Secondary')
    win.geometry('400x400')
    header = Label(win, text = f'Current amount is {amt}')
    header.pack()
    def add1():
        nonlocal amt
        amt += 1
        header.config(text=f'Current amount is {amt}')
    def on_cont():
        cont = False
        win.destroy()
    b_add = Button(win, text = 'add one', command = add1)
    b_cont = Button(win, text = 'continue', command = on_cont)
    b_add.pack()
    b_cont.pack()
    win.mainloop()
    #   #test: Prints correct amount, but only on closing root window
    #print(amt)
    return amt

    # __main__: open a window, open a secondary with addwin(), and then update primary window/app with value returned from addwin().
    #  check() function is supposed to print new value to test since header update doesn't work.  check() currently just prints
    #  the originally loaded value for r_amt.
if __name__ == "__main__":
    #   #test: creates Tk() window and secondary, passes back correct value on closing tk() window
    #   #if addwin function uses Tk() instead of Toplevel(), this works totally as expected.  Info is printed on hitting (continue)
    #x = addwin(3)
    #print(x) 
    r_amt = 5
    root = Tk()
    root.title("main")
    r_header = Label(root, text = f"imported amount is {r_amt}")
    r_header.pack()
    def import_r_amt():
        global r_amt
        r_amt = addwin(r_amt)
        #   #test: Prints correct amount, but only on closing root window
        #print(r_amt)
        #   #test: does not update header on root as intended, prints library error on closing root
        #r_header.config(text = f"imported amount is {r_amt}")
    def check():
        global r_amt
        print(r_amt)
    b_import = Button(text = "import amount", command = import_r_amt)
    b_import.pack()
    b_check = Button(text = "check amount", command = check)
    b_check.pack()
    root.mainloop()
    


