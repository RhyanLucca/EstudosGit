import customtkinter as ctk #Importando a biblioteca

app = ctk.CTk() #Criar a janela

#Configurando a janela principal

app.geometry("700x400")
app.title("Janela 1")

label = ctk.CTkLabel(app, text="Menu de opções. Aula - 09", font=("atial bold", 20)).pack(pady=20, padx=5)


#Aula 09 - Menu de opções

ctk.CTkLabel(app, text="Escolha o seu mês de nascimento", font=("arial bold", 14)).pack()


mes_var = ctk.StringVar(value="Escolha um mês")

def mes_nascimento(escolha):
    print(f"O seu mês de nascimento é: {escolha}")


mes =ctk.CTkOptionMenu(app, width=140, height=28,
                  values=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembo", "Outubro", "Novembro", "Dezembro"],
                  command=mes_nascimento,
                  variable=mes_var,
                  corner_radius=20,
                  fg_color="red",button_color="green",
                  button_hover_color="teal", 
                  dropdown_fg_color= "teal",
                  dropdown_text_color="yellow",
                  dropdown_font=("Arial Bold", 15),
                  dropdown_hover_color="green")

mes.pack(pady=10)
#mes.set("Selecione um mês")



"""
mes =ctk.CTkOptionMenu(app, width=140, height=28,
                  values=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembo", "Outubro", "Novembro", "Dezembro"],
                  command=mes_nascimento)

mes.pack(pady=10)
mes.set("Selecione um mês")
"""

app.mainloop()
