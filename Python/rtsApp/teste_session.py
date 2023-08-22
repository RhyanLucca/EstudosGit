import customtkinter as ctk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
import mysql.connector
from mysql.connector import Error

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
        
        def exit_screen():

            query = "SELECT usersNome, usersPswd FROM users;"

            cursor = Aplication.db_connect(self)

            self.cursor.execute(query)

            listaUser= self.cursor.fetchall()

            entryUser = userEntry.get()
            entryPswd = senhaEntry.get()

            #print(entry)

            # print(listaUser)

            for r in listaUser:
                #user = r[0]
                senha = r[1]
                #print(senha)

                if entryUser in r and entryPswd == senha:
                    print(f"Ok: {entryUser}, {entryPswd}")

                    global session
                    session = True
                    loginFrame.place_forget()
                    self.initial_frame()
                
                else:# not entryUser in r and entryPswd == senha:
                    ctk.CTkLabel(master=loginFrame, text="Usuário ou senha incorretos.", text_color="red", font=(f"{self.font}", self.scrWidth/50)).place(relx=0.1, rely=0.65)


        ctk.CTkLabel(master=loginFrame, text="Usuário", font=(f"{self.font}", self.scrWidth/40)).place(relx=0.1, rely=0.1)

        userEntry= ctk.CTkEntry(master=loginFrame, placeholder_text="Insira o usuário", width=scrWidth/1.2 ,font=(f"{self.font}", self.scrWidth/40))
        userEntry.place(relx=0.1, rely=0.25)


        ctk.CTkLabel(master=loginFrame, text="Senha", font=(f"{self.font}", self.scrWidth/40)).place(relx=0.1, rely=0.4)

        senhaEntry= ctk.CTkEntry(master=loginFrame, show="*", placeholder_text="Insira a senha", width=scrWidth/1.2 ,font=(f"{self.font}", self.scrWidth/40))
        senhaEntry.place(relx=0.1, rely=0.55)

        btnLogin = ctk.CTkButton(master=loginFrame, text="Entrar", command=exit_screen, width=scrWidth/2, font=(f"{self.font}", self.scrWidth/40)).place(relx=0.1, rely=0.8)
