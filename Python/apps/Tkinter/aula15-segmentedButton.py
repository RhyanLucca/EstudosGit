import customtkinter as ctk
from tkinter import *

app = ctk.CTk()
app.title("Janela 1")
app.geometry("700x500")

ctk.CTkLabel(app, text="Aula 15 - Segmented Button", font=("Arial bold", 20)).pack(pady=20)


def btn(value):
    print("Segmento selecionado:", value)


segmentBTN = ctk.CTkSegmentedButton(app, 
                                    values=["TKinter", "Django", "Flask"],
                                    command=btn,
                                    fg_color="teal",
                                    selected_color="red",
                                    selected_hover_color="green",
                                    unselected_hover_color="yellow",
                                    unselected_color="blue",
                                    border_width=5,
                                    width=110,
                                    corner_radius=100)

segmentBTN.pack(pady=20)
segmentBTN.set("Django")


app.mainloop()