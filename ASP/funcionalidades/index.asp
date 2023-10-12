<% response.charset = "utf-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estudos ASP Classico</title>
    <link rel="stylesheet" type="text/css" href="./style.css" />
</head>
<body>

    <!--#include file="include.asp"-->
    <% response.write("Conexão:" & Session("inicio"))%>

    <div id="menu_principal">
        <ul>
            <li><a href="strings.asp">Strings</a></li>
            <li><a href="variaveis.asp">Variaveis/matrizes</a></li>
            <li><a href="operadores.asp">Operadores</a></li>
            <li><a href="condicionais.asp">Condicionais</a></li>
            <li><a href="loopings.asp">Loopings</a></li>
            <li><a href="funcoes.asp">Funções</a></li>
            <li><a href="formularios/formularios_get.asp">Formulários</a></li>
            <!-- <li><a href="formularios/formularios_get.asp?valor1">Formulários</a></li> -->
            <li><a href="cookies.asp">Cookies</a></li>
            <li><a href="sessao.asp">Sessão</a></li>
            <li><a href="include.asp">Include</a></li>
            <li><a href="global.asa">Global</a></li>
            <li><a href="response.asp">Response/request</a></li>
            <li><a href="server.asp">Server</a></li>
            <li><a href="fileSystem.asp">Objeto File System</a></li>
            <li><a href="dicionarios.asp">Dicionários</a></li>
            <li><a href=""></a>AdRotator</li>
            <li><a href="browserCap.asp">BrowserCap</a></li>
            <li><a href="http://localhost/development/ASP/vamove/crud/index_crud.asp">Crud</a></li>
            <li><a href="http://localhost/development/ASP/vamove/login/login.asp">Fullstack</a></li>
        </ul>
    </div>


    <% 
    Response.write "<h1>" & "Hello ASP" & "</h1>"   
    %>
    <%
    response.write("Essa página armazenará todo o conteúdo de ASP Classico")
    %>

    <p>Para sabermos seu nome digite na aba de cookies</p>
    <%
        usuario = request.cookies("usuario")

        response.write("O usuario conectado é: " & usuario & "<br>Sessão iniciada às: " & session("entrada"))
    %>
    <br><br>
    <hr>

</body>
</html>