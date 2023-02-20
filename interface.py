from tkinter import *
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


#create main window
master = Tk()
master.title("tester")
master.geometry("300x100")


#make a label for the window
label1 = Label(master, text='Hellooooo')
# Lay out label
label1.pack()

# Run forever!
master.mainloop()