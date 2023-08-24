import customtkinter as ctk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
import mysql.connector
from mysql.connector import Error
import time


app = ctk.CTk()
session = False

class Aplication():

    def __init__(self) -> None:
        self.app=app
        self.main_window()
        self.geral_frame()
        self.login_frame()
        self.font = "Arial Bold"
        #self.db_connect()
        self.app.mainloop()

  
    def db_connect(self):
        
        self.con = mysql.connector.connect(
        user= 'root',
        password= '@RhyanLucca1000',
        host= 'localhost',
        database= 'RTSystems'
        )

        self.cursor = self.con.cursor()
 

    def main_window(self):

        self.app.attributes("-fullscreen", True)

        #self.app.geometry("700x700")
       # ctk.set_appearance_mode("light")
        self.app.title("RTS Systems")
        #print(self.current_frame)


    def geral_frame(self):
        self.geralFrame = ctk.CTkFrame(master=self.app, corner_radius=False) #, fg_color="red")
        self.geralFrame.pack(fill="both", side="left", expand=True)
        columns = 3

        self.geralFrame.grid_columnconfigure(0, weight=1)
        self.geralFrame.grid_columnconfigure(1, weight=2)
        self.geralFrame.grid_columnconfigure(2, weight=1)
      

    def login_frame(self):
        self.scrWidth= self.app.winfo_screenwidth()
        self.scrHeight = self.app.winfo_screenheight()
        scrWidth = self.scrWidth /2
        scrHeight=self.scrHeight / 2
        self.font = "Arial Bold"
        #print(scrWidth)
        #print(scrHeight)
        loginFrame= ctk.CTkFrame(master=self.geralFrame, width=scrWidth, height=scrHeight)# fg_color="black",
        loginFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        self.userPermissao = []

        def exit_screen():

            #query = "SELECT usersNome, usersPswd, usersPermissao FROM users;"

            cursor = Aplication.db_connect(self)

            entryUser = userEntry.get()
            entryPswd = senhaEntry.get()

            query = f"SELECT usersNome, usersPswd, usersPermissao FROM users WHERE usersNome = '{entryUser}' AND usersPswd = '{entryPswd}';"

            self.cursor.execute(query)

            resultado= self.cursor.fetchone()
            
            if resultado:
                print(resultado)
                print("Login")
                
                global user, senha, permissao, tipoUser
                user = resultado[0]
                senha = resultado[1]
                permissao = resultado[2]

                if permissao == '1':
                    tipoUser = 1
                elif permissao == '0':
                    tipoUser = 0

                self.initial_frame()
                self.side_menu_frame()

            #         print(user)

            else:
                ctk.CTkLabel(master=loginFrame, text="Usuário ou senha incorretos.", font=(f"{self.font}", self.scrWidth/70)).place(relx=0.1, rely=0.65,)

        ctk.CTkLabel(master=loginFrame, text="Usuário", font=(f"{self.font}", self.scrWidth/40)).place(relx=0.1, rely=0.1)


        userEntry= ctk.CTkEntry(master=loginFrame, placeholder_text="Insira o usuário", width=scrWidth/1.2 ,font=(f"{self.font}", self.scrWidth/40))
        userEntry.place(relx=0.1, rely=0.25)

        ctk.CTkLabel(master=loginFrame, text="Senha", font=(f"{self.font}", self.scrWidth/40)).place(relx=0.1, rely=0.4)

        senhaEntry= ctk.CTkEntry(master=loginFrame, show="*", placeholder_text="Insira a senha", width=scrWidth/1.2 ,font=(f"{self.font}", self.scrWidth/40))
        senhaEntry.place(relx=0.1, rely=0.55)

        btnLogin = ctk.CTkButton(master=loginFrame, text="Entrar", command=exit_screen, width=scrWidth/2, font=(f"{self.font}", self.scrWidth/40)).place(relx=0.1, rely=0.8)


    def side_menu_frame(self):

        imageHeight= round((self.scrHeight/100)*4)
        imageWidth=round((self.scrWidth/100)*4)

        
        shoppingImage = ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\cart_light.png"), dark_image=Image.open(r"Python\rtsApp\cart_dark.png"), size=(imageHeight, imageWidth))
        stockImage = ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\box_log_light.png"), dark_image=Image.open(r"Python\rtsApp\box_log_dark.png"), size=(imageHeight, imageWidth))
        cashImage = ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\cash_cash_light.png"), dark_image=Image.open(r"Python\rtsApp\cash_cash_dark.png"), size=(imageHeight, imageWidth))
        analysisImage = ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\anal_light.png"), dark_image=Image.open(r"Python\rtsApp\anal_dark.png"), size=(imageHeight, imageWidth))
        usersImage =ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\users_light.png"), dark_image=Image.open(r"Python\rtsApp\users_dark.png"), size=(imageHeight, imageWidth))
        configImage = ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\config_light.png"), dark_image=Image.open(r"Python\rtsApp\config_dark.png"), size=(imageHeight, imageWidth))

        frame_widget_max= self.scrWidth/ 4
        frame_wdiget_min= self.scrWidth/ 18


        frame_widget = frame_wdiget_min
        self.sideMenuFrame = ctk.CTkFrame(master=self.currentFrame, width=frame_widget, height=self.scrHeight, corner_radius=False)
        self.sideMenuFrame.place(relx=0, rely=0,relheight=1)

        rows = 25
        self.sideMenuFrame.grid_columnconfigure(0, weight=1)
        for row in range(rows):
            self.sideMenuFrame.grid_rowconfigure(row, weight=1)

        if tipoUser == 1:
            statusPermissao = "normal"
        else:
            statusPermissao = "disabled"
        

        ctk.CTkLabel(master=self.sideMenuFrame, text="RTS", font=(f"{self.font}", self.scrWidth/30)).grid(column=0, row=1) 

        self.stockFrameButton = ctk.CTkButton(master=self.sideMenuFrame, text='', command=self.stock_frame, image=shoppingImage, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scrWidth/40)).grid(column=0, row=5, padx=self.scrWidth/99)
        ctk.CTkLabel(master=self.sideMenuFrame, text="Compras", font=(f"{self.font}", self.scrWidth/70)).grid(column=0, row=6)  

        self.stockFrameButton = ctk.CTkButton(master=self.sideMenuFrame, text='', command=self.stock_frame, image=stockImage, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scrWidth/40)).grid(column=0, row=8, padx=self.scrWidth/99)#.place(relx=0, rely=0.25)
        ctk.CTkLabel(master=self.sideMenuFrame, text="Estoque", font=(f"{self.font}", self.scrWidth/70)).grid(column=0, row=9)  
        
        self.salesFrameButton = ctk.CTkButton(master=self.sideMenuFrame, text="", command=self.sales_frame, image=cashImage, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scrWidth/40)).grid(column=0, row=12, padx=self.scrWidth/99)#.place(relx=0, rely=0.45)
        ctk.CTkLabel(master=self.sideMenuFrame, text="Vendas", font=(f"{self.font}", self.scrWidth/70)).grid(column=0, row=13)  
        
        self.analysisFrameButton = ctk.CTkButton(master=self.sideMenuFrame, text="", command=self.analysis_frame, image=analysisImage, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scrWidth/40)).grid(column=0, row=16, padx=self.scrWidth/99)#.place(relx=0, rely=0.70)
        ctk.CTkLabel(master=self.sideMenuFrame, text="Analises", font=(f"{self.font}", self.scrWidth/70)).grid(column=0, row=17)  
        
        self.usersFrameButton = ctk.CTkButton(master=self.sideMenuFrame, text="", command=self.users_frame, image=usersImage, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scrWidth/40), state=f"{statusPermissao}").grid(column=0, row=20, padx=self.scrWidth/99)
        ctk.CTkLabel(master=self.sideMenuFrame, text="Usuários", font=(f"{self.font}", self.scrWidth/70)).grid(column=0, row=21)
        
        self.configFrameButton = ctk.CTkButton(master=self.sideMenuFrame, text="", command='increase_men', image=configImage, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scrWidth/40)).grid(column=0, row=24, padx=self.scrWidth/99)
        ctk.CTkLabel(master=self.sideMenuFrame, text="Config.", font=(f"{self.font}", self.scrWidth/70)).grid(column=0, row=25)
    
    
    def initial_frame(self):

        if tipoUser == 1:
            print("Usario adm")
        elif tipoUser == 0:
            print("Usuario padão")

        self.initialFrame = ctk.CTkFrame(master=self.geralFrame, width=self.scrWidth, corner_radius=False, border_color="black", border_width=1)
        self.initialFrame.pack(fill='both', side="right", expand=True)
        self.currentFrame = self.initialFrame
        self.side_menu_frame()
        
        ctk.CTkLabel(master=self.initialFrame, text="Bem vindo", font=(f"{self.font}", self.scrWidth/30)).place(relx=0.1, rely=0.05)

        self.currentFrame = self.initialFrame


    def stock_frame(self):

        self.currentFrame.pack_forget()
        self.stockFrame = ctk.CTkFrame(master=self.geralFrame, width=self.scrWidth, corner_radius=False, border_color="black", border_width=1)#fg_color="pink",
        self.stockFrame.pack(fill='both', side="right", expand=True)

        self.currentFrame = self.stockFrame
        self.side_menu_frame()

        ctk.CTkLabel(master=self.stockFrame, text="Estoque", font=(f"{self.font}", self.scrWidth/30)).place(relx=0.1, rely=0.05)

        self.valor= ''

        def supplier_crud():

            self.db_connect()

            def popular():
                supplierTreeView.delete(*supplierTreeView.get_children())
                query = "SELECT * FROM "

            def gravar():
                if CodigoEntry.get() == "": #or  nameEntry.get=="" or ContatoEntry.get() == "" or enderecoEntry.get() == "":
                    print("erro")
                else:
                    supplierTreeView.insert("", "end", values=(CodigoEntry.get(), nameEntry.get(), ContatoEntry.get(), enderecoEntry.get() ))
                    CodigoEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    ContatoEntry.delete(0, END) 
                    enderecoEntry.delete(0, END)

            def deletar():
                try:
                    selectedItem = supplierTreeView.selection()[0]
                    fornecedoresQueryDEL = f"DELETE FROM fornecedores WHERE idFornecedores = {selectedItem}"
                    print(fornecedoresQueryDEL)
                    selectedItem2 = supplierTreeView.selection()
                    print(selectedItem2)
                except:
                    print("Selecione um item válido")
         
            def obter():
                selectedItem = supplierTreeView.focus() #Retorna apenas um valor
                details = supplierTreeView.item(selectedItem)
                supplierGet = details.get("values")[2]
                print(selectedItem)
                # try:
                #     selectedItem = supplierTreeView.selection()[0]
                #     supplierTreeView.get_children()
                #     for value in supplierTreeView.item['values']:
                #         print(value)
                #     #valores = supplierTreeView.item(selectedItem, "values")
                #     #print(valores)
                # except:
                #     print("Selecione um item válido")


            self.currentFrame.pack_forget()
            frameCrud = ctk.CTkFrame(master=self.geralFrame, width=(self.scrWidth)-(self.scrWidth/100)*500, corner_radius=False, border_color="black", border_width=1)
            frameCrud.pack(fill='both', side="right", expand=True)

            self.currentFrame = frameCrud

            frameCrud.grid_columnconfigure(0, weight=1)
            frameCrud.grid_columnconfigure(1, weight=1)

            rows = 20

            for row in range(rows):
                frameCrud.grid_rowconfigure(row, weight=1)

        #INICIO DO FORMULARIO
            self.side_menu_frame()
            ctk.CTkLabel(master=self.currentFrame, text="Fornecedores", font=(f"{self.font}", self.scrWidth/30)).grid(row=0, column=0)
            
            #ctk.CTkLabel(master=self.currentFrame, text="Código do Fornecedor *", font=(f"{self.font}", self.scrWidth/50)).grid(row=2, column=0)
            CodigoEntry = ctk.CTkEntry(master=self.currentFrame, placeholder_text="Código do Fornecedor *", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/50))
            CodigoEntry.grid(row=2, column=0)

            #ctk.CTkLabel(master=self.currentFrame, text="Nome do Fornecedor *", font=(f"{self.font}", self.scrWidth/50)).grid(row=4, column=0)#.place(relx=0.1, rely=0.27)
            nameEntry = ctk.CTkEntry(master=self.currentFrame, placeholder_text="Nome do Fornecedor", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/50))
            nameEntry.grid(row=4, column=0)#.place(relx=0.1, rely=0.30)

            #ctk.CTkLabel(master=self.currentFrame, text="Contato do Fornecedor", font=(f"{self.font}", self.scrWidth/50)).grid(row=6, column=0)#.place(relx=0.1, rely=0.37)
            ContatoEntry = ctk.CTkEntry(master=self.currentFrame, placeholder_text="Contato do Fornecedor", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/50))
            ContatoEntry.grid(row=6, column=0)#.place(relx=0.1, rely=0.4)

            #ctk.CTkLabel(master=self.currentFrame, text="E-mail do Fornecedor", font=(f"{self.font}", self.scrWidth/50)).grid(row=8, column=0)#.place(relx=0.1, rely=0.47)
            emailEntry = ctk.CTkEntry(master=self.currentFrame, placeholder_text="E-mail do Fornecedor", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/50))
            emailEntry.grid(row=8, column=0)#.place(relx=0.1, rely=0.5)

            #ctk.CTkLabel(master=self.currentFrame, text="Contato do Fornecedor", font=(f"{self.font}", self.scrWidth/50)).grid(row=10, column=0)#.place(relx=0.1, rely=0.57)
            enderecoEntry = ctk.CTkEntry(master=self.currentFrame, placeholder_text="Contato do Fornecedor", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/50))
            enderecoEntry.grid(row=10, column=0)#.place(relx=0.1, rely=0.6)


        #FIM DO FORMULARIO

            #ctk.CTkLabel(master=self.currentFrame, text="Os campos com * são obrigatórios", font=(f"{self.font}", self.scrWidth/60)).place(relx=0.1, rely=0.65)

            #framesupplierTreeView = ctk.CTkFrame(master=frameCrud, fg_color="red")
            #framesupplierTreeView.grid(row=0, column=1, rowspan=3)

        #INICIO DA TREEVIEW
            if self.userPermissao == '1':
                supplierTreeView = ttk.Treeview(master=frameCrud, columns=("id", "codigo", "nome", "contato", "endereco", "email", "documento", "custos"), selectmode="browse", show="headings")
                #supplierTreeView['columns']=('Rank', 'Name', 'Badge')
                supplierTreeView.column('id',  width=round((self.scrWidth/100)*3, ), stretch=NO)
                supplierTreeView.column('codigo', width=round((self.scrWidth/100)*5), anchor=CENTER)
                supplierTreeView.column('nome', width=round((self.scrWidth/100)*15), anchor=CENTER)
                supplierTreeView.column('contato', width=round((self.scrWidth/100)*7), anchor=CENTER)
                supplierTreeView.column('email', width=round((self.scrWidth/100)*7), anchor=CENTER)
                supplierTreeView.column('endereco', width=round((self.scrWidth/100)*10), anchor=CENTER)
                supplierTreeView.column('documento', width=round((self.scrWidth/100)*10), anchor=CENTER)
                supplierTreeView.column('custos', width=round((self.scrWidth/100)*10), anchor=CENTER)


                supplierTreeView.heading('id', text='ID', anchor=CENTER)
                supplierTreeView.heading('codigo', text='Codigo', anchor=CENTER)
                supplierTreeView.heading('nome', text='Nome', anchor=CENTER)
                supplierTreeView.heading('contato', text='Contato', anchor=CENTER)
                supplierTreeView.heading('email', text='E-mail', anchor=CENTER)
                supplierTreeView.heading('endereco', text='Endereço', anchor=CENTER)
                supplierTreeView.heading('documento', text='Documento', anchor=CENTER)
                supplierTreeView.heading('custos', text='Custos', anchor=CENTER)

                fornecedoresQueryREAD = "SELECT * FROM supplier"

                self.cursor.execute(fornecedoresQueryREAD)

                #lista = [["1", "Rhyan", "11985987199", "Rua belem 68 ap 13"],["2", "Rhyan", "11985987199", "Rua belem 68 ap 13"],["3", "Rhyan", "11985987199", "Rua belem 68 ap 13"]]
                lista = self.cursor.fetchall()

                for r in lista:
                    
                    idSupplier = r[0]
                    codSupplier = r[1]
                    nomeSupplier = r[2]
                    contSupplier = r[3]
                    emailSupplier = r[4]
                    endSupplier= r[5]
                    docSupplier = r[6]
                    custosSupplier= r[7]
                    supplierTreeView.insert(parent='', index="end", text='', values=(idSupplier, codSupplier, nomeSupplier, contSupplier, emailSupplier, endSupplier, docSupplier, custosSupplier))
                    
                    #print(lista[4])

                #for (id, nome, fone, end) in lista:
                #    supplierTreeView.insert(parent='', index="end", text='', values=(id, nome,fone, end))

                # supplierTreeView.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
                # supplierTreeView.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
                # supplierTreeView.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
                # supplierTreeView.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))

                #supplierTreeView.place(relx=0.6, rely=0.15, height=(self.scrHeight/100) * 49)
                supplierTreeView.place(relx=0.57, rely=0.1, height=(self.scrHeight/100) * 70)
                #supplierTreeView.place(relx=0, rely=0)#height=(self.scrHeight/100) * 49)
                #supplierTreeView.grid(row=1, column=1)
            
            else:

                supplierTreeView = ttk.Treeview(master=frameCrud, columns=("id", "codigo", "nome", "contato", "endereco"), selectmode="browse", show="headings")
                #supplierTreeView['columns']=('Rank', 'Name', 'Badge')
                supplierTreeView.column('id',  width=round((self.scrWidth/100)*3), stretch=NO)
                supplierTreeView.column('codigo', width=round((self.scrWidth/100)*5), anchor=CENTER)
                supplierTreeView.column('nome', width=round((self.scrWidth/100)*15), anchor=CENTER)
                supplierTreeView.column('contato', width=round((self.scrWidth/100)*7), anchor=CENTER)
                supplierTreeView.column('endereco', width=round((self.scrWidth/100)*10), anchor=CENTER)

                supplierTreeView.heading('id', text='ID', anchor=CENTER)
                supplierTreeView.heading('codigo', text='Codigo', anchor=CENTER)
                supplierTreeView.heading('nome', text='Nome', anchor=CENTER)
                supplierTreeView.heading('contato', text='Contato', anchor=CENTER)
                supplierTreeView.heading('endereco', text='Endereço', anchor=CENTER)

                fornecedoresQueryREAD = "SELECT * FROM supplier"

                self.cursor.execute(fornecedoresQueryREAD)

                #lista = [["1", "Rhyan", "11985987199", "Rua belem 68 ap 13"],["2", "Rhyan", "11985987199", "Rua belem 68 ap 13"],["3", "Rhyan", "11985987199", "Rua belem 68 ap 13"]]
                lista = self.cursor.fetchall()

                for r in lista:
                    
                    idFornec = r[0]
                    codFornec = r[1]
                    nomeFornec = r[2]
                    contFornec = r[3]
                    emailFornec = r[4]
                    endFornec= r[5]
                    supplierTreeView.insert(parent='', index="end", text='', values=(idFornec, codFornec, nomeFornec, contFornec, emailFornec, endFornec))
                    
                    #print(lista[4])

                #for (id, nome, fone, end) in lista:
                #    supplierTreeView.insert(parent='', index="end", text='', values=(id, nome,fone, end))

                # supplierTreeView.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
                # supplierTreeView.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
                # supplierTreeView.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
                # supplierTreeView.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))

                #supplierTreeView.place(relx=0.6, rely=0.15, height=(self.scrHeight/100) * 49)
                supplierTreeView.place(relx=0.57, rely=0.1, height=(self.scrHeight/100) * 70)
                #supplierTreeView.place(relx=0, rely=0)#height=(self.scrHeight/100) * 49)
                #supplierTreeView.grid(row=1, column=1)

        #FIM DA TREEVIEW

            btnSalvar = ctk.CTkButton(master=self.currentFrame, text="Gravar", command=gravar, width=(self.scrWidth/100)*17, font=(f"{self.font}", self.scrWidth/40))
            btnSalvar.place(relx=0.1, rely=0.9)
            btnVisualizar = ctk.CTkButton(master=self.currentFrame, text="Obter", command=obter, width=(self.scrWidth/100)*17, font=(f"{self.font}", self.scrWidth/40))
            btnVisualizar.place(relx=0.329, rely=0.9)
            #btnAtualizar = ctk.CTkButton(master=self.currentFrame, text="Editar", width=(self.scrWidth/100)*17, font=(f"{self.font}", self.scrWidth/40)).place(relx=0.55, rely=0.9)
            btnDeletar = ctk.CTkButton(master=self.currentFrame, text="Excluir", command=deletar, width=(self.scrWidth/100)*17, font=(f"{self.font}", self.scrWidth/40))
            btnDeletar.place(relx=0.75, rely=0.9)


        def produtos_crud():

            frameCrud = ctk.CTkFrame(master=self.stockFrame, width=(self.scrWidth)-(self.scrWidth/100)*500, corner_radius=False, border_color="black", border_width=1)
            frameCrud.pack(fill='both', side="right", expand=True)
            self.side_menu_frame()
            ctk.CTkLabel(master=frameCrud, text="Produtos", font=(f"{self.font}", self.scrWidth/30)).place(relx=0.1, rely=0.05)

            CodigoEntry = ctk.CTkEntry(master=frameCrud, placeholder_text="Código do fornecedor", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/40))
            CodigoEntry.place(relx=0.1, rely=0.2)

            nameEntry = ctk.CTkEntry(master=frameCrud, placeholder_text="Nome do fornecedor", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/40))
            nameEntry.place(relx=0.1, rely=0.35)

            ContatoEntry = ctk.CTkEntry(master=frameCrud, placeholder_text="Contato do fornecedor", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/40))
            ContatoEntry.place(relx=0.1, rely=0.50)

            enderecoEntry = ctk.CTkEntry(master=frameCrud, placeholder_text="Endereço do fornecedor", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/40))
            enderecoEntry.place(relx=0.1, rely=0.65)


        def analEstoque_crud():

            frameCrud = ctk.CTkFrame(master=self.stockFrame, width=(self.scrWidth)-(self.scrWidth/100)*500, corner_radius=False, border_color="black", border_width=1)
            frameCrud.pack(fill='both', side="right", expand=True)
            self.side_menu_frame()           
            ctk.CTkLabel(master=frameCrud, text="Analisar Estoque", font=(f"{self.font}", self.scrWidth/30)).place(relx=0.1, rely=0.05)


        btnFornecedor = ctk.CTkButton(master=self.stockFrame, text="Fornecedores", command=supplier_crud, width=(self.scrWidth/100)*35, font=(f"{self.font}", self.scrWidth/30)).place(relx=0.5, rely=0.25, anchor=CENTER)
        btnProduto = ctk.CTkButton(master=self.stockFrame, text="Produtos", command=produtos_crud, width=(self.scrWidth/100)*35, font=(f"{self.font}", self.scrWidth/30)).place(relx=0.5, rely=0.45,anchor=CENTER)
        btnAnaliseEstoque = ctk.CTkButton(master=self.stockFrame, text="Analisar Estoque", command=analEstoque_crud, width=(self.scrWidth/100)*35, font=(f"{self.font}", self.scrWidth/30)).place(relx=0.5, rely=0.65,anchor=CENTER)


    def sales_frame(self):
        
        self.currentFrame.pack_forget()
        self.salesFrame = ctk.CTkFrame(master=self.geralFrame, width=self.scrWidth, corner_radius=False, border_color="black", border_width=1)#fg_color="pink",
        self.salesFrame.pack(fill='both', side="right", expand=True)
        self.currentFrame = self.salesFrame
        self.side_menu_frame()

        ctk.CTkLabel(master=self.salesFrame, text="Vendas", font=(f"{self.font}", self.scrWidth/30)).place(relx=0.1, rely=0.05)


    def analysis_frame(self):
        
        self.currentFrame.pack_forget()
        self.analysisFrame = ctk.CTkFrame(master=self.geralFrame, width=self.scrWidth, corner_radius=False, border_color="black", border_width=1)
        self.analysisFrame.pack(fill="both", side="right", expand=True)
        self.currentFrame = self.analysisFrame
        self.side_menu_frame()

        ctk.CTkLabel(master=self.analysisFrame, text="Analise", font=(f"{self.font}", self.scrWidth/30)).place(relx=0.1, rely=0.05)


    def users_frame(self):
        
        def new_user():

            self.currentFrame.pack_forget()
            frameCrud = ctk.CTkFrame(master=self.geralFrame, width=(self.scrWidth)-(self.scrWidth/100)*500, corner_radius=False, border_color="black", border_width=1)
            frameCrud.pack(fill='both', side="right", expand=True)

            self.currentFrame = frameCrud
            self.side_menu_frame()
            frameCrud.grid_columnconfigure(0, weight=1)


            rows = 20

            for row in range(rows):
                frameCrud.grid_rowconfigure(row, weight=1)
    
            #Inicio do formulário 

            ctk.CTkLabel(master=self.currentFrame, text="Novo Usuário", font=(f"{self.font}", self.scrWidth/30)).grid(row=0, column=0)

            nameEntry = ctk.CTkEntry(master=self.currentFrame, placeholder_text="Nome do Usuário", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/50))
            nameEntry.grid(row=3, column=0)#.place(relx=0.1, rely=0.30)

            senhaEntry = ctk.CTkEntry(master=self.currentFrame, placeholder_text="Senha do Usuário", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/50))
            senhaEntry.grid(row=5, column=0)#.place(relx=0.1, rely=0.4)

            confSenhaEntry = ctk.CTkEntry(master=self.currentFrame, placeholder_text="Confirme a Senha", width=(self.scrWidth/100)*40, font=(f"{self.font}", self.scrWidth/50))
            confSenhaEntry.grid(row=7, column=0)#.place(relx=0.1, rely=0.4)

            def mensagem(valor):

                if valor ==0:
                    frameMsg = ctk.CTkFrame(master=self.currentFrame, width=(self.scrWidth/100)*40, height=(self.scrWidth/100)*3)
                    frameMsg.grid(row=8, column=0)
                    msg = ctk.CTkLabel(master=frameMsg, text="Usuário adicionado com sucesso", width=self.scrWidth/10, bg_color="#00AC00", font=(f"{self.font}", self.scrWidth/70), corner_radius=50)
                    msg.pack()

                elif valor == 1:
                    frameMsg = ctk.CTkFrame(master=self.currentFrame, width=(self.scrWidth/100)*40, height=(self.scrWidth/100)*3)
                    frameMsg.grid(row=8, column=0)
                    msg = ctk.CTkLabel(master=frameMsg, text="Usuário já existe", width=self.scrWidth/10, font=(f"{self.font}", self.scrWidth/70), bg_color="#DA0000", corner_radius=50)
                    msg.pack()

                else:
                    frameMsg = ctk.CTkFrame(master=self.currentFrame, width=(self.scrWidth/100)*40, height=(self.scrWidth/100)*3)
                    frameMsg.grid(row=8, column=0)
                    msg = ctk.CTkLabel(master=frameMsg, text="As senhas não coincidem", width=self.scrWidth/10, font=(f"{self.font}", self.scrWidth/70), bg_color="#DA0000", corner_radius=50)
                    msg.pack()
                


            checkVar = ctk.StringVar(value="off")


            def check_valueAdm():

                global valorCheckPermissao 

                valor = checkVar.get()

                print("Valor", valor)

                if valor == "on":
                    valorCheckPermissao=1
                elif valor == "off":
                    valorCheckPermissao= 0
                else:
                    valorCheckPermissao= 0


            def gravar_registro(): 
                check_valueAdm()
                nome= nameEntry.get()
                senha= senhaEntry.get()
                confSenha= confSenhaEntry.get()

                permissao= valorCheckPermissao

                commandVerificaSQL = f"SELECT usersNome FROM users WHERE usersNome = '{nome}';"
                self.cursor.execute(commandVerificaSQL)

                resultado = self.cursor.fetchone()

                if resultado:
                    mensagem(1)
                else:
                    if confSenha == senha:
                        
                        print(nome, senha, permissao)
                        
                        self.db_connect()
                        #commandSQL = f"INSERT INTO RTSystems.users VALUES(NULL, '{nome}', '{senha}', {permissao});"
                    
                        #self.cursor.execute(commandSQL)
                        #self.con.commit()

                        nameEntry.delete(0, END)
                        senhaEntry.delete(0, END)
                        confSenhaEntry.delete(0, END)
                        checkVar.set("off")

                        mensagem(0)
                        # msg = ctk.CTkLabel(master=frameMsg, text="Usuário adicionado com sucesso", width=self.scrWidth/10, bg_color="#00AC00", font=(f"{self.font}", self.scrWidth/70), corner_radius=50)
                        # msg.grid(row=8, column=0)
                        
                        # msg.configure(Text="")

                    else:
                        mensagem(2)
                        # msg = ctk.CTkLabel(master=frameMsg, text="As senhas não coincidem", width=self.scrWidth/10, font=(f"{self.font}", self.scrWidth/70), bg_color="#DA0000", corner_radius=50).grid(row=8, column=0, ipady= (self.scrWidth/100), ipadx= (self.scrWidth/100))
                    

            checkboxPermissaoAdm = ctk.CTkCheckBox(master=frameCrud, text="Perfil Supervisor", variable=checkVar, onvalue="on", offvalue="off", command=check_valueAdm)
            # checkboxPermissaoSupervisor = ctk.CTkCheckBox(master=frameCrud, text="Perfil supervisor", variable=checkVar, onvalue="on", offvalue="off", command=check_valueAdm)
            checkboxPermissaoAdm.grid(row=9, column=0)
            # checkboxPermissaoSupervisor.grid(row=16, column=0)

            btnSalvar = ctk.CTkButton(master=self.currentFrame, text="Gravar", command=gravar_registro, width=(self.scrWidth/100)*17, font=(f"{self.font}", self.scrWidth/40))
            btnSalvar.place(relx=0.1, rely=0.9)

            #Fim do formulário

            # frame1 = ctk.CTkFrame(master=frameCrud, fg_color="red").grid(row=0, column=0)
            # frame2 = ctk.CTkFrame(master=frameCrud, fg_color="yellow").grid(row=0, column=1)
            # frame3 = ctk.CTkFrame(master=frameCrud, fg_color="green").grid(row=0, column=2)
            # frame4 = ctk.CTkFrame(master=frameCrud, fg_color="blue").grid(row=0, column=3)

        self.currentFrame.pack_forget()
        self.usersFrame= ctk.CTkFrame(master=self.geralFrame, width=self.scrWidth, corner_radius=False, border_color="black", border_width=1)
        self.usersFrame.pack(fill="both", side="right", expand=True)
        self.currentFrame = self.usersFrame
        self.side_menu_frame()
        ctk.CTkLabel(master=self.usersFrame, text="Usuários", font=(f"{self.font}", self.scrWidth/30)).place(relx=0.1, rely=0.05)
        

        btnNewUser = ctk.CTkButton(master=self.usersFrame, text="Novo Usuário", command=new_user, width=(self.scrWidth/100)*35, font=(f"{self.font}", self.scrWidth/30)).place(relx=0.5, rely=0.25, anchor=CENTER)
        

        btnPemissoesUser = ctk.CTkButton(master=self.usersFrame, text="Permissões", width=(self.scrWidth/100)*35, font=(f"{self.font}", self.scrWidth/30)).place(relx=0.5, rely=0.65,anchor=CENTER)


        btnGerenciamentoUser = ctk.CTkButton(master=self.usersFrame, text="Gerenciamento", width=(self.scrWidth/100)*35, font=(f"{self.font}", self.scrWidth/30)).place(relx=0.5, rely=0.45,anchor=CENTER)
        
        # btnPemissoesUser = ctk.CTkButton(master=self.usersFrame, text="Permissões", width=(self.scrWidth/100)*35, font=(f"{self.font}", self.scrWidth/30)).place(relx=0.5, rely=0.65,anchor=CENTER)


Aplication()