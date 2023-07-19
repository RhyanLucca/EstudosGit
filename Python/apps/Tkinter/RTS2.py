import customtkinter as ctk
from tkinter import *
from tkinter import Tk

rts = ctk.CTk()

class Aplication():

    def __init__(self):
        self.rts=rts
        self.conf_janela()
        self.framesInit()


        self.rts.mainloop()

    def conf_janela(self):
        self.rts.title("RTSystems")
        #self.rts.geometry("1200x600")
        self.rts.minsize(width=1000, height=500)
        #self.rts.attributes("-fullscreen", True)
        self.rts.wm_state('zoomed')
        
        #self.rts.maxsize(width=1000, height=700)
        #rts.grid_columnconfigure()
        
    def framesInit(self):


        self.frameLog = ctk.CTkFrame(master=self.rts, border_width=2, border_color="black", corner_radius=False)#fg_color="white"
        self.frameLog.pack(side="left", fill="both", expand=True)


        self.labelLog = ctk.CTkLabel(master=self.frameLog, text="RTS ESTOQUE", font=("roboto bold", 20))
        self.labelLog.place(relx=0.1, rely=0.07)
        
        self.frameCash = ctk.CTkFrame(master=self.rts, border_width=2, border_color="black", corner_radius=False)#fg_color="white"
        self.frameCash.pack(side="left", fill="both", expand=True)

        self.labelCash = ctk.CTkLabel(master=self.frameCash, text="RTS CAIXA", font=("roboto bold", 20))
        self.labelCash.place(relx=0.1, rely=0.07)

        self.frameCont = ctk.CTkFrame(master=self.rts, border_width=2, border_color="black", corner_radius=False)#fg_color="white"
        self.frameCont.pack(side="left", fill="both", expand=True)

        self.labelCont = ctk.CTkLabel(master=self.frameCont, text="RTS ANALISES", font=("roboto bold", 20))
        self.labelCont.place(relx=0.1, rely=0.07)

        rights=ctk.CTkLabel(self.frameCont, text="DESENVOLVIDO POR RTS SYSTEMS ®", bg_color='transparent')
        rights.pack(fill="x", side="bottom", padx=5, pady=5)

        self.frameLog.grid_columnconfigure(0, weight=1)
        self.frameCash.grid_columnconfigure(0, weight=1)
        self.frameCont.grid_columnconfigure(0, weight=1)



        #ESTOQUE BUTTONS

        btn_fornec= ctk.CTkButton(master=self.frameLog, width=250, height=50, font=("roboto bold", 16), text="FORNECEDORES",).place(relx=0.1 , rely=0.2)
        
        
        btn_prod= ctk.CTkButton(master=self.frameLog, width=250, height=50, font=("roboto bold", 16), text="PRODUTOS",).place(relx=0.1 , rely=0.4)
        
        
        btn_pac= ctk.CTkButton(master=self.frameLog, width=250, height=50, font=("roboto bold", 16), text="PACOTES",).place(relx=0.1 , rely=0.6)
        

        btn_cont= ctk.CTkButton(master=self.frameLog, width=250, height=50, font=("roboto bold", 16), text="CONTAGEM",).place(relx=0.1 , rely=0.8)
        

        #CAIXA BUTTONS

        btn_caixa= ctk.CTkButton(master=self.frameCash, width=250, height=50, font=("roboto bold", 16), text="CAIXA REGISTRADORA",).place(relx=0.15 , rely=0.2)

        btn_sangria= ctk.CTkButton(master=self.frameCash, width=250, height=50, font=("roboto bold", 16), text="SANGRIA",).place(relx=0.15 , rely=0.4)

        #btn_pac= ctk.CTkButton(master=self.frameLog, width=150, height=35, font=("roboto bold", 16), text="PACOTES",).place(relx=0.25 , rely=0.6)

        #btn_cont= ctk.CTkButton(master=self.frameLog, width=150, height=35, font=("roboto bold", 16), text="CONTAGEM",).place(relx=0.25 , rely=0.8)



        #ANALISE BUTTONS

        btn_analVendas= ctk.CTkButton(master=self.frameCont, width=250, height=50, font=("roboto bold", 16), text="ANALISE DE VENDAS",).place(relx=0.15 , rely=0.2)

        btn_analEstoque= ctk.CTkButton(master=self.frameCont, width=250, height=50, font=("roboto bold", 16), text="ANALISE DE MERCADORIA",).place(relx=0.15 , rely=0.4)

        btn_dash= ctk.CTkButton(master=self.frameCont, width=250, height=50, font=("roboto bold", 16), text="DASHBOARDS",).place(relx=0.15 , rely=0.6)
        


Aplication()