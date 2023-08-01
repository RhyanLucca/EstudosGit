<% response.charset = "utf-8"%>
<%
set dicionario = server.CreateObject("Scripting.Dictionary")

dicionario.Add "SP", "São Paulo"
dicionario.Add "Rj", "Riode Janeiro"
dicionario.Add "MG", "Minas Gerais"
dicionario.Add "ES", "Espirito Santo"

total = dicionario.count

response.write("MG é a sigla de " & dicionario.item("MG") & "<br>")
response.write("Existem " & total & "registros no dicionário")
%>