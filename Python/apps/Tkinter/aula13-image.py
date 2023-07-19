import customtkinter as ctk #Importando a biblioteca
from tkinter import *
from PIL import Image

app = ctk.CTk()

app.title("app teste")
app.geometry("700x400")

ctk.CTkLabel(app, text="Aula 13 - Imagens", font=("Arial bold", 20)).pack(pady=20)

img = ctk.CTkImage(light_image=Image.open(r"apps\RTS\RTSenv\Tkinter\Youtube.png"), dark_image=Image.open(r"apps\RTS\RTSenv\Tkinter\Youtube.png"), size=(20,20))

img1 = ctk.CTkImage(light_image=Image.open(r"apps\RTS\RTSenv\Tkinter\Pessoas-PNG.webp"), dark_image=Image.open(r"apps\RTS\RTSenv\Tkinter\Pessoas-PNG.webp"), size=(200,200))

ctk.CTkLabel(app, text=None, image=img1).pack()


ctk.CTkButton(app, 
              text="Youtube", 
              #command=evento,
              image=img).pack(pady=30)
              #state="disabled"


app.mainloop()