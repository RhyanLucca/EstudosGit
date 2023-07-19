import customtkinter as ctk
from tkinter import *

app = ctk.CTk()

app.title("Janela 1")
app.geometry('700x500')
#app._set_appearance_mode("light")

ctk.CTkLabel(app, text="Aula 14 - Slider", font=("arial bold", 20), fg_color="transparent", bg_color="transparent").pack(pady=20)

def slider_value(value):
    if value == 0:
        slider.configure(fg_color="gray")
    else:
        slider.configure(fg_color="red")
    print(value)

slider = ctk.CTkSlider(app, from_=0, to=100, 
                       command=slider_value,
                       width=500,
                       height=30,
                       corner_radius=20,
                       button_color="red",
                         button_hover_color="green",
                           border_color="pink",
                             bg_color="yellow",
                             fg_color="red",
                               button_length=80,
                                progress_color="blue" )

slider.pack(pady=30, padx=5)


app.mainloop()