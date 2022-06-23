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
mt_tree = ttk.Treeview(root)

#gui 
label=Label(root,text="Aplikasi Karyawan",font=('Arial Bold',30))
label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

root.mainloop()