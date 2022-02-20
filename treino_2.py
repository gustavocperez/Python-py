import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
from sqlite3 import Error

def clear():
    listBox.delete(*listBox.get_children())

custoop = tk.Tk()

cols = ('Ano', 'Mês', 'Valor')
listBox = ttk.Treeview(custoop, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=4, column=0, columnspan=4)

listBox.insert("", "end", values=("2021", "JANEIRO", "0.32"))

label = tk.Label(text="")
label.grid(row=6, column=1)



listBox.selection()

clearButoon = tk.Button(text="Clear", command=clear).grid(row= 5, column=0)

custoop.mainloop()