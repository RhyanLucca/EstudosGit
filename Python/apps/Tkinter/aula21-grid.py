import customtkinter as ctk
from tkinter import *

app = ctk.CTk()
app.geometry("350x250")



label1 = ctk.CTkLabel(master=app, text="Campo de informações 1")
label2 = ctk.CTkLabel(master=app, text="Campo de informações 2")
label3 = ctk.CTkLabel(master=app, text="Campo de informações 3")

entry1 = ctk.CTkEntry(master=app)
entry2 = ctk.CTkEntry(master=app)
entry3 = ctk.CTkEntry(master=app)

btn1 = ctk.CTkButton(master=app, text="Botão teste")



#Definição de posicionamento do widget nas colunas 
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)

label3.grid(row=2, column=0)
entry3.grid(row=2, column=1)

btn1.grid(row=3, column=0)



'''
    #Definição de tamanho de cada linha

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)

    #Definição de tamanho de cada coluna
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
'''
 



#Definição de tamanho de linhas e colunas com LOOP FOR para facilitar a configuração
rows = 4
columns= 2

for i in range(rows):
    app.grid_rowconfigure(i, weight=1)

for i in range(columns):
    app.grid_columnconfigure(i, weight=1)




app.mainloop()