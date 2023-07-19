import customtkinter as ctk

app = ctk.CTk()
app.title("Aula 18 - RadioButton")
app.geometry("700x400")
app.resizable(False, False)


ctk.CTkLabel(app, text="Aula 18 - RadioButton", font=("Arial bold", 20)).pack(pady=20) 


radio_var = ctk.IntVar(value=0)

def radio_event():

    v = radio_var.get()

    if v == 1:
        print("Masculino")
    else:
        print("Feminino")

    #print(radio_var.get())
    pass


radio1 = ctk.CTkRadioButton(app, text="Masculino",
                            command=radio_event,
                            variable= radio_var,
                            value=1 
                            #border_width_checked=20, 
                            #border_width_unchecked=5,
                            #border_color="green"
                            ).pack(pady=20)

radio2 = ctk.CTkRadioButton(app, text="Feminino", 
                            command=radio_event, 
                            variable=radio_var,
                            value=2
                            ).pack(pady=30)

app.mainloop()