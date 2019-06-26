
import shutil
import os
import time
import sqlite3
from tkinter import filedialog
from tkinter import *
import tkinter as tk


path = 'C:\\A\\'
source = os.listdir(path) #listdir() method

mtime = os.path.getmtime(path) # getmtime() method
local_time = time.ctime(mtime)

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:

        if ".txt" in file:
            print("Files in Directory: ",os.path.join(r, file), local_time) # path.join() method
                # prints .txt files and mtime to console
            

conn = sqlite3.connect('DataBaseDrill.db')
# creates tbl_file, assigns key and new column 
with conn:
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT, \
        col_fileTime TEXT \
        )")
    conn.commit() # commits the table creation
conn.close() # closes connection to database

fileList = 'A File.txt', 'Another File.txt', 'Hello.txt', 'index.html', 'Scripts.js', 'Style.css', 'webpage.htlm', 'World.txt', 'Yet Another File.txt'  


# adds files with .txt to dB
conn = sqlite3.connect('DataBaseDrill.db')

with conn:
    cur = conn.cursor()
    for files in fileList:
        if ".txt" in files:
            fType = files
            fTime = local_time
            cur.execute("INSERT INTO tbl_file(col_fileName, col_fileTime) VALUES(?,?)", [fType,fTime])
    conn.commit()
conn.close()





class ParentWindow(Frame): 
    def __init__ (self, master): 
        Frame.__init__(self)
        self.folderPath = StringVar()
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(450, 175))
        self.master.title('Directory Drill')
        
        # Label Box 
        self.txt_browse = Entry(self.master, width=40, textvariable=self.folderPath)
        self.txt_browse.grid(row=2, column=2, columnspan=2, padx=(20,0), pady=(40,5))
        
        # Buttons
        self.btn_browse = Button(self.master, width=12, height=1, text='Browse...', command=self.setFolderPath)
        self.btn_browse.grid(row=2,column=0,padx=(20,0),pady=(40,10))
        self.btn_transfer = Button(self.master, width=12, height=2, text='Transfer Files', command = self.fileTransfer)
        self.btn_transfer.grid(row=4,column=0,padx=(20,0),pady=(5,10))
        self.btn_close = Button(self.master, width=12, height=2, text='Close Program')
        self.btn_close.grid(row=4,column=3,padx=(200,10),pady=(10,10))




    def setFolderPath(self):
            folder_selected = filedialog.askdirectory()
            self.folderPath.set(folder_selected)
            
    def folder_path(self):
        return self.folderPath.get()  


    def fileTransfer(self):
        for files in source:
            if files.endswith(".txt"):
                destination = 'C:\\B\\'
                try:
                    os.makedirs(destination); # creates the destination folder
                except:
                    shutil.copy(files, destination) # Shutil's copy/move() method
                    print("Transfered: ", files, " to: ", destination, " on: ", local_time)




# queries data in dB and prints results
conn = sqlite3.connect('DataBaseDrill.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_file")
    for row in cur:
        print("DataBase Entry: ",row)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()










