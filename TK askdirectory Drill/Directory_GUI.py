

# Import widgets from TK
from tkinter import *
from tkinter import filedialog
import tkinter as tk


# Import main file so widgets can be placed inside Master
import Directory_Main




def askdirectory():
    dirname = filedialog.askdirectory()
    if dirname:
        var = StringVar()
        var.set(dirname)

def UserFileInput(status,name):
    optionFrame = Frame(root)
    optionLabel = Label(optionFrame)
    optionLabel["text"] = name
    text = status
    var = StringVar(root)
    var.set(text)
    w = Entry(optionFrame, textvariable= var)
    self.txt_browse = w
    return w, var




# Calls and loads GUI for Master file
def load_gui(self):

    # Entry Box 
    self.txt_browse = Entry(self.master, width=40)
    self.txt_browse.grid(row=2, column=2, columnspan=2, padx=(20,0), pady=(40,5))
    
    # Buttons
    self.btn_browse = Button(self.master, width=12, height=1, text='Browse...', command=askdirectory)
    self.btn_browse.grid(row=2,column=0,padx=(20,0),pady=(40,10))
    self.btn_check = Button(self.master, width=12, height=2, text='Check for files...')
    self.btn_check.grid(row=4,column=0,padx=(20,0),pady=(5,10))
    self.btn_close = Button(self.master, width=12, height=2, text='Close Program')
    self.btn_close.grid(row=4,column=3,padx=(200,10),pady=(10,10))





# Passes into Master file so GUI can be used by it
if __name__ == "__main__":
    pass


