<!--#include file="includes/conexao.asp"-->
<%

id = request.QueryString("id")

if trim(id) = "" or isnull(id) or trim(id)= "0" then
    response.write "<script>alert('Id não informado'); document.location = 'index_crud.asp';</script>"
    response.end
end if

strSQL = "delete from users where id = " & id

conDB.execute(strSQL)

response.write "<script>alert('Registro excluido'); document.location = 'index_crud.asp';</script>"
response.redirect "index_crud.asp"
response.end


response.write(strSQL)
%>