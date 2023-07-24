import customtkinter as ctk #Importando a biblioteca

app = ctk.CTk() #Criar a janela

#Configurando a janela principal

app.geometry("700x400")
app.title("Janela 1")
#app._set_appearance_mode("system")
app.maxsize(width=900, height=550) #tamanho maximo
app.minsize(width=500, height=250) #tamanho minimo
app.resizable(width=True, height=False) #altera a possibilidade de aumentar e diminuir o tamanho da tela

#Aula 05 - Frames

frame1 = ctk.CTkFrame(master = app, width=200, height=330, fg_color="red", bg_color="transparent", 
                      border_width=10, corner_radius=30, border_color="green").place(x=10, y=60)

frame2 = ctk.CTkFrame(master= app, width=200, height=330, fg_color="green", bg_color="yellow", 
                      border_width=5, corner_radius=360, border_color="red").place(x=230, y=60)

frame3 = ctk.CTkFrame(master = app, width=200, height=330, fg_color="blue", bg_color="yellow",  
                      border_width=15, corner_radius=90, border_color="red").place(x=450, y=60)


app.mainloop()

