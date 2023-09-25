<% response.charset = "utf-8"%>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h2>Funções</h2>

    <h4>Funções com string</h4>

    <p>
    <!-- function RetornaDiaSemana(data) -->
    function RetornaDiaSemana() <br><br>


    dim dias(8) <br><br>

    dias(1) = "Domingo"<br>
    dias(2) = "Segunda"<br>
    dias(3) = "Terça"<br>
    dias(4) = "Quarta"<br>
    dias(5) = "Quinta"<br>
    dias(6) = "Sexta"<br>
    dias(7) = "Sabado"<br><br>

    <!-- diaSemana = weekday(data) -->

    diaSemana = weekday(now()) <br><br>

    RetornaDiaSemana = dias(diaSemana) <br>
    end function <br><br>

    <!-- response.write RetornaDiaSemana("23/01/2003") -->
    response.write RetornaDiaSemana()
    </p>

    <hr>
    <%
    function RetornaDiaSemana()


    dim dias(8)

    dias(1) = "Domingo"
    dias(2) = "Segunda"
    dias(3) = "Terça"
    dias(4) = "Quarta"
    dias(5) = "Quinta"
    dias(6) = "Sexta"
    dias(7) = "Sabado"

    <!-- diaSemana = weekday(data) -->

    diaSemana = weekday(now())

    RetornaDiaSemana = dias(diaSemana)
    end function

    <!-- response.write RetornaDiaSemana("23/01/2003") -->
    response.write RetornaDiaSemana()
    %>

    <hr>

    <h3>Funções com valores numéricos</h3>
    <p>
        function CalculaIdade(idade) <br><br>

    if (idade < 18) then <br>
        response.write("Você é de menor") <br>

    elseif (idade > 18 and idade < 50) then <br>
        response.write("Você é um adulto") <br>
    else <br>
        response.write("Você é um idoso") <br>
    end if <br>

    end function <br><br>

    idade = 20 <br> <br>

    CalculaIdade(idade)
    </p>

    <hr>
    <%
    
    function CalculaIdade(idade)

    if (idade < 18) then
        response.write("Você é de menor")

    elseif (idade > 18 and idade < 50) then

        response.write("Você é um adulto")
    else
        response.write("Você é um idoso")
    end if

    end function

    idade = 20

    CalculaIdade(idade)
    %>

    <hr>

    <h2>Procedures</h2>

    <p>Executa um procedimento que executa instruções mas não retorna um valor</p>

    <p>
        sub EscreveTexto(texto) <br>
        response.write texto <br>
    end sub <br><br>
    
    EscreveTexto("Essa é um texto de teste")

    </p>

    <hr>

    <%
    sub EscreveTexto(texto)
        response.write texto
    end sub
    
    EscreveTexto("Essa é um texto de teste")

    %>

 
</body>
</html>