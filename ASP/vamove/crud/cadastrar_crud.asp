<!--#include file="includes/conexao.asp"-->

<%

<!--' GET ID -->'
id = request.QueryString("id")

'<!-- SE O ID FOR NULLO -->'
if trim(id) = "" or isnull(id) then
    id = 0
end if

'<!-- SE O ID NÃO FOR UMA VALOR NUMÉRICO -->'
if not isnumeric(id) then
    response.write("Parametro ID inválido")
    response.end
end if

''<!-- SE O ID FOR DIFERENTE DE 0: EDIÇÃO -->'''
if cint(id) <> 0 then '<!--Se o ID FOR DIFERENTE DE 0-->'

    strSQL = "SELECT * FROM users WHERE id = " & id

    set objectRset = conDB.execute(strSQL)

    if not objectRset.EOF then '<!--Se encontrar um valor na lista-->'
        id = objectRset("id")
        name = objectRset("nome")
        email = objectRset("email")
    end if

    set objectRset = nothing


end if
%>

 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="login.css" rel="Stylesheet" type="text/css" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>

    <style>

        *, #emailHelp{
            color: black;
        }

        .form-control{
            border-color: black;
        }

        .form-control:focus {
            border-color: black;
            box-shadow: none;
        }

        .container{
            width: 500px; 
            margin-top: 150px; 
            padding: 2rem; 
            border-radius: 1rem;
        }

        .div_formulario{
            border: 1px solid black;
            width: 500px;
            margin-left: auto;
            margin-right: auto;
        /* width: 100px;   */
            padding: 1rem; 
            border-radius: 1rem;
        }

    </style>

</head>
<body>

    <!--#include file="nav_crud.asp"-->

    <div class="container">

        <div class="div_formulario">
            <h1>Usuários</h1>
            <form class="formulario" method="post" action="cad_usuario.asp">

                <div class="mb-3">
                <label class="form-label">Usuario</label>
                <input type="text" class="form-control" id="inpt-user" name="name" value='<%=name%>'>

                <br>

                <div class="mb-3">
                <label class="form-label">E-mail</label>
                <input type="email" class="form-control" id="inpt-email" name="email" aria-describedby="emailHelp" value='<%=email%>'>
                <input type="hidden" name="id" id="id" value='<%=id%>'>
                </div>
                <button type="submit" id="btn-login" name="btn-login" class="btn btn-primary">Cadastrar</button>

            </form>

        </div>
    </div>


    

</body>
</html>