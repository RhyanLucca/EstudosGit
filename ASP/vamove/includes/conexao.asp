<%
strDB = "rhyanDb"

Set conDB = Server.CreateObject("ADODB.Connection")

strConexaoDB= "driver={MySQL ODBC 5.2 Driver};server=localhost;uid=root;pwd=@RhyanLucca1000;database=" & strDB & ";"

session("connectionString")= strConexaoDB

conDB.connectionString= Session("connectionString")
conDB.Open

response.write("Conexão OK")
%>