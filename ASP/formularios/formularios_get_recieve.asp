<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

</head>
<body>
    
    <h2>Formulários GET</h2>

    <!-- <form method="get" action="formularios_get.asp">

        Primeiro Nome: <input type="text" name="pnome">
        <br><br>
        Sobrenome: <input type="text" name="snome">
        <br><br>
        <input type="submit" value="enviar">

    </form> -->

    <%
    hidden_valor = request.queryString("hdn-valor")
    

    if hidden_valor = 1 then
    nome = request.queryString("pnome")
    sobrenome = request.queryString("snome")
    request.queryString("hdn-valor")

    response.write("Valor 1 definido!<br>Bem-vindo " & nome & " " & sobrenome & "!")
    
    <!-- elseif request.queryString = "hdn-valor=0" then -->

    elseif hidden_valor = 0 then

    response.write("Valor 0! <br> Preencha novamente os campos")

    end if
    %>

    <!-- <%
    if request.queryString <> "" then
        pnome = request.queryString("pnome")
        snome = request.queryString("snome")
        response.write("Olá " & pnome & " " & snome & "<br>")
    end if
    %>

    <%
    valor = request.queryString("valor")
    response.write "Você clicou no link " & valor & "<p>"
    %>

    <a href="formularios_get.asp?valor=1&">link 1</a>
    <a href="formularios_get.asp?valor=2">link 2</a>
    <a href="formularios_get.asp?valor=3">link 3</a>
    <a href="formularios_get.asp?valor=4">link 4</a>
    <a href="formularios_get.asp?valor=5">link 5</a> -->

</body>
</html>