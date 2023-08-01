<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<%
set navegador = server.CreateObject("MSWC.BrowserType")
<!-- response.write("O seu navegador é o " & navegador.browser) -->
%>

<table border="1" width="100%">
    <th>Sistema Operacional</th>
    <th><%=navegador.platform%></th>
    <tr></tr>
    <td>Navegador</td>
    <td><%=navegador.browser%></td>
    <tr></tr>
    <td>Versão do navegador</td>
    <td><%=navegador.version%></td>
    <tr></tr>
    <td>Suporte a frames?</td>
    <td><%=navegador.frames%></td>
    <tr></tr>
    <td>Suporte a tabelas?</td>
    <td><%=navegador.tables%></td>
    <tr></tr>
    <td>Suporte a Som?</td>
    <td><%=navegador.backgroundsounds%></td>
    <tr></tr>
    <td>Suporte a Cookies?</td>
    <td><%=navegador.cookies%></td>
    <tr></tr>
    <td>Suporte a VBScript?</td>
    <td><%=navegador.vbscript%></td>
    <tr></tr>
    <td>Suporte a JavaScript?</td>
    <td><%=navegador.javascript%></td>
</table>
</body>
</html>