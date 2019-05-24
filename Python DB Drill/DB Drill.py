

import sqlite3

conn = sqlite3.connect('DataBase.db')

# creates tbl_files, assigns key and new column 
with conn:
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit() # commits the table creation
conn.close() # closes connection to database 



# list of files for project
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')




        
# this prints the results of the iteration for .txt files
# but when I go to add the results of the iteration into my dB, it is only adding in the world.txt
# and not the Hello.txt as well



# adds files with .txt to dB
conn = sqlite3.connect('DataBase.db')

with conn:
    cur = conn.cursor()
    for files in fileList:
        if ".txt" in files:
            fType = files
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", [fType])
    conn.commit()
conn.close()


# queries data in dB and prints results
conn = sqlite3.connect('DataBase.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_files")
    for row in cur:
        print(row)



