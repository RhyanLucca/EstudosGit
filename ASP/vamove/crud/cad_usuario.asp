<!--#include file="includes/conexao.asp"-->

<%
id =  replace(Request.Form("id"), "'", "")
name = replace(Request.Form("name"), "'", "")
email = replace(Request.Form("email"), "'", "")


if trim(id) = "" or isnull(id) or trim(id) = "0" then

    id = 0

end if


if cint(id) <> 0 then

    strQuery = "UPDATE users SET nome= '"&name&"', email= '"&email&"' WHERE id = "& id

    conDB.execute(strQuery)

    response.redirect "index_crud.asp"
    response.end

else

    strQuery = "INSERT INTO users (nome, email) VALUES ('"& name &"', '" & email & "')"

    conDB.execute(strQuery)

    response.redirect "index_crud.asp"
    response.end

end if


'response.write(strQuery & "<br>")'
'response.write(name)'
'response.write("teste")'
'response.write(email)'
%>