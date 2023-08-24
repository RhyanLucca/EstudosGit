import customtkinter as ctk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
import mysql.connector
from mysql.connector import Error
import time

def teste():
    print("Teste Concluido")

def db_connect(self):
    
    con = mysql.connector.connect(
    user= 'root',
    password= '@RhyanLucca1000',
    host= 'localhost',
    database= 'RTSystems'
    )
    cursor = con.cursor()

def login(usuario, senha):

    query = f"SELECT usersNome, usersPswd, usersPermissao FROM users WHERE usersNome = '{usuario}' AND usersPswd = '{senha}';"

    db_connect()
        
    cursor = db_connect(cursor)

    curso

    resultado= cursor.fetchone()
    
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