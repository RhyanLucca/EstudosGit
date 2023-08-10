<!--#include file="includes/conexao.asp"-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD Cadastros</title>
    <link rel="stylesheet" href="includes/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">

    <style>

.tittle{
    text-align: center;
}

.container{

    /* width: 100px;   */
    padding: 1rem; 
    border-radius: 1rem;
}

table tr, td{
    border: 1px solid black; 
    width: 700px;  
    padding: 2rem; 
    border-radius: 1rem;
}

.btn-cadastrar{
    align-items: center;
    margin-left: auto;
    margin-right: auto;
}

    </style>

</head>
<body>
    
    <!--#include file="nav_crud.asp"-->

    <br>
        <div class="tittle">
            <h1>Cadastros</h1>
        </div>
    <br>

    <!-- <a href="cadastrar_crud.asp"><input id="btn-cadastrar" class="btn-cadastrar" type="submit" value="Cadastrar" action="cadastrar_crud.asp"></a> -->

    <div class="container">
        
        <a href="cadastrar_crud.asp"><button type="button" class="btn btn-primary">Cadastrar</button></a>

        <br><br>

        <!-- MODAL -->

        <div class="modal" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">Modal title</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">
                  <p>Modal body text goes here.</p>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-primary">EXCLUIR</button>
                  <button type="button" class="btn btn-secondary" data-dismiss="modal">FECHAR</button>
                </div>
              </div>
            </div>
          </div>

          <!-- FIM DO MODAL -->

        <table class="table table-striped">
            <thead>
                <th>ID</th>
                <th>Nome</th>
                <th>E-mail</th>

                <th>Ação</th>
            </thead>
            <tbody>
            <%
            strSQL = "SELECT * FROM users ORDER BY id DESC ;"
    
            set objectRset = conDB.execute(strSQL)
    
            do while not objectRset.EOF
    
            %>

            <tr class="table_crud_row">
                <td><%= objectRset("id")%></td>
                <td><%= objectRset("nome")%></td>
                <td><%= objectRset("email")%></td>
                <td>
                    <a href='cadastrar_crud.asp?id=<%=objectRset("id")%>'><button type="button" class="btn btn-primary" id="btn-editar" name="btn-editar">Editar</button></a>
                    <a href='exc_usuario.asp?id=<%=objectRset("id")%>'><button type="button" class="btn btn-primary" id="btn-excluir" name="btn-excluir">Excluir</button></a>
                </td>
            </tr>



            <%
            objectRset.MoveNext
            loop

            set objectRset = Nothing
            %>
            </tbody>
          </table>

    </div>
</body>
</html>