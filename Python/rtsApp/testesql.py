import pyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'FRANCO-0106'
DATABASE_NAME = 'RTSystems'

def retornar_conexao():
    server = 'FRANCO-0106'
    database = 'RTSystems'
    username = 'sa'
    password = '123456'
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    #string_conexao = 'Driver={SQL Server Native Client 11.0}; server = '+server+' ;Database = '+database+' ;Trusted_Connection=yes'
    conexao = odbc.connect(string_conexao)
    return conexao.cursor()

retornar_conexao()
