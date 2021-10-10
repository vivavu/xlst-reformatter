from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os, re

window = Tk()

window.title("tag replacer")

window.geometry('250x100')
msg1 = 'This app replace the tag "<br/>" with'
msg2 = '<br style="mso-data-placement:same-cell;"/>'
lbl1 = Label(window, text=msg1)
lbl2 = Label(window, text=msg2)
lbl3 = Label(window)

lbl1.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
lbl3.grid(column=0, row=2)

def clicked():
    #get 1st file
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file


    # Read in the file
    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('<br/>', '<br style="mso-data-placement:same-cell;"/>')

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)

    btn.configure(text="It's done")

btn = Button(window, text="Select File", command=clicked)

btn.grid(column=0, row=3)

window.mainloop()