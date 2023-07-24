import customtkinter as ctk #Importando a biblioteca
from tkinter import *
from PIL import Image
app = ctk.CTk() #Criar a janela

#Configurando a janela principal

app.geometry("700x400")
app.title("Janela 1")
#app._set_appearance_mode("light")

ctk.CTkLabel(app, text="Aula 12 - Button", font=("Arial bold", 20)).pack(pady=20, padx=5)

def evento():
    print("O botão foi clicado")
    pass

# def nova_tela():
#     nova_janela = ctk.CTkToplevel(app, fg_color="red") #fg_color: cor de plano de fundo
#     nova_janela.geometry("300x300")


img = ctk.CTkImage(light_image=Image.open(r"C:\Users\rhyan.gaudino\Desktop\RhyanLucca\Automações Rhyan\apps\RTS\RTSenv\Tkinter\Youtube.png"), dark_image=Image.open(r"C:\Users\rhyan.gaudino\Desktop\RhyanLucca\Automações Rhyan\apps\RTS\RTSenv\Tkinter\Youtube.png"), size=(80,80))


ctk.CTkButton(app, 
              text="Clique em mim", 
              command=evento,
              width=300,
              height=50,
              fg_color="teal",
              bg_color="transparent",
              hover_color="Green",
              corner_radius=40,
              text_color="white",
              font=("Arial bold", 18),
              border_color="red",
              border_width=5,
              border_spacing=2,
              state="normal").pack(pady=30)
              #state="disabled"


ctk.CTkButton(app, 
              text="Youtube", 
              command=evento,
              width=300,
              height=50,
              fg_color="teal",
              bg_color="transparent",
              hover_color="Green",
              corner_radius=40,
              text_color="red",
              font=("Arial bold", 18),
              border_color="red",
              border_width=5,
              border_spacing=2,
              state="normal",
              image=img).pack(pady=30)
              #state="disabled"


app.mainloop()