<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <h2>Estrutura de repetição FOR</h2>

    <p>    
    for x=1 to 10 <br>
        response.write("Linha" & x &) <br>
    next
    </p>

    <%
    for x=1 to 10
        response.write("Linha" & x & "<br>")
    next
    %>

    <hr>

    <h2>Estrutura de repetição WHILE</h2>

    <%

    x = 1

    while (x < 10000)
        response.write(x)
        x = x * 2
        response.write( " vezes 2 é igual a " & x & "<br>")
    wend
    %>

</body>
</html>