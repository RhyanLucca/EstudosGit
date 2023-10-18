<%

Dim strConexaoDB, conexao1 

Sub open_connection()

    Set conexao1 = Server.CreateObject("ADODB.Connection")

    strConexaoDB = ("Driver={SQL Server Native Client 11.0};Server=FRANCO-0106;Uid=sa;Pwd=123456;Database=rtsystems")

    conexao1.open strConexaoDB
    
End Sub



Sub end_connection()

    conexao1.close

    Set conexao1 = Nothing

End Sub

%>