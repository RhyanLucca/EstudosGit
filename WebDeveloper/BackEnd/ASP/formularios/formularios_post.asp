<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        span{
            font-weight: bold;
        }
    </style>

</head>
<body>
    
    <h2>Formulários POST</h2>

    <form method="post" action="formularios_post.asp">

        Primeiro Nome: <input type="text" name="pnome">
        <br><br>
        Sobrenome: <input type="text" name="snome">
        <br><br>
        <input type="submit" value="enviar">

    </form>

    <%
    if request.form <> "" then
        pnome = request.form("pnome")
        snome = request.form("snome")
        response.write("Olá " & pnome & " " & snome)
    end if
    %>

    
    

</body>
</html>