import customtkinter as ctk #Importando a biblioteca

app = ctk.CTk() #Criar a janela

#Configurando a janela principal

app.geometry("700x400")
app.title("Janela 1")
#app._set_appearance_mode("system")
app.maxsize(width=900, height=550) #tamanho maximo
app.minsize(width=500, height=250) #tamanho minimo
app.resizable(width=True, height=False) #altera a possibilidade de aumentar e diminuir o tamanho da tela
#app.iconify() #Abre e fecha a janela
#app.deiconify() #Abre novamente a janela


#Customizando os temas da aplicação - 03
app._set_appearance_mode("Dark")
#app._set_appearance_mode("Light")
#app._set_appearance_mode("System")

app.mainloop()

