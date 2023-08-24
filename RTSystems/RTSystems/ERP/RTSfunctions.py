import mysql.connector
from mysql.connector import Error
import time
import customtkinter as ctk


def funcao(nome, sobrenome):
    #nome = nome
    #sobrenome = "Lucca"
    texto = "Uma fução retorna valores, seja através do print ou atraves do return"
    completo = nome + ' ' + sobrenome + f"\n{texto}"
    #return completo
    print(completo)


def metodo():
    print("Um método não retorna valores")


def teste():
    metodo()
    print(funcao())


def soma(*args):
    
    sum = 0

    for r in args:
        sum += r

    print(sum)


def db_connect():
        
        global con, cursor
        
        con = mysql.connector.connect(
        user= 'root',
        password= '@RhyanLucca1000',
        host= 'localhost',
        database= 'RTSystems'
        )

        cursor = con.cursor()


def buscarUsuario(name, password):
     
    strSQL = f"SELECT usersNome, usersPswd, usersPermissao FROM users WHERE usersNome = '{name}' AND usersPswd = '{password}';"
    
    cursor.execute(strSQL)

    resultado= cursor.fetchone()
            
    if resultado:
        
        global user, senha, permissao, tipoUser
        user = resultado[0]
        senha = resultado[1]
        permissao = resultado[2]

        if permissao == '1':
            tipoUser = 1
        elif permissao == '0':
            tipoUser = 0

        entrar = True
        arrayUser = [entrar, user, senha, permissao, tipoUser]

    else:
        entrar = False
        arrayUser = [entrar]

    return arrayUser


def inserirUsuario(nome, senha, permissao):
    
    strSQL = f"INSERT INTO users VALUES(NULL, '{nome}', '{senha}', {permissao});"
    
    cursor.execute(strSQL)
    con.commit()


# def showMsg(text, size, width):

#     currentFrame= rts.currentFrame

#     msg = ctk.CTkLabel(master=currentFrame, text=text, font=(f"Arial Bold", size), width=width)
#     msg.place(relx=0, rely=1)
#     print("msg ok")

#     print(f"msg = ctk.CTkLabel(master=, text='{text}', font=(f'Arial Bold', {size}))")
