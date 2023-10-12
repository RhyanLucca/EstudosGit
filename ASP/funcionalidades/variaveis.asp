<% response.charset = "utf-8"%>

<%

Response.write("<h3>" & "Declaração de variáveis" & "</h3>")

dim nome
nome = "Rhyan Lucca"
sobrenome = "Borges"

response.write("dim nome" & "<br>" & "nome = 'Rhyan Lucca'" & "<br>" & "sobrenome = 'Borges' " & "<br>" & "response.write(nome & ' ' & sobrenome)" & "<br><br>")

response.write(nome & " " & sobrenome & "<br><br>")



Response.write("<h3>" & "Declaração de matrizes" & "</h3>")

dim frutas(3)
    frutas(0) = "Banana"
    frutas(1) = "Maçã"
    frutas(2) = "Morango"

response.write(frutas(0) & "<br>")
response.write(frutas(1) & "<br>")
response.write(frutas(2) & "<br>")

%>