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

        # ==============All Variables=======================

        self.Alumni_ID_var = StringVar()
        self.Name_var = StringVar()
        self.Department_var = StringVar()
        self.Admission_Year_var = StringVar()
        self.Graduation_Year_var = StringVar()
        self.Email_var = StringVar()
        self.Phone_Number_var = StringVar()
        self.Current_Address_var = StringVar()

        self.Search_By = StringVar()
        self.Search_txt = StringVar()

        # ============Manage Frame==========================
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="firebrick")
        Manage_Frame.place(x=10, y=80, width=480, height=610)

        m_title = Label(Manage_Frame, text="Insert Alumni Information", bg="firebrick", fg="white",
                        font=("times new roman", 28, "bold"))
        m_title.grid(row=0, columnspan=2, pady=16)

        #lbl_Alumni_ID = Label(Manage_Frame, text="Alumni_ID", bg="firebrick", fg="white",font=("times new roman", 20, "bold"))
        #lbl_Alumni_ID.grid(row=1, column=0, pady=8, padx=5, sticky="w")

        #txt_Alumni_ID = Entry(Manage_Frame, textvariable=self.Alumni_ID_var, font=("times new roman", 15, "bold",),bd=5, relief=GROOVE)
        #txt_Alumni_ID.grid(row=1, column=1, pady=8, padx=5, sticky="w")

        lbl_Name = Label(Manage_Frame, text="Name", bg="firebrick", fg="white", font=("times new roman", 20, "bold"))
        lbl_Name.grid(row=2, column=0, pady=10, padx=5, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 15, "bold",), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=5, sticky="w")

        lbl_Department = Label(Manage_Frame, text="Department", bg="firebrick", fg="white", font=("times new roman", 20, "bold"))
        lbl_Department.grid(row=3, column=0, pady=10, padx=5, sticky="w")

        txt_Department = Entry(Manage_Frame, textvariable=self.Department_var, font=("times new roman", 15, "bold",), bd=5,
                          relief=GROOVE)
        txt_Department.grid(row=3, column=1, pady=10, padx=5, sticky="w")

        lbl_Admission_Year = Label(Manage_Frame, text="Admission_Year", bg="firebrick", fg="white", font=("times new roman", 20, "bold"))
        lbl_Admission_Year.grid(row=4, column=0, pady=10, padx=5, sticky="w")

        txt_Admission_Year = Entry(Manage_Frame, textvariable=self.Admission_Year_var, font=("times new roman", 15, "bold",), bd=5,
                          relief=GROOVE)
        txt_Admission_Year.grid(row=4, column=1, pady=10, padx=5, sticky="w")

        lbl_Graduation_Year = Label(Manage_Frame, text="Graduation_Year", bg="firebrick", fg="white",
                                   font=("times new roman", 20, "bold"))
        lbl_Graduation_Year.grid(row=5, column=0, pady=10, padx=5, sticky="w")

        txt_Graduation_Year = Entry(Manage_Frame, textvariable=self.Graduation_Year_var,
                                   font=("times new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_Graduation_Year.grid(row=5, column=1, pady=10, padx=5, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="firebrick", fg="white",
                                    font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=6, column=0, pady=10, padx=5, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var,
                                    font=("times new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_Email.grid(row=6, column=1, pady=10, padx=5, sticky="w")

        lbl_Phone_Number = Label(Manage_Frame, text="Phone_Number", bg="firebrick", fg="white",
                               font=("times new roman", 20, "bold"))
        lbl_Phone_Number.grid(row=7, column=0, pady=10, padx=5, sticky="w")

        txt_Phone_Number = Entry(Manage_Frame, textvariable=self.Phone_Number_var, font=("times new roman", 15, "bold",),
                               bd=5, relief=GROOVE)
        txt_Phone_Number.grid(row=7, column=1, pady=10, padx=5, sticky="w")

        lbl_Current_Address = Label(Manage_Frame, text="Current_Address", bg="firebrick", fg="white",
                                    font=("times new roman", 20, "bold"))
        lbl_Current_Address.grid(row=8, column=0, pady=10, padx=5, sticky="w")

        self.txt_Current_Address = Text(Manage_Frame, width=30, height=3, font=("", 10))
        self.txt_Current_Address.grid(row=8, column=1, pady=10, padx=5, sticky="w")




root = Tk()
ob=Alumni(root)
root.mainloop()