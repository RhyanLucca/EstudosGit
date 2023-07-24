import customtkinter as ctk #Importando a biblioteca
from tkinter import *

app = ctk.CTk() #Criar a janela

#Configurando a janela principal

app.geometry("700x400")
app.title("Janela 1")
#app._set_appearance_mode("dark")



#Aula 10 - Labels



ctk.CTkLabel(app, text="Curso CustomTkInter - Aula 11 (Entry)", font=("atial bold", 20)).pack(pady=20, padx=5)


entry = ctk.CTkEntry(app, 
                     width=300,
                     placeholder_text="Digite o seu nome completo...",
                     placeholder_text_color="red",
                     fg_color="blue",
                     text_color="teal",
                     font=("Arial bold", 16),
                     border_width=10,
                     border_color="#fff",
                     state="normal",
                     corner_radius=20)#disabled
entry.pack(pady=20)


def pegar():
    print(entry.get())
    entry.delete(0, END)


# def apagar():
#     entry.delete(0, END)
#     pass

ctk.CTkButton(app, width=300, text="Pegar texto", command=pegar).pack(pady=10)

#ctk.CTkButton(app, width=300, text="Apagar texto", command=apagar).pack()






app.mainloop()
