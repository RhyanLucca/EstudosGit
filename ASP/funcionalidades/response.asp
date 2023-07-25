<p>
< %="Esse texto foi escrito sem o uso da tag <b>RESPONSE.WRITE</b>"
</p>
<p>
Response.Redirect "LINK" (Redireciona o usuario para o link selecionado<!--redireciona o usuario para a tela que quisermos-->
</p>

<p>
response.end (Encerra a execução do script) <!--Encerra a execução do script-->
</p>

<p>
<%
navegador = request.ServerVariables("http_user_agent")
servidor = request.ServerVariables("server_software")

response.write("O navegador usado pelo usuario é: <br><br>" &navegador & "<br><br>")
response.write("O servidor do usuario é: <br><br>" &servidor)

%>
</p>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>