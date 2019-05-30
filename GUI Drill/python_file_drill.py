

# Import widgets from TK
from tkinter import *
import tkinter as tk

# Import GUI file for placement/stylings
import file_gui

# Calls parent window so widgets can be placed
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        # GUI file for placement/stylings
        file_gui.load_gui(self)

# Keeps program looping so it doesnt auto close
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
