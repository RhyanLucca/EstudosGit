<%

strDB = "rhyandb"

'Cria uma nova instancia da Classe formando o Objeto'
Set conDB = Server.CreateObject("ADODB.Connection")

strConexaoDB= "driver={MySQL ODBC 5.1 Driver};server=localhost;uid=root;pwd=@RhyanLucca1000;database=" & strDB

session("connectionString")= strConexaoDB

'Abre a conexão com o Banco de Dados'
conDB.connectionString= session("connectionstring")
conDB.Open

response.write("Conexão OK")
%>