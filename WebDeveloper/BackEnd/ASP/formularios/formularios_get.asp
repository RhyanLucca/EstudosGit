<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <form method="get" action="formularios_get_recieve.asp">

        Primeiro nome: <input id="pnome" name="pnome" type="text">
        <br><br>
        Sobrenome: <input id="snome" name="snome" type="text">
        <input id="hdn-valor" name="hdn-valor" type="hidden" value="">
        <br><br>
        <input onclick="validaPreenchimento()" type="submit">

    <!-- <a href="formularios_get_recieve.asp">Proxima pagina</a> -->

    </form>


    <script>
        
        function validaPreenchimento(){

            var primeiro_nome = document.getElementById("pnome").value
            var sobrenome = document.getElementById("snome").value

            if (primeiro_nome != "" && sobrenome != ""){
                var hidden_valor = document.getElementById("hdn-valor").value = 1
            } else 
                var hidden_valor = document.getElementById("hdn-valor").value = 0
        }

        // var hidden_valor = document.getElementById("hdn-valor").value
        // document.write(hidden_valor)

    </script>


    <%
     if request.queryString <> "" then
        request.queryString("pnome")
        request.queryString("snome")
        request.queryString("hdn-valor")
    end if

    %>

    
</body>
</html>