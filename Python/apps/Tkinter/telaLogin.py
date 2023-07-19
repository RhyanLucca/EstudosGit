import customtkinter as ctk
from tkinter import *
from PIL import Image
from tkinter import messagebox


janela = ctk.CTk()

class Aplication():

    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()


    def tema(self):
        ctk.set_default_color_theme("green")
        ctk.set_appearance_mode("dark")


    def tela(self):
        janela.title("CTK TESTE")
        janela.geometry("700x450")
        janela.iconbitmap("apps\Tkinter\planejamento.ico")
        janela.resizable(False, False)


    def tela_login(self):

        #Trabalhando com a imagem da tela
        img = ctk.CTkImage(light_image=Image.open(r"apps\Tkinter\img.png"), dark_image=Image.open(r"apps\Tkinter\img.png"), size=(400,400))
        label_img = ctk.CTkLabel(master=janela, text=None, image=img, bg_color="transparent").place(x=5, y=65)

        label_tt = ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha\nacesso a plataforma", font=("Roboto", 20), text_color="green").place(x=20, y=10)

        #Frame
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT, padx=10)

        #Frame widgets
        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=("Roboto", 20)).place(x=25, y=5)

        register_span= ctk.CTkLabel(master=login_frame, text="Certifique-se de que os dados estão corretos", font=('Roboto', 11)).place(x=25, y=35)


        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14)).place(x=25, y=85)
        username_label1 = ctk.CTkLabel(master=login_frame, text="O campo nome de usuário é obrigatório", text_color="green", font=("Roboto", 11)).place(x=25, y=115)

        pswd_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha de usuário", width=300, font=("Roboto", 14), show="*").place(x=25, y=155)
        pswd_label = ctk.CTkLabel(master=login_frame, text="O campo senha de usuário é obrigatório", text_color="green", font=("Roboto", 11)).place(x=25, y=185)

        checkboxLembrar = ctk.CTkCheckBox(master=login_frame, text="Lembrar informações de login", fg_color="green").place(x=25, y=225)

        def login():
            msg = messagebox.showinfo(title="Cadastro realizado", message="Seu usuário foi cadastrado com sucesso!")

        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300, command=login).place(x=25, y=270)
        

        
        def tela_register():
            #Remover o frame de login
            login_frame.pack_forget()
            
            #Atualizar o frame PARA CADASTROS
            register_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            register_frame.pack(side=RIGHT, padx=10)

            label = ctk.CTkLabel(master=register_frame, text="Cadastro de novo usuário", font=("Roboto", 20)).place(x=25, y=5)

            register_span= ctk.CTkLabel(master=register_frame, text="Todos os dados são obrigatórios", font=('Roboto', 11)).place(x=25, y=35)


            RGusername_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14)).place(x=25, y=75)

            RGemail_entry = ctk.CTkEntry(master=register_frame, placeholder_text="E-mail", width=300, font=("Roboto", 14)).place(x=25, y=125)

            RGpswd_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Senha", show="*", width=300, font=("Roboto", 14)).place(x=25, y=175)

            RGconfPswd_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Confirme a senha", show="*", width=300, font=("Roboto", 14)).place(x=25, y=225)
            
            termos_check = ctk.CTkCheckBox(master=register_frame, text="Aceito os termos de privacidade").place(x=25, y=275)

            def back_button():
                #Removendo frame de cadastro
                register_frame.pack_forget()

                #devolvendo o frame de login
                login_frame.pack(side=RIGHT, padx=10)
                pass

            btn_voltar = ctk.CTkButton(master=register_frame, text="Voltar", fg_color="gray", hover_color="black",command=back_button).place(x=25, y=325)

            def save_user():
                msg = messagebox.showinfo(title="Cadastro realizado", message="Seu usuário foi cadastrado com sucesso!")
                pass

            btn_cadastrar = ctk.CTkButton(master=register_frame, text="Cadastrar", command=save_user). place(x=185, y=325)


        register_span = ctk.CTkLabel(master=login_frame, text="Se não tem uma conta").place(x=25, y=315)
        register_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", fg_color="green", width=150, command=tela_register).place(x=175, y=315)



Aplication()
