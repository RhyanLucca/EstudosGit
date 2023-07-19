import customtkinter as ctk
from tkinter import *

app = ctk.CTk()
app.title("CustomTkinter - Switch")
app.geometry("700x500")


ctk.CTkLabel(app, text="Aula 16 - Switch", font=("Arial bold", 20)).pack(pady=20)


switch_var = ctk.StringVar(value="on")

def event():

    if switch_var.get() == "Ativado":
        ctk.set_appearance_mode("Light")
    elif switch_var.get()== "Desativado":
        ctk.set_appearance_mode("Dark")
    else:
        ctk.set_appearance_mode("System")  
    #print("O switch esta:", switch_var.get())

switch = ctk.CTkSwitch(app,
                       text="Switch",
                       #text=None
                       command=event,
                       variable=switch_var,
                       onvalue="Ativado",
                       offvalue="Desativado",
                       width=30,
                       fg_color="teal",
                       button_length=5)
switch.pack(pady=20)

app.mainloop()