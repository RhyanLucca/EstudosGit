import customtkinter as ctk
from tkinter import *
from PIL import Image

app = ctk.CTk()

class Aplication():

    def __init__(self) -> None:
        self.app=app
        self.tela_inicial()
        self.frame_geral()
        self.frame_login()
        self.font = "Arial Bold"
        self.currentFrame = ""
        self.app.mainloop()


    def tela_inicial(self):
        self.currentFrame = "FrameInicial"
        print(self.currentFrame)

        self.app.attributes("-fullscreen", True)

        # self.app.geometry("700x700")
       # ctk.set_appearance_mode("light")
        self.app.title("RTS Systems")
        #print(self.current_frame)


    def frame_geral(self):
        # self.currentFrame = "FrameGeral"
        # print(self.currentFrame)
        # if self.currentFrame =="FrameGeral":
        #     print('Teste ok')
        self.frameGeral = ctk.CTkFrame(master=self.app, corner_radius=False) #, fg_color="red")
        self.frameGeral.pack(fill="both", side="left", expand=True)
        columns = 3

        self.frameGeral.grid_columnconfigure(0, weight=1)
        self.frameGeral.grid_columnconfigure(1, weight=2)
        self.frameGeral.grid_columnconfigure(2, weight=1)
      

    def frame_login(self):
        self.scr_width= self.app.winfo_screenwidth()
        self.scr_height = self.app.winfo_screenheight()
        scr_width = self.scr_width /2
        scr_height=self.scr_height / 2
        #print(scr_width)
        #print(scr_height)
        frameLogin= ctk.CTkFrame(master=self.frameGeral, width=scr_width, height=scr_height)# fg_color="black",
        frameLogin.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        def sair_da_tela():
            frameLogin.place_forget()
            self.frame_inicial()

        # columns=3
        # rows = 6
        # for row in range(rows):
        #     self.frameLogin.rowconfigure(row, weight=1)
        # for column in range(columns):
        #     self.frameLogin.columnconfigure(column,weight=1)

        # ctk.CTkLabel(master=self.frameLogin, text="Insira o nome de usuario").grid(row=2, column=1)

        ctk.CTkLabel(master=frameLogin, text="Usuário", font=("calibri bold", scr_width/20)).place(relx=0.1, rely=0.1)

        userEntry= ctk.CTkEntry(master=frameLogin, placeholder_text="Insira o usuário", width=scr_width/1.2 ,font=("calibri", scr_width/25)).place(relx=0.1, rely=0.25)

        ctk.CTkLabel(master=frameLogin, text="Senha", font=("calibri bold", scr_width/20)).place(relx=0.1, rely=0.4)

        userEntry= ctk.CTkEntry(master=frameLogin, placeholder_text="Insira a senha", width=scr_width/1.2 ,font=("calibri", scr_width/25)).place(relx=0.1, rely=0.55)

        btnLogin = ctk.CTkButton(master=frameLogin, text="Entrar", command=sair_da_tela, width=scr_width/2, font=("calibri", scr_width/20)).place(relx=0.1, rely=0.8)


    def frame_menu_lateral(self):

        image_heigth= round((self.scr_height/100)*4)
        image_width=round((self.scr_width/100)*4)
        image_estoque = ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\box_log_light.png"), dark_image=Image.open(r"Python\rtsApp\box_log_dark.png"), size=(image_heigth, image_width))
        image_cash = ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\cash_cash_light.png"), dark_image=Image.open(r"Python\rtsApp\cash_cash_dark.png"), size=(image_heigth, image_width))
        image_anal = ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\anal_light.png"), dark_image=Image.open(r"Python\rtsApp\anal_dark.png"), size=(image_heigth, image_width))
        image_users =ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\user_light.png"), dark_image=Image.open(r"Python\rtsApp\user_dark.png"), size=(image_heigth, image_width))
        image_config = ctk.CTkImage(light_image=Image.open(r"Python\rtsApp\config_light.png"), dark_image=Image.open(r"Python\rtsApp\config_dark.png"), size=(image_heigth, image_width))
        

        frame_widget_max= self.scr_width/ 4
        frame_wdiget_min= self.scr_width/ 18

        def diminui_menu():
            self.frameMenuLateral.place_forget()


        def aumenta_menu():

            frame_widget = frame_widget_max
            self.frameMenuLateral = ctk.CTkFrame(master=self.FrameSelecinado, width=frame_widget, height=self.scr_height, corner_radius=False)
            self.frameMenuLateral.place(relx=0, rely=0, relheight=1) #, fg_color='yellow')
        
            rows = 6
            self.frameMenuLateral.grid_columnconfigure(0, weight=1)
            for row in range(rows):
                self.frameMenuLateral.grid_rowconfigure(row, weight=1)

            ctk.CTkLabel(master=self.frameMenuLateral, text="RTS SYSTEMS", font=(f"{self.font}", self.scr_width/35)).place(relx=0.05, rely=0.05)    
            
            self.btnEstoque = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Estoque", command=diminui_menu, image=image_estoque, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scr_width/40)).grid(column=0, row=1, padx=self.scr_width/99)#.place(relx=0, rely=0.25)
            self.btnVendas = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Vendas", command=diminui_menu, image=image_cash, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scr_width/40)).grid(column=0, row=2, padx=self.scr_width/99)#.place(relx=0, rely=0.45)
            self.btnAnalise = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Análise", command=diminui_menu, image=image_anal, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scr_width/40)).grid(column=0, row=3, padx=self.scr_width/99)#.place(relx=0, rely=0.65)
            self.btnUsusarios = ctk.CTkButton(master=self.frameMenuLateral, text="Usuarios", command=diminui_menu, image=image_users, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scr_width/40)).grid(column=0, row=4, padx=self.scr_width/99)
            self.btnConfiguracoes = ctk.CTkButton(master=self.frameMenuLateral, text="Configurações", command=diminui_menu, image=image_config, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scr_width/40)).grid(column=0, row=5, padx=self.scr_width/99)

        frame_widget = frame_wdiget_min
        self.frameMenuLateral = ctk.CTkFrame(master=self.FrameSelecinado, width=frame_widget, height=self.scr_height, corner_radius=False)
        self.frameMenuLateral.place(relx=0, rely=0,relheight=1)

        rows = 6
        self.frameMenuLateral.grid_columnconfigure(0, weight=1)
        for row in range(rows):
            self.frameMenuLateral.grid_rowconfigure(row, weight=1)

        ctk.CTkLabel(master=self.frameMenuLateral, text="RTS", font=(f"{self.font}", self.scr_width/41)).place(relx=0.1, rely=0.05)    

        self.btnEstoque = ctk.CTkButton(master=self.frameMenuLateral, text='', command=self.estoque_frame, image=image_estoque, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scr_width/40)).grid(column=0, row=1, padx=self.scr_width/99)#.place(relx=0, rely=0.25)
        self.btnVendas = ctk.CTkButton(master=self.frameMenuLateral, text="", command=self.vendas_frame, image=image_cash, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scr_width/40)).grid(column=0, row=2, padx=self.scr_width/99)#.place(relx=0, rely=0.45)
        self.btnAnalise = ctk.CTkButton(master=self.frameMenuLateral, text="", command=self.analise_frame, image=image_anal, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scr_width/40)).grid(column=0, row=3, padx=self.scr_width/99)#.place(relx=0, rely=0.65)
        self.btnUsusarios = ctk.CTkButton(master=self.frameMenuLateral, text="", command=aumenta_menu, image=image_users, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scr_width/40)).grid(column=0, row=4, padx=self.scr_width/99)
        self.btnConfiguracoes = ctk.CTkButton(master=self.frameMenuLateral, text="", command=aumenta_menu, image=image_config, compound=LEFT, width=frame_widget, corner_radius=False, fg_color="transparent", font=(f"{self.font}", self.scr_width/40)).grid(column=0, row=5, padx=self.scr_width/99)


    def frame_inicial(self):
        
        self.frameInicial = ctk.CTkFrame(master=self.frameGeral, width=self.scr_width, corner_radius=False, border_color="black", border_width=1)
        self.frameInicial.pack(fill='both', side="right", expand=True)
        self.FrameSelecinado = self.frameInicial
        self.frame_menu_lateral()
        
        ctk.CTkLabel(master=self.frameInicial, text="Bem vindo", font=(f"{self.font}", self.scr_width/30)).place(relx=0.1, rely=0.05)

        self.FrameSelecinado = self.frameInicial

    def estoque_frame(self):
        self.FrameSelecinado.pack_forget()
        self.frameEstoque = ctk.CTkFrame(master=self.frameGeral, width=self.scr_width, corner_radius=False, border_color="black", border_width=1)#fg_color="pink",
        self.frameEstoque.pack(fill='both', side="right", expand=True)

        self.FrameSelecinado = self.frameEstoque
        self.frame_menu_lateral()

        ctk.CTkLabel(master=self.frameEstoque, text="Estoque", font=(f"{self.font}", self.scr_width/30)).place(relx=0.1, rely=0.05)

        self.valor= ''
        
        def estoque_Crud():
            pass
            #if prodBtn
        #     global btnClicked
        #     btnClicked = not btnClicked
            
        # btnClicked = False
                #self.frameEstoque
            #     tela = "Fornecedores"

        frameCrud = ctk.CTkFrame(master=self.frameEstoque, width=(self.scr_width)-(self.scr_width/100)*500, corner_radius=False, border_color="black", border_width=1)
        frameCrud.pack(fill='both', side="right", expand=True)
        self.frame_menu_lateral()
        ctk.CTkLabel(master=self.frameEstoque, text="valor", font=(f"{self.font}", self.scr_width/30)).place(relx=0.1, rely=0.05)

        # def estoque_produtos():
        #     print(self.FrameSelecinado)
        #     frameProdutos = ctk.CTkFrame(master=self.frameEstoque, width=(self.scr_width)-(self.scr_width/100)*500, corner_radius=False, border_color="black", fg_color="red", border_width=1)
        #     frameProdutos.pack(fill='both', side="right", expand=True)
        #     self.frame_menu_lateral()
        #     ctk.CTkLabel(master=self.frameEstoque, text="Produtos", font=(f"{self.font}", self.scr_width/30)).place(relx=0.1, rely=0.05)
        #     print(self.FrameSelecinado)

        fornecBtn = ctk.CTkButton(master=self.frameEstoque, text="Fornecedores", command=estoque_Crud, width=(self.scr_width/100)*35, font=(f"{self.font}", self.scr_width/30)).place(relx=0.4, rely=0.25, anchor=CENTER)
        prodBtn = ctk.CTkButton(master=self.frameEstoque, text="Produtos", command=estoque_Crud, width=(self.scr_width/100)*35, font=(f"{self.font}", self.scr_width/30)).place(relx=0.4, rely=0.45,anchor=CENTER)
        analEstoqueBtn = ctk.CTkButton(master=self.frameEstoque, text="Analisar Estoque", command=estoque_Crud, width=(self.scr_width/100)*35, font=(f"{self.font}", self.scr_width/30)).place(relx=0.4, rely=0.65,anchor=CENTER)



    def vendas_frame(self):
        
        self.FrameSelecinado.pack_forget()
        self.frameVendas = ctk.CTkFrame(master=self.frameGeral, width=self.scr_width, corner_radius=False, border_color="black", border_width=1)#fg_color="pink",
        self.frameVendas.pack(fill='both', side="right", expand=True)
        self.FrameSelecinado = self.frameVendas
        self.frame_menu_lateral()

        ctk.CTkLabel(master=self.frameVendas, text="Vendas", font=(f"{self.font}", self.scr_width/30)).place(relx=0.1, rely=0.05)


    def analise_frame(self):
        
        self.FrameSelecinado.pack_forget()
        self.frameAnalise = ctk.CTkFrame(master=self.frameGeral, width=self.scr_width, corner_radius=False, border_color="black", border_width=1)#fg_color="pink",
        self.frameAnalise.pack(fill='both', side="right", expand=True)
        self.FrameSelecinado = self.frameAnalise
        self.frame_menu_lateral()

        ctk.CTkLabel(master=self.frameAnalise, text="Analise", font=(f"{self.font}", self.scr_width/30)).place(relx=0.1, rely=0.05)

        


    # # def frame_menu_lateral(self):

    # #     def estoque_frame():
    # #         self.frameInicial.pack_forget()
    # #         self.frameMenuLateral.place_forget()
    # #         #self.frameEstoque.pack(fill='both', side="right", expand=True)
    # #         self.frame_estoque()
        
    # #     def vendas_frame():
    # #         pass
    # #         #self.frame

    # #     scr_width = self.scr_width
    # #     scr_height = self.scr_height
    # #     self.frameMenuLateral = ctk.CTkFrame(master=self.frameGeral, width=scr_width/ 4, height=scr_height, border_color="black", border_width=1, corner_radius=False)
    # #     self.frameMenuLateral.place(relx=0, rely=0) #, fg_color='yellow')
    # #     #self.frameMenuLateral.pack(fill="y", side="left", expand=True)
    # #     ctk.CTkLabel(master=self.frameMenuLateral, text="RTS Systems", font=(f"{self.font}", scr_width/30)).place(relx=0.05, rely=0.05)

    # #     self.btnEstoque = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Estoque", command=estoque_frame, font=(f"{self.font}", scr_width/40)).place(relx=0.1, rely=0.3)
    # #     self.btnVendas = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Vendas", font=(f"{self.font}", scr_width/40)).place(relx=0.1, rely=0.6)
    # #     self.btnAnalise = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Análise", font=(f"{self.font}", scr_width/40)).place(relx=0.1, rely=0.9)



    

Aplication()