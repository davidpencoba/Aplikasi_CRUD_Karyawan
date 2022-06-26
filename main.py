import bdb
from cProfile import label
import imp
from logging import root
from tkinter import font
from tkinter.tix import COLUMN
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


#gui
root = Tk()
root.title("Aplikasi Karyawan Beta Version")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)

#gui 
label=Label(root,text="Aplikasi Database Karyawan",font=('Arial Bold',30))
label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

studidLabel=Label(root,text="Stud ID",font=('Arial',15))
fnameLabel=Label(root,text="Firstname",font=('Arial',15))
lnameLabel=Label(root,text="Lastname",font=('Arial',15))
addressLabel=Label(root,text="Address",font=('Arial',15))
phoneLabel=Label(root,text="Phone",font=('Arial',15))

studidLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
fnameLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
lnameLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
addressLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
phoneLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)

 #textvariabel 
studidEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
fnameEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
lnameEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
addressEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
phoneEntry = Entry(root, width=55, bd=5, font=('Arial', 15))

studidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
fnameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
lnameEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
addressEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
phoneEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn =Button(
    root, text ="Add", padx=65, pady=25, width=10, bd=5, font=('Arial',15), bg="#84f894"
)
updateBtn =Button(
    root, text ="Update", padx=65, pady=25, width=10, bd=5, font=('Arial',15), bg="#84E8F8"
)
deleteBtn =Button(
    root, text ="Delete", padx=65, pady=25, width=10, bd=5, font=('Arial',15), bg="#FF9999"
)
searchBtn =Button(
    root, text ="Search", padx=65, pady=25, width=10, bd=5, font=('Arial',15), bg="#F4FE82"
)
resetBtn =Button(
    root, text ="Reset", padx=65, pady=25, width=10, bd=5, font=('Arial',15), bg="#F398FF"
)
selectBtn =Button(
    root, text ="Select", padx=65, pady=25, width=10, bd=5, font=('Arial',15), bg="#EEEEEE"
)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)


style= ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))
my_tree['columns'] = ("Stud ID","Firstname","Lastname","Address","Phone")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Stud ID", anchor=W, width=170)
my_tree.column("Firstname", anchor=W, width=150)
my_tree.column("Lastname", anchor=W, width=150)
my_tree.column("Address", anchor=W, width=165)
my_tree.column("Phone", anchor=W, width=150)

my_tree.heading("Stud ID", text="Student ID", anchor=W)
my_tree.heading("Firstname", text="Firstname", anchor=W)
my_tree.heading("Lastname", text="Lastname", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)
my_tree.heading("Phone", text="Phone", anchor=W)


root.mainloop()