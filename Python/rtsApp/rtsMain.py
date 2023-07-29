import customtkinter as ctk
from tkinter import *

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
        #ctk.set_appearance_mode("dark")
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


    def frame_inicial(self): 

        def estoque_frame():
            self.frameInicial.pack_forget()
            self.frameMenuLateral.place_forget()
            #self.frameEstoque.pack(fill='both', side="right", expand=True)
            self.frame_estoque()
            btn_abreMenu = ctk.CTkButton(master=self.frameEstoque, text="Menu", width=self.scr_width/50, font=(f"{self.font}", self.scr_width/70))
            btn_abreMenu.place(relx=0.01, rely=0.01)

        def vendas_frame():
            self.frameInicial.pack_forget()
            self.frameMenuLateral.place_forget()
            #self.frameEstoque.pack(fill='both', side="right", expand=True)
            self.vendas_frame()
            btn_abreMenu = ctk.CTkButton(master=self.frameEstoque, text="Menu", width=self.scr_width/50, font=(f"{self.font}", self.scr_width/70))
            btn_abreMenu.place(relx=0.01, rely=0.01)
        
        def analise_frame():
            self.frameInicial.pack_forget()
            self.frameMenuLateral.place_forget()
            #self.frameEstoque.pack(fill='both', side="right", expand=True)
            self.analise_frame()
            btn_abreMenu = ctk.CTkButton(master=self.frameEstoque, text="Menu", width=self.scr_width/50, font=(f"{self.font}", self.scr_width/70))
            btn_abreMenu.place(relx=0.01, rely=0.01)

        self.frameInicial = ctk.CTkFrame(master=self.frameGeral, width=self.scr_width, corner_radius=False, border_color="black", border_width=1)
        self.frameInicial.pack(fill='both', side="right", expand=True)
        #self.frame_menu_lateral()
        ctk.CTkLabel(master=self.frameInicial, text="Bem vindo", font=(f"{self.font}", self.scr_width/30)).place(relx=0.3, rely=0.05)

        scr_width = self.scr_width
        scr_height = self.scr_height
        self.frameMenuLateral = ctk.CTkFrame(master=self.frameInicial, width=scr_width/ 4, height=scr_height, border_color="black", border_width=1, corner_radius=False)
        self.frameMenuLateral.place(relx=0, rely=0) #, fg_color='yellow')
        #self.frameMenuLateral.pack(fill="y", side="left", expand=True)

        ctk.CTkLabel(master=self.frameMenuLateral, text="RTS Systems", font=(f"{self.font}", scr_width/30)).place(relx=0.05, rely=0.05)

        self.btnEstoque = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Estoque", command=estoque_frame, font=(f"{self.font}", scr_width/40)).place(relx=0.1, rely=0.3)
        self.btnVendas = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Vendas", command=vendas_frame, font=(f"{self.font}", scr_width/40)).place(relx=0.1, rely=0.6)
        self.btnAnalise = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Análise", command=analise_frame, font=(f"{self.font}", scr_width/40)).place(relx=0.1, rely=0.9)


    def frame_estoque(self):
        self.currentFrame = "frameEstoque"
        print(self.currentFrame)
        if self.currentFrame =="frameEstoque":
            print('Frame estoque ok')
        self.frameEstoque = ctk.CTkFrame(master=self.frameGeral, width=self.scr_width, corner_radius=False, border_color="black", border_width=1)#fg_color="pink",
        self.frameEstoque.pack(fill='both', side="right", expand=True)
        # self.frame_menu_lateral()
        ctk.CTkLabel(master=self.frameEstoque, text="Estoque", font=(f"{self.font}", self.scr_width/30)).place(relx=0.3, rely=0.05)

    def vendas_frame(self):
        self.currentFrame = "frameEstoque"
        print(self.currentFrame)
        if self.currentFrame =="frameEstoque":
            print('Frame estoque ok')
        self.frameEstoque = ctk.CTkFrame(master=self.frameGeral, width=self.scr_width, corner_radius=False, border_color="black", border_width=1)#fg_color="pink",
        self.frameEstoque.pack(fill='both', side="right", expand=True)
        # self.frame_menu_lateral()
        ctk.CTkLabel(master=self.frameEstoque, text="Vendas", font=(f"{self.font}", self.scr_width/30)).place(relx=0.3, rely=0.05)

    def analise_frame(self):
        self.currentFrame = "frameEstoque"
        print(self.currentFrame)
        if self.currentFrame =="frameEstoque":
            print('Frame estoque ok')
        self.frameEstoque = ctk.CTkFrame(master=self.frameGeral, width=self.scr_width, corner_radius=False, border_color="black", border_width=1)#fg_color="pink",
        self.frameEstoque.pack(fill='both', side="right", expand=True)
        # self.frame_menu_lateral()
        ctk.CTkLabel(master=self.frameEstoque, text="Analise", font=(f"{self.font}", self.scr_width/30)).place(relx=0.3, rely=0.05)

        


    # def frame_menu_lateral(self):

    #     def estoque_frame():
    #         self.frameInicial.pack_forget()
    #         self.frameMenuLateral.place_forget()
    #         #self.frameEstoque.pack(fill='both', side="right", expand=True)
    #         self.frame_estoque()
        
    #     def vendas_frame():
    #         pass
    #         #self.frame

    #     scr_width = self.scr_width
    #     scr_height = self.scr_height
    #     self.frameMenuLateral = ctk.CTkFrame(master=self.frameGeral, width=scr_width/ 4, height=scr_height, border_color="black", border_width=1, corner_radius=False)
    #     self.frameMenuLateral.place(relx=0, rely=0) #, fg_color='yellow')
    #     #self.frameMenuLateral.pack(fill="y", side="left", expand=True)
    #     ctk.CTkLabel(master=self.frameMenuLateral, text="RTS Systems", font=(f"{self.font}", scr_width/30)).place(relx=0.05, rely=0.05)

    #     self.btnEstoque = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Estoque", command=estoque_frame, font=(f"{self.font}", scr_width/40)).place(relx=0.1, rely=0.3)
    #     self.btnVendas = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Vendas", font=(f"{self.font}", scr_width/40)).place(relx=0.1, rely=0.6)
    #     self.btnAnalise = ctk.CTkButton(master=self.frameMenuLateral, text="RTS Análise", font=(f"{self.font}", scr_width/40)).place(relx=0.1, rely=0.9)



    

Aplication()
