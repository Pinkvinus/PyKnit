# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Choose a profile")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text = "Waist")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10, textvariable="in cm")
txt.grid(column =1, row =0)


# function to display user text when 
# button is clicked
def clicked():

    res = int(txt.get())

# button widget with red color text inside
btn = Button(root, text = "update measurements" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.mainloop()
