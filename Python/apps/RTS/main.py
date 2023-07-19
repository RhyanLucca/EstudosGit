import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x500")
app.title("Janela 1")
app._set_appearance_mode("dark")

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

button = ctk.CTkButton(app, text="Botao")
button.grid(row=0, column=1, padx=20, pady=0)

app.mainloop()