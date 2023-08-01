<!DOCTYPE html>

    <%
    if request.form <> "" then

        usuario = request.form("usuario")

        response.cookies("usuario") = usuario

        <!-- response.cookies("usuario").expires=#july 25, 2023# -->

        mensagem ="Usuario " & usuario & " conectado"

    else

        mensagem= ("digite  o seu nome de usuário" & "<p></p>")

    end if

    %>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <form method="post">

        Nome: <input type="text" name="usuario">
        <br>
        <input type="submit" value="Enviar">

    </form>

    <a href="index.asp">index</a>

</body>
</html> 