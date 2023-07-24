import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image
from metodos_relatorios import *

tela = ctk.CTk()



class Aplication():


    def __init__(self):
        self.tela=tela
        self.tela_conf()
        self.main_frame_style()
        self.tela.mainloop()
        

    def tela_conf(self):
        self.tela.title("Franco contabilidade")
        self.tela.geometry("950x750")
        self.tela.minsize(750,500)
        self.tela.iconbitmap("icone.ico")
        #self.tela.attributes("-fullscreen", True)
        ctk.set_appearance_mode("light")


    def main_frame_style(self):
        self.frameMainMenu = ctk.CTkFrame(master=self.tela, corner_radius=False, fg_color="white")
        self.frameMainMenu.pack(fill="both", side="left", expand=True)

        self.frameMainMenu.grid_columnconfigure(0, weight=1)
        self.frameMainMenu.grid_columnconfigure(1, weight=1)
        self.frameMainMenu.grid_columnconfigure(2, weight=2)
        self.frameMainMenu.grid_columnconfigure(3, weight=1)
        self.frameMainMenu.grid_columnconfigure(4, weight=1)
        rows = 8
        for i in range(rows):
            self.frameMainMenu.grid_rowconfigure(i, weight=1)

        ctk.CTkLabel(self.frameMainMenu, text="Selecione um setor", font=("calibri bold", 50),text_color="#043151").grid(row=0, column=0, columnspan=5)

        img = ctk.CTkImage(light_image=Image.open(r"Franco_Contabilidade.png"), size=(230,200))
        imglabel = ctk.CTkLabel(self.frameMainMenu, text=None, image=img).grid(row=3, column=2, padx=10)#, columnspan=3)#.place(relx=0.7, rely=0.675)


        #btn_voltar = ctk.CTkButton(self.frameMainMenu, text="Fechar", command=self.tela.destroy, width=90, font=("calibri bold", 15), border_width=4, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", corner_radius=3).place(relx=0, rely=0)

        btn_franco000= ctk.CTkButton(self.frameMainMenu, width=280, height=50, command=self.franco_000, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", text_color="white",  font=("calibri bold", 23), text="000-Franco").grid(row=1, column=1, padx=10)
        btnteste1= ctk.CTkButton(self.frameMainMenu, text="001-Administração", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=2, column=1, padx=10)
        btnteste2= ctk.CTkButton(self.frameMainMenu, text="002-Contabilidade", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=3, column=1, padx=10)
        btnteste3= ctk.CTkButton(self.frameMainMenu, text="003-Departamento Pessoal", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", font=("calibri bold", 23),).grid(row=4, column=1, padx=10)
        btnteste4= ctk.CTkButton(self.frameMainMenu, text="004-Legalização", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=5, column=1, padx=10)
        btnteste5= ctk.CTkButton(self.frameMainMenu, text="005-Fiscal", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=6, column=1, padx=10)
        btn_franco006= ctk.CTkButton(self.frameMainMenu, text="006-Comercial", width=280, height=50, command=self.comercial_006, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", text_color="white", font=("calibri bold", 23),).grid(row=1, column=2, padx=10)
        btn_franco007= ctk.CTkButton(self.frameMainMenu, text="007-TI Infra", width=280, height=50, command=self.infra_007, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", text_color="white", font=("calibri bold", 23),).grid(row=2, column=2, padx=10)
        btnteste8= ctk.CTkButton(self.frameMainMenu, text="008-Diretoria", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=4, column=2, padx=10)
        btnteste9= ctk.CTkButton(self.frameMainMenu, text="009-Tributario", state="disabled",  width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=5, column=2, padx=10)
        btnteste10= ctk.CTkButton(self.frameMainMenu, text="010-Secretaria", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=6, column=2, padx=10)
        btnteste11= ctk.CTkButton(self.frameMainMenu, text="011-Financeiro", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=1, column=3, padx=10)
        btnteste12= ctk.CTkButton(self.frameMainMenu, text="012-Qualidade", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=2, column=3, padx=10)
        btnteste13= ctk.CTkButton(self.frameMainMenu, text="013-Integração", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=3, column=3, padx=10)
        btn_franco014= ctk.CTkButton(self.frameMainMenu, text="014-Auditoria", width=280, height=50, command=self.auditoria_014, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", text_color="white", font=("calibri bold", 23),).grid(row=4, column=3, padx=10)
        btn_franco015= ctk.CTkButton(self.frameMainMenu, text="015-Recursos Humanos", width=280, height=50, command=self.recursos_humanos015, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", text_color="white", font=("calibri bold", 23),).grid(row=5, column=3, padx=10)
        btnteste17= ctk.CTkButton(self.frameMainMenu, text="017-Desenvolvimento", state="disabled", width=280, height=50, command="", border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23),).grid(row=6, column=3, padx=10)


    def franco_000(self):

        def back_button():
            self.frameFranco000.pack_forget()
            self.frameMainMenu.pack(fill="both", side="left", expand=True)

        def atualizar_relatorios():
            
            lista = []

            valorIntranetTributacao = checkvarIntranetTributacao.get()

            valorIntranetEmpresas = checkvarIntranetEmpresas.get()

            valorIntranetResponsaveis = checkvarIntranetResponsaveis.get()

            valorIntranetWorkFlow = checkvarIntranetWorkFlow.get()
            

            if valorIntranetTributacao == "on":
                nome = "Intranet Tributação"
                print(f"Relatório {nome} atualizado")
                lista.append(nome)
                #atualizaTributacao()
                checkvarIntranetTributacao.set("off")
            else:pass
            
            if valorIntranetEmpresas =="on":
                nome = "Intranet Empresas"
                print(f"Relatório {nome} atualizado")
                lista.append(nome)
                #atualizarEmpresas()
                checkvarIntranetEmpresas.set("off")

            else: pass

            if valorIntranetResponsaveis =="on":
                nome = "Intranet Responsaveis"
                print(f"Relatório {nome} atualizado")
                lista.append(nome)
                #atualizarResponsaveis()
                checkvarIntranetResponsaveis.set("off")
            else: pass

            if valorIntranetWorkFlow =="on":
                nome = "Intranet WorkFlow"
                lista.append(nome)
                print(f"Relatório {nome} atualizado")
                #atualizarWorkFlow()
                checkvarIntranetWorkFlow.set("off")
            else: pass

            m = len(lista)

            print(m)

            if m == 0:
                print("não há nada para atualizar")
            else:
                messagebox.showinfo(title="Fim do processamento", message=f"Atualização concluída")

            print(lista)
            

        def selecionar_tudo():
            
            checkvarIntranetTributacao.set("on")
            checkvarIntranetResponsaveis.set("on")
            checkvarIntranetEmpresas.set("on")
            checkvarIntranetWorkFlow.set("on")
        

        self.frameMainMenu.pack_forget()
        
        self.frameFranco000 = ctk.CTkFrame(master=self.tela, corner_radius=False, fg_color="white")
        self.frameFranco000.pack(fill="both", side="left", expand=True)
        
        self.frameFranco000.grid_columnconfigure(0, weight=1)
        self.frameFranco000.grid_columnconfigure(1, weight=1)
        self.frameFranco000.grid_columnconfigure(2, weight=1)
        self.frameFranco000.grid_columnconfigure(3, weight=1)
        self.frameFranco000.grid_columnconfigure(4, weight=1)
        rows = 8
        for i in range(rows):
            self.frameFranco000.grid_rowconfigure(i, weight=1)




        ctk.CTkLabel(self.frameFranco000, text="Atualização de relatórios Franco Contabilidade",font=("calibri bold", 35), text_color="#043151").grid(row=0, column=0, columnspan=5)

        self.btn_voltar = ctk.CTkButton(self.frameFranco000, text="Voltar", command=back_button, width=90, font=("calibri bold", 15), border_width=4, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", corner_radius=3).place(relx=0, rely=0)
        
        checkvarIntranetTributacao = ctk.StringVar(value="")
        cbFrancoIntranetConsultaTrib = ctk.CTkCheckBox(master=self.frameFranco000, text="Consulta-Tributação", variable=checkvarIntranetTributacao, onvalue="on", offvalue="off", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.1, rely=0.25) #OK

        cbTeste2 = ctk.CTkCheckBox(master= self.frameFranco000, state="disabled", text="Intranet - Mundança  de Tributação.", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.1, rely=0.40) #OK

        cbTeste3 = ctk.CTkCheckBox(master= self.frameFranco000, state="disabled", text="Intranet Franco - Usuários", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.1, rely=0.55) #OK

        cbTeste4= ctk.CTkCheckBox(master= self.frameFranco000, state="disabled", text="Intranet-Departamentos", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.1, rely=0.70) #OK

        checkvarIntranetEmpresas = ctk.StringVar(value="")
        cbFrancoIntranetEmpresas = ctk.CTkCheckBox(master= self.frameFranco000, text="Intranet-Empresas", variable=checkvarIntranetEmpresas, onvalue="on", offvalue="off",text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.4, rely=0.25) #OK

        cbTeste7 = ctk.CTkCheckBox(master= self.frameFranco000, state="disabled", text="Intranet-Obrigações", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.4, rely=0.55) #OK

        checkvarIntranetResponsaveis = ctk.StringVar(value="")
        cbFrancoIntranetResponsaveis = ctk.CTkCheckBox(master= self.frameFranco000, text="Intranet-Responsáveis", variable=checkvarIntranetResponsaveis, onvalue="on", offvalue="off", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.4, rely=0.70) #ok

        cbTeste9 = ctk.CTkCheckBox(master= self.frameFranco000, state="disabled", text="Intranet-Tributação", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.7, rely=0.25) #ok

        cbTeste10 = ctk.CTkCheckBox(master= self.frameFranco000, state="disabled", text="Intranet-UF", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.7, rely=0.40) #OK

        checkvarIntranetWorkFlow = ctk.StringVar(value="")
        cbFrancoIntranetWorkFlow = ctk.CTkCheckBox(master= self.frameFranco000, text="Intranet-Workflow Porcentagem", variable=checkvarIntranetWorkFlow, onvalue="on", offvalue="off", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.7, rely=0.55) #ok

        cbTeste12 = ctk.CTkCheckBox(master= self.frameFranco000, state="disabled", text="Prosoft-Contagem", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.7, rely=0.70)#OK

        cbTeste6 = ctk.CTkCheckBox(master= self.frameFranco000, state="disabled", text="Prosoft-Realizado-Analítico", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.4, rely=0.40)

        btnAtualizarRelatorios000 = ctk.CTkButton(self.frameFranco000, text="Atualizar Relatórios", command=atualizar_relatorios, width=250, height=40, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23)).grid(row=7, column=0)#.place(relx=0.1, rely=0.84)

        btnAtualizarSelecionarTodos000 = ctk.CTkButton(self.frameFranco000, text="Selecionar Todos", command=selecionar_tudo, width=250, height=40, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23)).grid(row=7, column=1)#.place(relx=0.4, rely=0.84)

        img = ctk.CTkImage(light_image=Image.open(r"franco_Logo.png"), size=(150,150))
        imglabel = ctk.CTkLabel(self.frameFranco000, text=None, image=img).grid(row=7, column=3)#.place(relx=0.7, rely=0.783)


    def comercial_006(self):
        def back_button():
            self.frameComercial006.pack_forget()
            self.frameMainMenu.pack(fill="both", side="left", expand=True)

        def atualizar_relatorios():
            
            lista = []

            valorIntranetDesligamentos = checkvarIntranetDesligamentos.get()
            
            if valorIntranetDesligamentos == "on":
                nome = "Intranet Desligamentos"
                lista.append(nome)
                print(f"Relatório {nome} atualizado")
                #atualizarDesligamentos()
                checkvarIntranetDesligamentos.set("off")
            else:pass

            m = len(lista)

            print(m)

            if m == 0:
                print("não há nada para atualizar")
            else:
                messagebox.showinfo(title="Fim do processamento", message=f"Atualização concluída")
                
            print(lista)


        def selecionar_tudo():
            checkvarIntranetDesligamentos.set("on")

        

        self.frameMainMenu.pack_forget()

        
        self.frameComercial006 = ctk.CTkFrame(master=self.tela, corner_radius=False, fg_color="white")
        self.frameComercial006.pack(fill="both", side="left", expand=True)

        self.frameComercial006.grid_columnconfigure(0, weight=1)
        self.frameComercial006.grid_columnconfigure(1, weight=1)
        self.frameComercial006.grid_columnconfigure(2, weight=2)
        self.frameComercial006.grid_columnconfigure(3, weight=1)
        self.frameComercial006.grid_columnconfigure(4, weight=1)
        rows = 8
        for i in range(rows):
            self.frameComercial006.grid_rowconfigure(i, weight=1)

        ctk.CTkLabel(self.frameComercial006, text="Atualização de relatórios Franco Contabilidade",font=("calibri bold", 35), text_color="#043151").grid(row=0, column=0, columnspan=5)

        self.btn_voltar = ctk.CTkButton(self.frameComercial006, text="Voltar", command=back_button, width=90, font=("calibri bold", 15), border_width=4, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", corner_radius=3).place(relx=0, rely=0)
        
        checkvarIntranetDesligamentos = ctk.StringVar(value="")
        cbFrancoIntranetDesligamentos = ctk.CTkCheckBox(master=self.frameComercial006, text="Intranet-Desligamentos", variable=checkvarIntranetDesligamentos, onvalue="on", offvalue="off", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.1, rely=0.25)#.place(relx=0.5, rely=0.5, anchor=CENTER) #OK

        btnAtualizarRelatorios006 = ctk.CTkButton(self.frameComercial006, text="Atualizar Relatórios", command=atualizar_relatorios, width=250, height=40, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23)).grid(row=7, column=0)#.place(relx=0.1, rely=0.84)

        btnAtualizarSelecionarTodos006 = ctk.CTkButton(self.frameComercial006, text="Selecionar Todos", command=selecionar_tudo, width=250, height=40, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23)).grid(row=7, column=1)#.place(relx=0.4, rely=0.84)

        img = ctk.CTkImage(light_image=Image.open(r"franco_Logo.png"), size=(150,150))
        imglabel = ctk.CTkLabel(self.frameComercial006, text=None, image=img).grid(row=7, column=3)#.place(relx=0.7, rely=0.783)


    def infra_007(self):
         
        def back_button():
            self.frameInfra007.pack_forget()
            self.frameMainMenu.pack(fill="both", side="left", expand=True)

        def atualizar_relatorios():
            
            lista = []

            valorIntranetDescarte = checkvarIntranetDescarte.get()
            valorIntranetMaquinas = checkvarIntranetMaquinas.get()
            valorIntranetServidores = checkvarIntranetServidores.get()
            valorIntranetSuporte = checkvarIntranetSuporte.get()

            if valorIntranetSuporte == "on":
                nome = "Intranet_Suporte TI"
                print(f"Relatório {nome} atualizado")
                lista.append(nome)
                #atualizarSuporteInfra()
                checkvarIntranetSuporte.set("off")
            else:pass

            if valorIntranetDescarte == "on":
                nome = "Intranet-Descarte"
                print(f"Relatório {nome} atualizado")
                lista.append(nome)
                #atualizarDescarte()
                checkvarIntranetDescarte.set("off")
            else:pass

            if valorIntranetMaquinas == "on":
                nome = "Intranet-Maquinas"
                print(f"Relatório {nome} atualizado")
                lista.append(nome)
                #atualizarMaquinas()
                checkvarIntranetMaquinas.set("off")
            else:pass

            if valorIntranetServidores == "on":
                nome = "Intranet-Servidores"
                lista.append(nome)
                print(f"Relatório {nome} atualizado")
                #atualizarServidores()
                checkvarIntranetServidores.set("off")
            else:pass

            m = len(lista)

            print(m)

            if m == 0:
                print("não há nada para atualizar")
            else:
                messagebox.showinfo(title="Fim do processamento", message=f"Atualização concluída")
                
            print(lista)


        def selecionar_tudo():
            
            checkvarIntranetDescarte.set("on")
            checkvarIntranetMaquinas.set("on")
            checkvarIntranetServidores.set("on")
            checkvarIntranetSuporte.set("on")
        


        self.frameMainMenu.pack_forget()
        
        self.frameInfra007 = ctk.CTkFrame(master=self.tela, corner_radius=False, fg_color="white")
        self.frameInfra007.pack(fill="both", side="left", expand=True)

        self.frameInfra007.grid_columnconfigure(0, weight=1)
        self.frameInfra007.grid_columnconfigure(1, weight=1)
        self.frameInfra007.grid_columnconfigure(2, weight=2)
        self.frameInfra007.grid_columnconfigure(3, weight=1)
        self.frameInfra007.grid_columnconfigure(4, weight=1)
        rows = 8
        for i in range(rows):
            self.frameInfra007.grid_rowconfigure(i, weight=1)

        ctk.CTkLabel(self.frameInfra007, text="Atualização de relatórios Franco Contabilidade",font=("calibri bold", 35), text_color="#043151").grid(row=0, column=0, columnspan=5)

        self.btn_voltar = ctk.CTkButton(self.frameInfra007, text="Voltar", command=back_button, width=90, font=("calibri bold", 15), border_width=4, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", corner_radius=3).place(relx=0, rely=0)
        

        checkvarIntranetSuporte = ctk.StringVar(value="")
        cbFrancoIntranetSuporte = ctk.CTkCheckBox(master=self.frameInfra007, text="Intranet-Suporte", variable=checkvarIntranetSuporte, onvalue="on", offvalue="off", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.1, rely=0.25)#.place(relx=0.4, rely=0.25,) #OK

        checkvarIntranetServidores = ctk.StringVar(value="")
        cbFrancoIntranetServidores = ctk.CTkCheckBox(master=self.frameInfra007, text="Intranet-Servidores", variable=checkvarIntranetServidores, onvalue="on", offvalue="off", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.1, rely=0.40)#.place(relx=0.4, rely=0.35,) #OK

        checkvarIntranetMaquinas = ctk.StringVar(value="")
        cbFrancoIntranetMaquinas = ctk.CTkCheckBox(master=self.frameInfra007, text="Intranet-Maquinas", variable=checkvarIntranetMaquinas, onvalue="on", offvalue="off", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.1, rely=0.55)#.place(relx=0.4, rely=0.45,) #OK

        checkvarIntranetDescarte = ctk.StringVar(value="")
        cbFrancoIntranetDescarte = ctk.CTkCheckBox(master=self.frameInfra007, text="Intranet-Descarte", variable=checkvarIntranetDescarte, onvalue="on", offvalue="off", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold" , 17)).place(relx=0.1, rely=0.70)#.place(relx=0.4, rely=0.55,) #OK

        #checkvarIntranetQTDE = ctk.StringVar(value="")
        cbFrancoIntranetQTDE = ctk.CTkCheckBox(master=self.frameInfra007, state="disabled", text="Impressoras-Qtde", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.4, rely=0.25,) #OK
        
        
        btnAtualizarRelatorios007 = ctk.CTkButton(self.frameInfra007, text="Atualizar Relatórios", command=atualizar_relatorios, width=250, height=40, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23)).grid(row=7, column=0)#.place(relx=0.1, rely=0.84)

        btnAtualizarSelecionarTodos007 = ctk.CTkButton(self.frameInfra007, text="Selecionar Todos", command=selecionar_tudo, width=250, height=40, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23)).grid(row=7, column=1)#.place(relx=0.4, rely=0.84)

        img = ctk.CTkImage(light_image=Image.open(r"franco_Logo.png"), size=(150,150))
        imglabel = ctk.CTkLabel(self.frameInfra007, text=None, image=img).grid(row=7, column=3)#.place(relx=0.7, rely=0.783)


    def auditoria_014(self):
        
        def back_button():
            self.frameAuditoria014.pack_forget()
            self.frameMainMenu.pack(fill="both", side="left", expand=True)

        def atualizar_relatorios():
            
            lista = []

            valorIntranetObrigacoes = checkvarIntranetObrigacoes.get()
            
            if valorIntranetObrigacoes == "on":
                nome = "Consulta Obrigações"
                lista.append(nome)
                print(f"Relatório {nome} atualizado")
                #atualizarObrigacoes()
                checkvarIntranetObrigacoes.set("off")
            else:pass

            m = len(lista)

            print(m)

            if m == 0:
                print("não há nada para atualizar")
            else:
                messagebox.showinfo(title="Fim do processamento", message=f"Atualização concluída")
                
            print(lista)


        def selecionar_tudo():
            checkvarIntranetObrigacoes.set("on")



        self.frameMainMenu.pack_forget()

        self.frameAuditoria014 = ctk.CTkFrame(master=self.tela, corner_radius=False, fg_color="white")
        self.frameAuditoria014.pack(fill="both", side="left", expand=True)

        self.frameAuditoria014.grid_columnconfigure(0, weight=1)
        self.frameAuditoria014.grid_columnconfigure(1, weight=1)
        self.frameAuditoria014.grid_columnconfigure(2, weight=2)
        self.frameAuditoria014.grid_columnconfigure(3, weight=1)
        self.frameAuditoria014.grid_columnconfigure(4, weight=1)
        rows = 8
        for i in range(rows):
            self.frameAuditoria014.grid_rowconfigure(i, weight=1)

        ctk.CTkLabel(self.frameAuditoria014, text="Atualização de relatórios Franco Contabilidade",font=("calibri bold", 35), text_color="#043151").grid(row=0, column=0, columnspan=5)

        self.btn_voltar = ctk.CTkButton(self.frameAuditoria014, text="Voltar", command=back_button, width=90, font=("calibri bold", 15), border_width=4, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", corner_radius=3).place(relx=0, rely=0)
        
        checkvarIntranetObrigacoes = ctk.StringVar(value="")
        cbFrancoIntranetObrigacoes = ctk.CTkCheckBox(master=self.frameAuditoria014, text="Consulta-Obrigações", variable=checkvarIntranetObrigacoes, onvalue="on", offvalue="off", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.1, rely=0.25)#.place(relx=0.5, rely=0.5, anchor=CENTER) #OK

        btnAtualizarRelatorios014 = ctk.CTkButton(self.frameAuditoria014, text="Atualizar Relatórios", command=atualizar_relatorios, width=250, height=40, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23)).grid(row=7, column=0)#.place(relx=0.1, rely=0.84)

        btnAtualizarSelecionarTodos014 = ctk.CTkButton(self.frameAuditoria014, text="Selecionar Todos", command=selecionar_tudo, width=250, height=40, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23)).grid(row=7, column=1)#.place(relx=0.4, rely=0.84)

        img = ctk.CTkImage(light_image=Image.open(r"franco_Logo.png"), size=(150,150))
        imglabel = ctk.CTkLabel(self.frameAuditoria014, text=None, image=img).grid(row=7, column=3)#.place(relx=0.7, rely=0.783)


    def recursos_humanos015(self):
        
        def back_button():
            self.frameRecursosHumanos015.pack_forget()
            self.frameMainMenu.pack(fill="both", side="left", expand=True)
        
        def atualizar_relatorios():
            
            lista = []

            valorIntranetTimeSheet = checkvarIntranetTimeSheet.get()
            
            if valorIntranetTimeSheet == "on":
                nome = "Intranet TimeSheet"
                lista.append(nome)
                print(f"Relatório {nome} atualizado")
                #atualizarTimeSheet()
                checkvarIntranetTimeSheet.set("off")
            else:pass

            m = len(lista)

            print(m)

            if m == 0:
                print("não há nada para atualizar")
            else:
                messagebox.showinfo(title="Fim do processamento", message=f"Atualização concluída")
                
            print(lista)


        def selecionar_tudo():
            checkvarIntranetTimeSheet.set("on")


        self.frameMainMenu.pack_forget()
        self.frameRecursosHumanos015 = ctk.CTkFrame(master=self.tela, corner_radius=False, fg_color="white")
        self.frameRecursosHumanos015.pack(fill="both", side="left", expand=True)

        self.frameRecursosHumanos015.grid_columnconfigure(0, weight=1)
        self.frameRecursosHumanos015.grid_columnconfigure(1, weight=1)
        self.frameRecursosHumanos015.grid_columnconfigure(2, weight=2)
        self.frameRecursosHumanos015.grid_columnconfigure(3, weight=1)
        self.frameRecursosHumanos015.grid_columnconfigure(4, weight=1)
        rows = 8
        for i in range(rows):
            self.frameRecursosHumanos015.grid_rowconfigure(i, weight=1)

        ctk.CTkLabel(self.frameRecursosHumanos015, text="Atualização de relatórios Franco Contabilidade",font=("calibri bold", 35), text_color="#043151").grid(row=0, column=0, columnspan=5)

        self.btn_voltar = ctk.CTkButton(self.frameRecursosHumanos015, text="Voltar", command=back_button, width=90, font=("calibri bold", 15), border_width=4, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc", corner_radius=3).place(relx=0, rely=0)

        checkvarIntranetTimeSheet = ctk.StringVar(value="")
        cbFrancoIntranetTimeSheet = ctk.CTkCheckBox(master=self.frameRecursosHumanos015, text="Intranet-TimeSheet", variable=checkvarIntranetTimeSheet, onvalue="on", offvalue="off", text_color="#043151", border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 17)).place(relx=0.1, rely=0.25)#.place(relx=0.5, rely=0.5, anchor=CENTER) #OK

        btnAtualizarRelatorios015 = ctk.CTkButton(self.frameRecursosHumanos015, text="Atualizar Relatórios", command=atualizar_relatorios, width=250, height=40, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23)).grid(row=7, column=0)#.place(relx=0.1, rely=0.84)

        btnAtualizarSelecionarTodos015 = ctk.CTkButton(self.frameRecursosHumanos015, text="Selecionar Todos", command=selecionar_tudo, width=250, height=40, border_width=7, border_color="#0494dc", fg_color="#14a6e1", hover_color="#0494dc",  font=("calibri bold", 23)).grid(row=7, column=1)#.place(relx=0.4, rely=0.84)

        img = ctk.CTkImage(light_image=Image.open(r"franco_Logo.png"), size=(150,150))
        imglabel = ctk.CTkLabel(self.frameRecursosHumanos015, text=None, image=img).grid(row=7, column=3)#.place(relx=0.7, rely=0.783)


Aplication()