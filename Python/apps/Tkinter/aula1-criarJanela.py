import customtkinter as ctk #Importando a biblioteca

app = ctk.CTk() #Criar a janela
# app.geometry("500x500")
# app.title("Janela 1")
# app._set_appearance_mode("system")


button = ctk.CTkButton(app, text="Botao")
button.pack()

app.mainloop()