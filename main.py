from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import re

con = sqlite3.connect('Alumni.db')
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS alumni (Alumni_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
Name VARCHAR, Department VARCHAR, Admission_Year VARCHAR, Graduation_Year VARCHAR, Email VARCHAR, 
Phone_Number VARCHAR, Current_Address VARCHAR)''')
con.commit()
con.close()

class Alumni:
    def __init__(self,root):
        self.root=root
        self.root.title("")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="University Alumni Tracking App ", bd=10, relief=GROOVE,
                      font=("times new roman", 36, "bold"), bg="white", fg="firebrick")
        title.pack(side=TOP, fill=X)





root = Tk()
ob=Alumni(root)
root.mainloop()