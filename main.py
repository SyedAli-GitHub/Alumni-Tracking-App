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
        Manage_Frame.place(x=10, y=80, width=470, height=610)

        m_title = Label(Manage_Frame, text="Insert Alumni Information", bg="firebrick", fg="white",font=("times new roman", 28, "bold"))
        m_title.grid(row=0, columnspan=2, pady=16)

        #lbl_Alumni_ID = Label(Manage_Frame, text="Alumni_ID", bg="firebrick", fg="white",font=("times new roman", 20, "bold"))
        #lbl_Alumni_ID.grid(row=1, column=0, pady=8, padx=5, sticky="w")

        #txt_Alumni_ID = Entry(Manage_Frame, textvariable=self.Alumni_ID_var, font=("times new roman", 15, "bold",),bd=5, relief=GROOVE)
        #txt_Alumni_ID.grid(row=1, column=1, pady=8, padx=5, sticky="w")

        lbl_Name = Label(Manage_Frame, text="Name" "*", bg="firebrick", fg="white", font=("times new roman", 19, "bold"))
        lbl_Name.grid(row=2, column=0, pady=10, padx=5, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 15, "bold",), bd=5,relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=5, sticky="w")

        lbl_Department = Label(Manage_Frame, text="Department" "*", bg="firebrick", fg="white", font=("times new roman", 19, "bold"))
        lbl_Department.grid(row=3, column=0, pady=10, padx=5, sticky="w")

        txt_Department = Entry(Manage_Frame, textvariable=self.Department_var, font=("times new roman", 15, "bold",), bd=5,relief=GROOVE)
        txt_Department.grid(row=3, column=1, pady=10, padx=5, sticky="w")

        lbl_Admission_Year = Label(Manage_Frame, text="Admission_Year" "*", bg="firebrick", fg="white", font=("times new roman", 19, "bold"))
        lbl_Admission_Year.grid(row=4, column=0, pady=10, padx=5, sticky="w")

        txt_Admission_Year = Entry(Manage_Frame, textvariable=self.Admission_Year_var, font=("times new roman", 15, "bold",), bd=5,relief=GROOVE)
        txt_Admission_Year.grid(row=4, column=1, pady=10, padx=5, sticky="w")

        lbl_Graduation_Year = Label(Manage_Frame, text="Graduation_Year" "*", bg="firebrick", fg="white",font=("times new roman", 19, "bold"))
        lbl_Graduation_Year.grid(row=5, column=0, pady=10, padx=5, sticky="w")

        txt_Graduation_Year = Entry(Manage_Frame, textvariable=self.Graduation_Year_var,font=("times new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_Graduation_Year.grid(row=5, column=1, pady=10, padx=5, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="firebrick", fg="white",font=("times new roman", 19, "bold"))
        lbl_Email.grid(row=6, column=0, pady=10, padx=5, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var,font=("times new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_Email.grid(row=6, column=1, pady=10, padx=5, sticky="w")

        lbl_Phone_Number = Label(Manage_Frame, text="Phone_Number", bg="firebrick", fg="white",font=("times new roman", 19, "bold"))
        lbl_Phone_Number.grid(row=7, column=0, pady=10, padx=5, sticky="w")

        txt_Phone_Number = Entry(Manage_Frame, textvariable=self.Phone_Number_var, font=("times new roman", 15, "bold",),bd=5, relief=GROOVE)
        txt_Phone_Number.grid(row=7, column=1, pady=10, padx=5, sticky="w")

        lbl_Current_Address = Label(Manage_Frame, text="Current_Address", bg="firebrick", fg="white",font=("times new roman", 19, "bold"))
        lbl_Current_Address.grid(row=8, column=0, pady=10, padx=5, sticky="w")

        self.txt_Current_Address = Text(Manage_Frame, width=30, height=3, font=("", 10))
        self.txt_Current_Address.grid(row=8, column=1, pady=10, padx=5, sticky="w")

        # ==============Button Frame========================

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="firebrick")
        btn_Frame.place(x=5, y=520, width=454)

        addbtn = Button(btn_Frame, text="Add", font="bold", width=10, command=self.add_alumni).grid(row=0, column=0, padx=6, pady=10)
        updatebtn = Button(btn_Frame, text="Update", font="bold", width=10, command=self.update_data).grid(row=0, column=1, padx=5,pady=10)
        deletebtn = Button(btn_Frame, text="Delete", font="bold", width=10, command=self.delete_data).grid(row=0, column=2, padx=5,                                                                                      pady=10)
        clearbtn = Button(btn_Frame, text="Clear", font="bold", width=10, command=self.clear).grid(row=0, column=3, padx=6, pady=10)

        # ============Detail Frame==========================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="firebrick")
        Detail_Frame.place(x=490, y=80, width=900, height=610)

        lbl_search = Label(Detail_Frame, text="Search By", bg="firebrick", fg="white",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.Search_By, width=15,font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Alumni_ID", "Name", "Department", "Admission_Year", "Graduation_Year", "Email", "Phone_Number", "Current_Address")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_Frame, textvariable=self.Search_txt, width=20, font=("times new roman", 10, "bold"),bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", font="bold", width=12, pady=3, command=self.search_data).grid(row=0,column=3,padx=16,pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", font="bold", width=12, pady=3, command=self.fetch_data).grid(row=0,column=4,padx=16,pady=10)

        # =========Table Frame======================

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="firebrick")
        Table_Frame.place(x=5, y=70, width=860, height=520)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.alumni_table = ttk.Treeview(Table_Frame, columns=("Alumni_ID", "Name", "Department", "Admission_Year", "Graduation_Year", "Email", "Phone_Number", "Current_Address"),xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.alumni_table.xview)
        scroll_y.config(command=self.alumni_table.yview)
        self.alumni_table.heading("Alumni_ID", text="Alumni_ID")
        self.alumni_table.heading("Name", text="Name")
        self.alumni_table.heading("Department", text="Department")
        self.alumni_table.heading("Admission_Year", text="Admission_Year")
        self.alumni_table.heading("Graduation_Year", text="Graduation_Year")
        self.alumni_table.heading("Email", text="Email")
        self.alumni_table.heading("Phone_Number", text="Phone_Number")
        self.alumni_table.heading("Current_Address", text="Current_Address")
        self.alumni_table["show"] = 'headings'
        self.alumni_table.column("Alumni_ID", width=60)
        self.alumni_table.column("Name", width=110)
        self.alumni_table.column("Department", width=70)
        self.alumni_table.column("Admission_Year", width=90)
        self.alumni_table.column("Graduation_Year", width=95)
        self.alumni_table.column("Email", width=130)
        self.alumni_table.column("Phone_Number", width=90)
        self.alumni_table.column("Current_Address", width=160)
        self.alumni_table.pack(fill=BOTH, expand=1)
        self.alumni_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_alumni(self):
        match_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',self.Email_var.get())
        match_phone = re.match('^(\+([0-9]){1,2})?((((([0-9]){2,3})[-.]){1,2}([0-9]{4,10}))|([0-9]{10,16}))$',self.Phone_Number_var.get())
        if self.Name_var.get() == "" or self.Department_var.get() == "" or self.Admission_Year_var.get() == "" or self.Graduation_Year_var.get() == "":
            messagebox.showerror("Error", "Name, Department, Admission_Year and Graduation_Year Fields Are Required!!")

        elif match_email==None:
            messagebox.showerror("Error", "Valid Email Address Is Required!!")

        elif match_phone==None:
            messagebox.showerror("Error", "Valid Phone Number With Country And City Code Is Required!!")

        else:
            con = sqlite3.connect('Alumni.db')
            c = con.cursor()
            c.execute("INSERT INTO alumni VALUES (NULL,?,?,?,?,?,?,?)", (
                                                                                    self.Name_var.get(),
                                                                                    self.Department_var.get(),
                                                                                    self.Admission_Year_var.get(),
                                                                                    self.Graduation_Year_var.get(),
                                                                                    self.Email_var.get(),
                                                                                    self.Phone_Number_var.get(),
                                                                                    self.txt_Current_Address.get('1.0',
                                                                                                                 END)
                                                                                    ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success!", "Records Have Been Inserted Successfully!!")



    def fetch_data(self):
        con = sqlite3.connect('Alumni.db')
        c = con.cursor()
        c.execute("select * from alumni")
        rows=c.fetchall()
        if len(rows)!=0:
            self.alumni_table.delete(*self.alumni_table.get_children())
            for row in rows:
                self.alumni_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear(self):
        self.Alumni_ID_var.set("")
        self.Name_var.set("")
        self.Department_var.set("")
        self.Admission_Year_var.set("")
        self.Graduation_Year_var.set("")
        self.Email_var.set("")
        self.Phone_Number_var.set("")
        self.txt_Current_Address.delete('1.0', END)

    def get_cursor(self, ev):
        cursor_row = self.alumni_table.focus()
        contents = self.alumni_table.item(cursor_row)
        row = contents['values']
        self.Alumni_ID_var.set(row[0])
        self.Name_var.set(row[1])
        self.Department_var.set(row[2])
        self.Admission_Year_var.set(row[3])
        self.Graduation_Year_var.set(row[4])
        self.Email_var.set(row[5])
        self.Phone_Number_var.set(row[6])
        self.txt_Current_Address.delete("1.0", END)
        self.txt_Current_Address.insert(END, row[7])

    def update_data(self):
        match_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',self.Email_var.get())
        match_phone = re.match('^(\+([0-9]){1,2})?((((([0-9]){2,3})[-.]){1,2}([0-9]{4,10}))|([0-9]{10,16}))$',self.Phone_Number_var.get())

        if match_email==None:
            messagebox.showerror("Error", "Valid Email Address Is Required!!")

        elif match_phone==None:
            messagebox.showerror("Error", "Valid Phone Number With Country And City Code Is Required!!")

        else:
            con = sqlite3.connect('Alumni.db')
            c = con.cursor()
            c.execute("UPDATE alumni SET Name=?,Department=?,Admission_Year=?,Graduation_Year=?,Email=?,Phone_Number=?,Current_Address=? where Alumni_ID=?",(
                                                                                                                                            self.Name_var.get(),
                                                                                                                                            self.Department_var.get(),
                                                                                                                                            self.Admission_Year_var.get(),
                                                                                                                                            self.Graduation_Year_var.get(),
                                                                                                                                            self.Email_var.get(),
                                                                                                                                            self.Phone_Number_var.get(),
                                                                                                                                            self.txt_Current_Address.get('1.0',END),
                                                                                                                                            self.Alumni_ID_var.get()
                                                                                                                                            ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success!", "Records Have Been Updated Successfully!!")

    def delete_data(self):
        con = sqlite3.connect('Alumni.db')
        c = con.cursor()
        c.execute("delete from alumni where Alumni_ID=?",(self.Alumni_ID_var.get(),))
        c.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME = 'alumni'")
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = sqlite3.connect('Alumni.db')
        c = con.cursor()

        c.execute("SELECT * from alumni where "+str(self.Search_By.get())+" LIKE '%"+str(self.Search_txt.get())+"%'")
        rows=c.fetchall()
        if len(rows)!=0:
            self.alumni_table.delete(*self.alumni_table.get_children())
            for row in rows:
                self.alumni_table.insert('', END, values=row)
                con.commit()
        con.close()




root = Tk()
ob=Alumni(root)
root.iconbitmap("C:/Users/User/PycharmProjects/University Alumni Tracking App/BUET ALUMNI TRACKING APP.ico")
root.mainloop()