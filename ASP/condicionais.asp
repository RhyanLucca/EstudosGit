<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h2>Condicionais IF</h2>

        <p>   
            x = "pera" <br><br>
            
            if (x = "maca") then <br>
            response.write("A fruta é uma maçã")
            <br>
            elseif (x = "banana") then <br>
            response.write("A fruta é uma banana")
            <br>
            elseif (x = "laranja") then <br>
            response.write("A fruta é uma laranja")
            <br>
            else <br>
            response.write("A fruta não foi identificada") <br>
            end if
        </p>


        <%
        
        x = "pera"
        
        if (x = "maca") then 
        response.write("<b> Resposta: A fruta é uma maçã <br>")
        
        elseif (x = "banana") then
        response.write("<b> Resposta: A fruta é uma banana <br>")
        
        elseif (x = "laranja") then
        response.write("<b> Resposta: A fruta é uma laranja <br>")
        
        else 
        response.write("<b> Resposta: A fruta não foi identificada</b> <br>")
        end if
        %>
        
    <hr>


        <p>
            y = 20 <br><br>
            
            if (y < 10) then <br>
            response.write( y & " maior que 10") <br>
            
            elseif (y < 50) then <br>
            response.write( y & " menor que 50") <br>
             
            end if
        </p>



        <%
            
        y = 5
        
        if (y < 10) then
        response.write("<b> Resposta:" & y & " maior que 10 </b>")
        
        elseif (y < 50) then
        response.write("<b> Resposta:" & y & " menor que 50 </b>")
        
        end if
        %>
        <hr>
        <br>

        <h2>Condicionais CASE</h2>


        <p>
            dia = weekday(now()) <br><br>

        select case dia <br>
            case 6 <br>
                response.write("Finalmente Sexta") <br>
            case 7 <br>
                resposta.write("Super Sabado") <br>
            case 1 <br>
                resposta.write("Domingo Sonolento") <br>
            case else <br>
                resposta.write("Estou esperando o fim de semana") <br>
        end select
        </p>


        <%
        dia = weekday(now())

        select case dia 
            case 6
                response.write("<b> Finalmente Sexta </b>")
            case 7
                resposta.write("<b> Super Sabado </b>")
            case 1
                resposta.write("<b> Domingo Sonolento </b>")
            case else
                resposta.write("<b> Estou esperando o fim de semana </b>")
        end select
        %>

</body>
</html>