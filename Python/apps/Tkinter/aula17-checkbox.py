import customtkinter as ctk

app = ctk.CTk()
app.title("CTK - Checkbox")
app.geometry("700x500")


ctk.CTkLabel(app, text="Aula 17 - CheckBox", font=("Arial bold", 20)).pack(pady=20)

checkVar = ctk.StringVar(value="off")


def check_value():
    valor = checkVar.get()

    if valor == "on":
        ctk.set_appearance_mode("light")
        print("Tema claro")
    elif valor == "off":
        ctk.set_appearance_mode("dark")
        print("Tema escuro")
    else:
        ctk.set_appearance_mode("system")
        print("Tema do sistema")


checkbox = ctk.CTkCheckBox(app, text="Tema", variable=checkVar, onvalue="on", offvalue="off", command=check_value)

checkbox.pack(pady=20, padx=5)

app.mainloop()