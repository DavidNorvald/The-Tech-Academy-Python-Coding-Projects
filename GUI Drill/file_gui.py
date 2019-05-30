

# Import widgets from TK
from tkinter import *
import tkinter as tk

# Import main file so widgets can be placed inside Master
import python_file_drill

# Calls and loads GUI for Master file
def load_gui(self):

    # Entry Box
    self.txt_browse = tk.Entry(self.master, width=40, text='')
    self.txt_browse.grid(row=2, column=2, columnspan=2, padx=(20,0), pady=(40,5))
    self.txt_browse2 = tk.Entry(self.master, width=40, text='')
    self.txt_browse2.grid(row=3, column=2, columnspan=2, padx=(20,0), pady=(5,5))

    # Buttons
    self.btn_browse = tk.Button(self.master, width=12, height=1, text='Browse...')
    self.btn_browse.grid(row=2,column=0,padx=(20,0),pady=(40,10))
    self.btn_browse2 = tk.Button(self.master, width=12, height=1, text='Browse...')
    self.btn_browse2.grid(row=3,column=0,padx=(20,0),pady=(5,10))
    self.btn_check = tk.Button(self.master, width=12, height=2, text='Check for files...')
    self.btn_check.grid(row=4,column=0,padx=(20,0),pady=(5,10))
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program')
    self.btn_close.grid(row=4,column=3,padx=(200,10),pady=(10,10))
    

# Passes into Master file so GUI can be used by it
if __name__ == "__main__":
    pass
