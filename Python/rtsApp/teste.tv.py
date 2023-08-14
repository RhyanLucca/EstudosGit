import tkinter as tk
from tkinter.ttk import Treeview

root = tk.Tk()

f1 = tk.Frame(root)
f2 = tk.Frame(root)

f1.grid(column=0, row=0, sticky="ns")
f2.grid(column=1, row=0, sticky="n")
root.rowconfigure(0, weight=1)

Treeview(f1).grid(row=0, column=0, sticky='ns')  # replaced pack with grid method
f1.rowconfigure(0, weight=1)  # Add this newline for Treeview to stretch vertically in f1. 
tk.Button(f2, text="DAT BUTTON IS IN F2").grid(row=0, column=0)
tk.Button(f2, text="DAT BUTTON IS IN F2").grid(row=1, column=0)
tk.Button(f2, text="DAT BUTTON IS IN F2").grid(row=2, column=0)

root.mainloop()