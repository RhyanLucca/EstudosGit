import customtkinter as ctk #Importando a biblioteca

app = ctk.CTk() #Criar a janela

#Configurando a janela principal

app.geometry("700x400")
app.title("Janela 1")
#app._set_appearance_mode("dark")



#Aula 10 - Labels

ctk.CTkLabel(app, text="Curso CustomTkInter - Aula 10 (Label)", font=("atial bold", 20)).pack(pady=20, padx=5)

ctk.CTkLabel(app, text="Este texto é estático de um label",). pack()


#Trabalhando com label de forma dinamica

#2 forma: Introduzindo texto por entry (Forma mais prática)

def enviar_texto():
    t = entry.get()
    lab.configure(text=str(t))
    pass


lab = ctk.CTkLabel(app, 
                   text="",
                   #width=200, 
                   #height=25, 
                   #text_color="red",
                   font=("Arial bold", 16),
                   fg_color="teal",
                   corner_radius=20,)

lab.pack(pady=10)

entry = ctk.CTkEntry(app, width=200)
entry.pack()


ctk.CTkButton(app, text="Enviar", width=200, command=enviar_texto).pack(pady=10)

"""

#1 forma: Introduzindo texto por input

text_var = ctk.StringVar(value=input("Digite seu nome completo: "))

lab = ctk.CTkLabel(app, 
                   textvariable= text_var,
                   width=200, 
                   height=25, 
                   text_color="red",
                   font=("Arial bold", 16))

lab.pack(pady=10)
"""

app.mainloop()
