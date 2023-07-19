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

#Aula 07 - Textbox(caixas de textos)

textbox = ctk.CTkTextbox(app, width=300, height=350, scrollbar_button_color="green", scrollbar_button_hover_color="red", border_color="red", border_width=2, corner_radius=15, fg_color="teal", border_spacing=20, activate_scrollbars=True,)
textbox.pack()

textbox.insert("1.0", "Titulo do texto\n\n" + "Olá mundo, estou treinando desenvolvimento de interface gráficas com Python e CustomTkinter vendo videos no youtube\n\n" *20)


app.mainloop()
