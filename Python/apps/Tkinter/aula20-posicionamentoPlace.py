import customtkinter as ctk


#Place
#Pack
#Grid

app = ctk.CTk()
app.title("Aula 20 - Posicionamento Place")
app.geometry("700x400")


btn1 = ctk.CTkButton(app, text="Botão1")
btn1.place(relx=0.4, rely=0.2)

btn2 = ctk.CTkButton(app, text="Botão2")
btn2.place(relx=0.8, rely=0.4)

btn3 = ctk.CTkButton(app, text="Botão3")
btn3.place(relx=0.1, rely=0.2) #relx e rely equivalem a 10% e 20% do tamamnho da tela




app.mainloop()