




# Import widgets from TK
from tkinter import filedialog
from tkinter import *
import tkinter as tk

# Import main file and GUI
import Directory_Main
import Directory_GUI



def browse_func(self):
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

    
def button_press_handle(callback=None):
    if callback:
        callback(browse_func(self))


if __name__ == "__main__":
    pass
