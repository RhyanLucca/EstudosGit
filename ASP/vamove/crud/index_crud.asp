<!--#include virtual=/includes/conexao.asp-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD Cadastros</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <link rel="stylesheet" href="../style.css">

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

        <table class="table">
            <thead>
                <th>ID</th>
                <th>Nome</th>
                <th>E-mail</th>
                <th>Status</th>
                <th>Permissões</th>
                <th>Ação</th>
            </thead>
            <tr class="table_crud_row">
                <td>1</td>
                <td>Rhyan</td>
                <td>brhyanlucca@gmail.com</td>
                <td>Ativo</td>
                <td>Administrador</td>
                <td>
                    <button type="button" class="btn btn-primary" id="btn-editar" name="btn-editar">Editar</button>  
                    <button type="button" class="btn btn-primary" id="btn-excluir" name="btn-excluir">Excluir</button>
                </td>
            </tr>
          </table>

    </div>
</body>
</html>