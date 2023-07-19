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

#Aula 06 - TabView (Abas no Ctkinter)

tabview = ctk.CTkTabview(app, width=400, corner_radius=20, border_width=1, border_color="red", #bg_color="purple",
                         fg_color="teal", segmented_button_fg_color="red", segmented_button_selected_color="green", 
                         segmented_button_unselected_hover_color="blue", segmented_button_unselected_color="yellow")

tabview.pack() #Insere o elemento centralizado na tela
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Generos")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(1, weight=1)
tabview.tab("Generos").grid_columnconfigure(0, weight=1)

#Adicionando elementos na nossa tab

text_nome = ctk.CTkLabel(tabview.tab("Nomes"), text="Salvador Eduardo\nEugenio Eduardo\nAntonia Tomocene")
text_nome.pack()

text_idade = ctk.CTkLabel(tabview.tab("Idades"), text="18\n20\n30")
text_idade.pack()

text_genero = ctk.CTkLabel(tabview.tab("Generos"), text="Masculino\nMasculino\nFeminino")
text_genero.pack()

app.mainloop()

