import customtkinter as ctk
from tkinter import * 
from tkinter import ttk



app = ctk.CTk()
app.geometry("900x500")

columns = 2
for i in range(columns):
   app.grid_columnconfigure(i, weight=1) 

app.grid_rowconfigure(0, weight=1)
app.title("RTSystems")
#ctk._set_appearance_mode("light")
ctk.set_appearance_mode("light")

#app.grid_columnconfigure(0, weight=1)
#app.grid_columnconfigure(1, weight=1)


frame_principal = ctk.CTkFrame(master=app)
frame_principal.pack(side="left", fill="both", expand=True)#.grid(row=0, column=0)
#frame_principal._set_appearance_mode("light")



def btn_frame():

   frame_prod = ctk.CTkFrame(master=frame_principal, corner_radius=False)
   frame_prod.pack(side="left", fill="both", expand=True)#relx=0.1, rely=0.7)#.pack(side="right", fill="both", expand=True)#.grid(row=0, column=0)
   frame_prod.grid_columnconfigure(0, weight=1)
   label_titulo_frame = ctk.CTkLabel(frame_prod, text="CADASTRO DE PRODUTOS", font=("Roboto bold", 20))
   label_titulo_frame.place(relx=0.06, rely=0.05)
   #Nome Produto
   nomeProdLabel = ctk.CTkLabel(frame_prod, text="NOME", font=("roboto", 15))
   nomeProdLabel.place(relx=0.06,rely=0.15)
   nomeProdEntry = ctk.CTkEntry(frame_prod, placeholder_text="INSIRA O NOME DO PRODUTO", width=350, corner_radius=False)
   nomeProdEntry.place(relx=0.06,rely=0.21)
   #Telefone
   valorProdLabel = ctk.CTkLabel(frame_prod, text="VALOR", font=("roboto", 15))
   valorProdLabel.place(relx=0.06,rely=0.31)

   valorProdEntry = ctk.CTkEntry(frame_prod, placeholder_text="INSIRA O VALOR DO PRODUTO", width=350, corner_radius=False)
   valorProdEntry.place(relx=0.06,rely=0.37)
   #Quantidade
   quantidadeProdLabel = ctk.CTkLabel(frame_prod, text="QUANTIDADE", font=("roboto", 15))
   quantidadeProdLabel.place(relx=0.06,rely=0.47)
   quantidadeProdEntry = ctk.CTkEntry(frame_prod, placeholder_text="INSIRA A QUANTIDADE DO PRODUTO", width=350, corner_radius=False)
   quantidadeProdEntry.place(relx=0.06,rely=0.53)
   #Descrição
   descricaoProdLabel = ctk.CTkLabel(frame_prod, text="DESCRIÇÃO", font=("roboto", 15))
   descricaoProdLabel.place(relx=0.06,rely=0.63)
   descricaoProdEntry = ctk.CTkEntry(frame_prod, placeholder_text="INSIRA A DESCRIÇÃO DO PRODUTO", width=350, corner_radius=False)
   descricaoProdEntry.place(relx=0.06,rely=0.69)

   frame_info = ctk.CTkFrame(master=frame_principal, corner_radius=False)
   frame_info.pack(side="right", fill="both", expand=True)#relx=0.1, rely=0.7)#.pack(side="right", fill="both", expand=True)#.grid(row=0, column=0)
   label_titulo_frame = ctk.CTkLabel(frame_info, text="LISTA DE PRODUTOS", font=("Roboto bold", 20))
   label_titulo_frame.place(relx=0.06, rely=0.05)
   tv = ttk.Treeview(frame_info,columns=("ID", "NOME", "VALOR", "QUANTIDADE", "DESCRIÇÃO"), show="headings")
   tv.column("ID", minwidth=0, width=50)
   tv.column("NOME", minwidth=0, width=100)
   tv.column("VALOR", minwidth=0, width=50)
   tv.column("QUANTIDADE", minwidth=0, width=50)
   tv.column("DESCRIÇÃO", minwidth=0, width=100)
   tv.heading("ID", text="ID")
   tv.heading("NOME", text="NOME")
   tv.heading("VALOR", text="VALOR")
   tv.heading("QUANTIDADE", text="QUANTIDADE")
   tv.heading("DESCRIÇÃO", text="DESCRIÇÃO")
   tv.place(relx=0.06, rely=0.15)
   listaProds = [["10", "Ticolé", "2.00", "100", "Ticolé é mt bom"],["11", "Ticolé", "2.00", "100", "Ticolé é mt bom"],["12", "Ticolé", "3.00", "100", "Ticolé é mt bom"]]
   for (id,nome,valor,quantidade,descricao) in listaProds:
      tv.insert('', "end", values=(id, nome, valor, quantidade, descricao))
   btn_cad= ctk.CTkButton(frame_prod, text="CADASTRAR", height=40, font=("roboto bold", 15)).place(relx=0.06 , rely=0.85)
   btn_update= ctk.CTkButton(frame_prod, text="Atualizar", height=40, font=("roboto bold", 15)).place(relx=0.525, rely=0.85)
   btn_get= ctk.CTkButton(frame_info, text="Trazer Informações", height=40, font=("roboto bold", 15)).place(relx=0.06, rely=0.85)
   btn_delete= ctk.CTkButton(frame_info, text="Excluir", height=40, font=("roboto bold", 15)).place(relx=0.533, rely=0.85)



btn_Voltar = ctk.CTkButton(frame_principal, text="Sair",width=100).place(relx=0.001, rely=0.01)



# segmented_button = ctk.CTkSegmentedButton(frame_principal, 
#                                     values=["VOLTAR","CADASTRO DE FORNECEDORES", "CADASTRO DE PRODUTOS", "CADASTRO DE PACOTES"],
#                                     command=btn_frame,
#                                     fg_color="gray",
#                                     selected_color="red",
#                                     font=("roboto bold", 15),
#                                     height=40,
#                                     corner_radius=False,
#                                     unselected_hover_color="black"
#                                     #selected_hover_color="black",
#                                     #unselected_hover_color="yellow",
#                                     #unselected_color="blue",
#                                     #border_width=5,
#                                     #width=110,
#                                     #corner_radius=100)
# )

# segmented_button.pack(fill="x", side="top")



# frame_prod = ctk.CTkFrame(master=frame_principal, corner_radius=False)
# frame_prod.pack(side="left", fill="both", expand=True)#relx=0.1, rely=0.7)#.pack(side="right", fill="both", expand=True)#.grid(row=0, column=0)
# frame_prod.grid_columnconfigure(0, weight=1)


# label_titulo_frame = ctk.CTkLabel(frame_prod, text="CADASTRO DE PRODUTOS", font=("Roboto bold", 20))
# label_titulo_frame.place(relx=0.06, rely=0.05)


# #Nome Produto
# nomeProdLabel = ctk.CTkLabel(frame_prod, text="NOME", font=("roboto", 15))
# nomeProdLabel.place(relx=0.06,rely=0.15)

# nomeProdEntry = ctk.CTkEntry(frame_prod, placeholder_text="INSIRA O NOME DO PRODUTO", width=350, corner_radius=False)
# nomeProdEntry.place(relx=0.06,rely=0.21)


# #Telefone
# valorProdLabel = ctk.CTkLabel(frame_prod, text="VALOR", font=("roboto", 15))
# valorProdLabel.place(relx=0.06,rely=0.31)

# valorProdEntry = ctk.CTkEntry(frame_prod, placeholder_text="INSIRA O VALOR DO PRODUTO", width=350, corner_radius=False)
# valorProdEntry.place(relx=0.06,rely=0.37)


# #Quantidade
# quantidadeProdLabel = ctk.CTkLabel(frame_prod, text="QUANTIDADE", font=("roboto", 15))
# quantidadeProdLabel.place(relx=0.06,rely=0.47)

# quantidadeProdEntry = ctk.CTkEntry(frame_prod, placeholder_text="INSIRA A QUANTIDADE DO PRODUTO", width=350, corner_radius=False)
# quantidadeProdEntry.place(relx=0.06,rely=0.53)

# #Descrição
# descricaoProdLabel = ctk.CTkLabel(frame_prod, text="DESCRIÇÃO", font=("roboto", 15))
# descricaoProdLabel.place(relx=0.06,rely=0.63)

# descricaoProdEntry = ctk.CTkEntry(frame_prod, placeholder_text="INSIRA A DESCRIÇÃO DO PRODUTO", width=350, corner_radius=False)
# descricaoProdEntry.place(relx=0.06,rely=0.69)

# frame_info = ctk.CTkFrame(master=frame_principal, corner_radius=False)
# frame_info.pack(side="right", fill="both", expand=True)#relx=0.1, rely=0.7)#.pack(side="right", fill="both", expand=True)#.grid(row=0, column=0)


# label_titulo_frame = ctk.CTkLabel(frame_info, text="LISTA DE PRODUTOS", font=("Roboto bold", 20))
# label_titulo_frame.place(relx=0.06, rely=0.05)


# tv = ttk.Treeview(frame_info,columns=("ID", "NOME", "VALOR", "QUANTIDADE", "DESCRIÇÃO"), show="headings")
# tv.column("ID", minwidth=0, width=50)
# tv.column("NOME", minwidth=0, width=100)
# tv.column("VALOR", minwidth=0, width=50)
# tv.column("QUANTIDADE", minwidth=0, width=50)
# tv.column("DESCRIÇÃO", minwidth=0, width=100)

# tv.heading("ID", text="ID")
# tv.heading("NOME", text="NOME")
# tv.heading("VALOR", text="VALOR")
# tv.heading("QUANTIDADE", text="QUANTIDADE")
# tv.heading("DESCRIÇÃO", text="DESCRIÇÃO")

# tv.place(relx=0.06, rely=0.15)

# listaProds = [["10", "Ticolé", "2.00", "100", "Ticolé é mt bom"],["11", "Ticolé", "2.00", "100", "Ticolé é mt bom"],["12", "Ticolé", "3.00", "100", "Ticolé é mt bom"]]

# for (id,nome,valor,quantidade,descricao) in listaProds:
#    tv.insert('', "end", values=(id, nome, valor, quantidade, descricao))

# btn_cad= ctk.CTkButton(frame_prod, text="CADASTRAR", height=40, font=("roboto bold", 15)).place(relx=0.06 , rely=0.85)

# btn_update= ctk.CTkButton(frame_prod, text="Atualizar", height=40, font=("roboto bold", 15)).place(relx=0.525, rely=0.85)

# btn_get= ctk.CTkButton(frame_info, text="Trazer Informações", height=40, font=("roboto bold", 15)).place(relx=0.06, rely=0.85)

# btn_delete= ctk.CTkButton(frame_info, text="Excluir", height=40, font=("roboto bold", 15)).place(relx=0.533, rely=0.85)




# segmented_button2 = ctk.CTkSegmentedButton(frame_principal, 
#                                      values=["CRIAR REGISTRO", "VISUALIZAR", "ATUALIZAR REGISTRO", "DELETAR REGISTRO"],
#                                      #command=btn,
#                                      fg_color="gray",
#                                      selected_color="red",
#                                      font=("roboto bold", 15),
#                                      height=40,
#                                      corner_radius=False,
#                                      unselected_hover_color="black"
#                                      #selected_hover_color="black",
#                                      #unselected_hover_color="yellow",
#                                      #unselected_color="blue",
#                                      #border_width=5,
#                                      #width=110,
#                                      #corner_radius=100)
# )

# segmented_button.pack(fill="x", side="top")


#frame_info._set_appearance_mode("light")

#frame_principal.grid_columnconfigure(0, weight=1)
#frame_principal.grid_columnconfigure(1, weight=1)

#frame_prod = ctk.CTkFrame(master=frame_principal, fg_color="green", width=100, height=100).pack()



#frame_lista = ctk.CTkFrame(master=frame_principal, bg_color="red").grid(row=0, column=1)



app.mainloop()