import customtkinter as ctk #Importando a biblioteca

app = ctk.CTk() #Criar a janela

#Configurando a janela principal

app.geometry("700x400")
app.title("Janela 1")
#app._set_appearance_mode("system")
app.maxsize(width=900, height=550) #tamanho maximo
app.minsize(width=500, height=250) #tamanho minimo
app.resizable(width=True, height=False) #altera a possibilidade de aumentar e diminuir o tamanho da tela
app._set_appearance_mode("System")

#Aula 08 - Dialog (Caixa de dialogo)

def abrir_dialog():
    dialog = ctk.CTkInputDialog(title="Caixa de dialogo", text="Digite seu número de celular") #entry_border_color="red", entry_fg_color="red",text_color="teal", button_fg_color="green", fg_color="#129845")
    print("Numero de celular Inserido: ",dialog.get_input())




btn = ctk.CTkButton(app, text="Abrir caixa de dialogo", command=abrir_dialog)
btn.pack()


app.mainloop()
