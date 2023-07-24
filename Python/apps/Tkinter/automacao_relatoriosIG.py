import customtkinter as ctk
from tkinter import *
from PIL import Image


janela = ctk.CTk()

class Aplication:
        
    def __init__(self):
        self.janela=janela
        self.conf_janela()
        self.tema()
        self.janela_relatorios()
        self.atualizar_relatorios()
        self.janela.mainloop()
        

    def conf_janela(self):
        self.janela.title("Automação de Relatórios")
        self.janela.geometry("800x550")
        self.janela.resizable(False, False)
        #self.janela.resizable(False, False)


    def tema(self):
        #self.janela._set_appearance_mode("system")
        ctk.set_appearance_mode("system")
        #self.janela.configure(background="red")
        #ctk.configure(bg="red")

    
    def janela_relatorios(self):
        
        img = ctk.CTkImage(light_image=Image.open(r"apps\RTS\RTSenv\Tkinter\franco_Contabilidade_Colorido-removebg-preview.png"), size=(130,130))
        imglabel = ctk.CTkLabel(self.janela, text=None, image=img).place(relx=0.7, rely=0.675)


        ctk.CTkLabel(self.janela, text="Atualização de relatórios Franco Contabilidade", font=("roboto bold", 25)).place(relx=0.05, rely=0.05)#.grid(row=0, column=0)
        ctk.CTkLabel(self.janela, text="____________________________________________________________________________",text_color="#14a6e1", font=("Arial bold", 25)).place(relx=0., rely=0.1)#.grid(row=0, column=0)


        cb_relatorio_infra = ctk.CTkCheckBox(master=self.janela, text="Intranet-Suporte", fg_color="#14a6e1")
        cb_relatorio_infra.place(relx=0.1, rely=0.25)#place(relx=0.1, rely=0.1)
    

        cb_relatorio_desligamento = ctk.CTkCheckBox(master=self.janela, fg_color="#14a6e1" , text="Intranet-Desligamentos") #Ultimo
        cb_relatorio_desligamento.place(relx=0.1, rely=0.40)


        cb_relatorio_empresas = ctk.CTkCheckBox(master=self.janela, text="Intranet-Empresas", fg_color="#14a6e1", hover_color="#0494dc")
        cb_relatorio_empresas.place(relx=0.1, rely=0.55)

        cb_relatorio_responsaveis = ctk.CTkCheckBox(master=self.janela, text="Intranet-Responsáveis", fg_color="#14a6e1", hover_color="#0494dc") 
        cb_relatorio_responsaveis.place(relx=0.1, rely=0.70)

        cb_relatorio_obrigacoes = ctk.CTkCheckBox(master=self.janela, text="Consulta-Obrigações", fg_color="#14a6e1", hover_color="#0494dc")
        cb_relatorio_obrigacoes.place(relx=0.4, rely=0.25)

        cb_relatorio_workFlow = ctk.CTkCheckBox(master=self.janela, text="Intranet-Workflow", fg_color="#14a6e1", hover_color="#0494dc")
        cb_relatorio_workFlow.place(relx=0.4, rely=0.40)

        cb_relatorio_maquinas = ctk.CTkCheckBox(master=self.janela, text="Intranet-Maquinas", fg_color="#14a6e1", hover_color="#0494dc")
        cb_relatorio_maquinas.place(relx=0.4, rely=0.55)

        cb_relatorio_timeSheet = ctk.CTkCheckBox(master=self.janela, text="Intranet-TimeSheet", fg_color="#14a6e1", hover_color="#0494dc")
        cb_relatorio_timeSheet.place(relx=0.4, rely=0.70)

        cb_relatorio_tributacao = ctk.CTkCheckBox(master=self.janela, text="Consulta-Tributação", fg_color="#14a6e1", hover_color="#0494dc")
        cb_relatorio_tributacao.place(relx=0.7, rely=0.25)

        cb_relatorio_tributacao = ctk.CTkCheckBox(master=self.janela, text="Intranet-Servidores", fg_color="#14a6e1", hover_color="#0494dc")
        cb_relatorio_tributacao.place(relx=0.7, rely=0.40)

        cb_relatorio_tributacao = ctk.CTkCheckBox(master=self.janela, text="Intranet-Descarte", fg_color="#14a6e1", hover_color="#0494dc")
        cb_relatorio_tributacao.place(relx=0.7, rely=0.55)

        ctk.CTkLabel(self.janela, text="Desenvolvido por: Rhyan Lucca Borges Galdino", font=("arial bold", 10)).place(relx=0.01, rely=0.95)

    def atualizar_relatorios(self):
        btn_atualizar = ctk.CTkButton(master=self.janela, text="Atualizar relatórios", hover_color="#0494dc", border_color="#0494dc", border_width=3,  fg_color="#14a6e1", width=300, height=40, font=("Roboto", 15))
        btn_atualizar.place(relx=0.1, rely=0.87)


Aplication()

