<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operadores</title>
</head>
<body>
    
    <h2>Operadores matemáticos</h2>

    <%
        x= 10
        y=5
    %>

        <p>x = 10</p>
        <hr>

        <p>response.write( x + 2) Soma</p>

        <%
        response.write( x + 2)
        %>
        <hr>
        
        <p>response.write( 50 - x) Subtração</p>

        <%
        response.write( 50 - x )
        %>
        <hr>

        <p>response.write(5 * x) Multiplicação</p>

        <%
        response.write( 5 * x)
        %>
        <hr>

        <p>response.write( x / 5) Divisão</p>

        <%
        response.write( x / 5)
        %>
        <hr>
        <br>


    <h2>Operadores de comparação (True/False)</h2>

        <p>x = 10</p>
        <p>y = 5</p>
        <hr>

        <p>response.write( x = 8) Igual à</p>

        <%
        response.write( x = 8)
        %>
        <hr>

        <p>response.write( x <> 8) Diferente de</p>

        <%
        response.write( x <> 8)
        %>
        <hr>

        <p>response.write( x > y) Maior que</p>

        <%
        response.write( x > y)
        %>
        <hr>

        <p>response.write( y < y) Menor que</p>

        <%
        response.write( y < y)
        %>
        <hr>

        <p>response.write( y >= 5) Maior igual</p>

        <%
        response.write( y >= 5)
        %>
        <hr>

        <p>response.write( y <= x) Menor igual</p>

        <%
        response.write( y <= x)
        %>
        <hr>
        <br>

    <h2>Operadores lógicos</h2>

        <p>x = 10</p>
        <p>y = 5</p>
        <hr>

        <p>response.write( x > y AND y < 100) Ambas as condições devem ser verdadeiras</p>

        <%
        response.write(x > y AND y < 100)
        %>
        <hr>

        <p>response.write( x > y OR y > 100) Apenas uma condição precisa ser verdadeira</p>

        <%
        response.write( x > y OR y > 100)
        %>
        <hr>

        <p>response.write(not(x = y)) Inverte o valor da condição</p>

        <%
        response.write(not(x = y))
        %>
        <hr>



</body>
</html>