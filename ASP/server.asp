<% response.charset = "utf-8"%>
<%
caminho = server.MapPath("index.asp")

response.write("O arquivo INDEX.ASP está na pasta " & caminho & "<br><br>")


texto = "<table border=1><tr><td>Texto 1</td></tr></table>"

response.write (texto & "(Sem HTMLEncode) <br><br>")
response.write server.HTMLEncode (texto & " (Com HTMLEncode)")
%>