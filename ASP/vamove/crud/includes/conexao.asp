<%

strDB = "rhyandb"

'Cria uma nova instancia da Classe formando o Objeto'
Set conDB = Server.CreateObject("ADODB.Connection")

strConexaoDB= "Driver={SQL Server Native Client 11.0};Server=FRANCO-0106;Uid=sa;Pwd=123456;Database=" & strDB

session("connectionString")= strConexaoDB

'Abre a conexão com o Banco de Dados'
conDB.connectionString= session("connectionstring")
conDB.Open

'response.write("Conexão OK")'
%>