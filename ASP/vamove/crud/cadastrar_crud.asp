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
            <h1>Cadastrar Usuário</h1>
            <br>
            <form class="formulario">
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">E-mail</label>
                <input type="email" class="form-control" id="campo-email" name="campo-email" aria-describedby="emailHelp">

                <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Senha</label>
                <input type="password" class="form-control" id="campo-senha" name="campo-senha">
                </div>
                <button type="submit" id="btn-login" name="btn-login" class="btn btn-primary">Cadastrar</button>

            </form>

        </div>
    </div>


    

</body>
</html>