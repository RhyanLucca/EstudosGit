import customtkinter as ctk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
import mysql.connector
from mysql.connector import Error


app = ctk.CTk()

class Models():
    
    query

    def db_connect():
        
        con = mysql.connector.connect(
        user= 'root',
        password= '@RhyanLucca1000',
        host= 'localhost',
        database= 'RTSystems'
        )

        cursor = con.cursor()

class Views():

    def __init__(self):
        self.app = app
        self.app.geometry("700x700")
        self.app.title("RTS Systems")
        self.teste()
        app.mainloop()
        
    def teste(self):
        btnTeste = ctk.CTkButton(master=app, text="Teste", command=Controller.teste)
        btnTeste.pack()

class Controller(Models):

    def __init__(self) -> None:
        super().__init__()
    
    def teste(Models):
        print("Botão pressionado")
        con = Models.db_connect()
        teste = Models.db_connect.

        print("Conexão bem sucedida")




    

Views()
Controller()