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
    
    <h2>Objeto File System</h2>
    <hr>
    <h4>Criação de arquvio para o desktop</h4>
    <%
dim fs, fname

set fs = Server.CreateObject("Scripting.FileSystemObject")
set fname = fs.CreateTextFile("C:\inetpub\wwwroot\Development\ASP\ArquivoFileSystems", true)

fname.writeLine("Olá mundo")
fname.close
set fname = nothing
set fs= nothing

response.write("Arquivo Criado")
%>

<br><br><br>
<h4>Verificação de pastas no desktop</h4>

<%
set fs=Server.CreateObject("Scripting.FileSystemObject")

if fs.folderExists("C:\inetpub\wwwroot\Development\ASP") = true then
    response.write("Pasta C:\inetpub\wwwroot\Development\ASP Existe.")
else
    response.write("pasta C:\inetpub\wwwroot\Development\ASP não existe.")
end if

set fs=nothing
%>

<br><br><br>
<h4>Ler um arquivo com FILESYSTEM</h4>

<%
set fs = server.CreateObject("Scripting.FIleSystemObject")
set arquivo = fs.OpenTextFile("C:\inetpub\wwwroot\Development\ASP\ArquivoFileSystems", 1)

response.write(arquivo.readAll)

arquivo.close

set arquivo = nothing
set fs = nothing
%>

<br><br><br>
<h4>Escrevendo dentro de um arquivo de texto</h4>
<p>Existem parametros para alterações nos arquivos com asp como:<br>
    set arquivo = fs.OpenTextFile("C:\inetpub\wwwroot\Development\ASP\ArquivoFileSystems", <b>1</b>) <br>
    Esse numero representa ação que será tomada sendo elas: <br>
    1: ler o arquivo <br>
    2: Substituir todo o conteúdo do arquivo <br>
    8:Adiciona o um texo escrito pelo usuario no final do arquivo
</p>

<%
set fs = server.CreateObject("Scripting.FIleSystemObject")
set arquivo = fs.OpenTextFile("C:\inetpub\wwwroot\Development\ASP\ArquivoFileSystems", 8)
arquivo.write("Como você está hoje? Texto adicionado")
<!-- response.write(arquivo.readAll) -->

arquivo.close

set arquivo = nothing

set arquivo = fs.OpenTextFile("C:\inetpub\wwwroot\Development\ASP\ArquivoFileSystems", 1)

response.write(arquivo.readAll)

set fs = nothing
%>

<br><br><br>
<h4>Obejto Folder</h4>
<p>O objeto folder é usado para obter informações sobre uma pasta especifica</p>

<%
set fs= server.CreateObject("Scripting.FileSystemObject")
set pasta = fs.GetFolder("C:\inetpub\wwwroot\Development\Python")
response.write("Pasta criada em: " & pasta.DateCreated)
set pasta = nothing
set fs = nothing
%>

<br><br><br>
<h4>Objeto Drive</h4>
</body>
<p>O objeto drive fornece informações sobre um disco do servidor</p>

<%
set fs = server.CreateObject("Scripting.FileSystemObject")
set disco = fs.GetDrive("C:")
response.write("Tamanho total de C: em bytes: " & disco.totalSize)
set disco = nothing
set fs = nothing
%>

<br><br><br>
<h4>Obter informações sobre um arquivo</h4>


<%
set fs = Server.CreateObject("Scripting.FileSystemObject")
caminho = server.mapPath("index.asp")
set arquivo = fs.GetFile(caminho)
response.write("Este arquivo foi criado em: " & arquivo.DateCreated)
set arquivo = nothing
set fs = nothing
%>

<br><br><br>
</html>
