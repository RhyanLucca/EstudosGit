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
    h1{
        align-self: center;
    }

    .btn-cadastrar{
        margin-left: auto;
        margin-right: auto;
    }

    .table_crud{
        border: 1px solid black;
        margin-left: auto;
        margin-right: auto;
    }

    .table_crud td, .table_crud tr, .table_crud th{
        border: 1px solid black;
        padding: 10px 30px 10px 30px;
        text-align: center;
    }
    </style>

</head>
<body>
    
    <!--#include file="nav_crud.asp"-->

      <br>
      <h1>Cadastros</h1>
      <br><br>

    <a href="cadastrar_crud.asp"><input id="btn-cadastrar" class="btn-cadastrar" type="submit" value="Cadastrar" action="cadastrar_crud.asp"></a>

    <div class="table_div">
        
        <table class="table_crud">

            <thead>
                <th>ID</th>
                <th>Nome</th>
                <th>E-mail</th>
                <th>Ação</th>
            </thead>
            <tr class="table_crud_row">
                <td>1</td>
                <td>Rhyan</td>
                <td>brhyanlucca@gmail.com</td>
                <td><a href="edita_crud.asp">Editar</a>  <a href="">Excluir</a></td>
            </tr>

        </table>
    </div>
</body>
</html>