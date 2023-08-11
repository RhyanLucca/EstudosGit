pip install Django 

            #Conjunto de aplicativos
Django-admin startproject "Nome do projeto"

    Manage.py - ultilitario de linha de comando que interage com o projeto django de diversas maneiras

    init.py Arquivo que diz ao python que o diretório deve ser tratado como um pacote

    settings.py arquivo de configurações do projeto, onde descrevemos e detalhamos como o projeto funciona e quais definições estão disponisveis

    urls.py arquivo de url, onde armazena-se as urls para o projeto

    wsgi.py integração de servidores web que implementa o padrão wsgi (Utilizado em deploy)

    asgi.py integração de servidores web que utiliza comunicação assincrona 

    #apps
    python manage.py startapp "Nome do app" (necessario instalar a pasta do app como um aplicativo em setting.py installed apps)

    view.py: responsável por encapsular a lógica que recebe e responde as requisições dos usuarios e pode ou não definir comportamentos especificos como buscar informações no banco de dados. Toda view é uma função de retorno vinculada a uma url configurada no arquivo de urls, sendo assim não existe uma url sem um retorno de view

    models.py representação exata do banco de dados onde as classes são tabelas e seus atributos são os campos das tabelas. 
    Essa camada guarda as informações disponibilizadas para outras camadas da aplicação.

        #Avisar o Django sobre alguma alteração dos modelos no banco de dados
        python manage.py makemigrations usuarios

        #Rodar as migrações de forma automática, sincronizando o banco com as informações na camada de modelo
        python manage.py migrate

        #Criar um super usuario para poder fazer as primeiras informações do site
        python manage.py createsuperuser
        

python manage.py runserver
