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
            border: 1px solid black; 
            width: 700px; 
            margin-top: 150px; 
            padding: 2rem; 
            border-radius: 1rem;

        }
/* 
        .btn-primary{
            background-color: green;
            border-color: green;
        }

        .btn-primary:hover{
            background-color: rgba(21, 221, 41, 0.818);
            border-color: green;
        }

        .btn-primary:{
            background-color: red;
        }

        .btn-primary:active{
            background-color: rgba(21, 221, 41, 0.818);
            border-color: green;
        } */

    </style>

</head>
<body>

    <div class="container">
        <h1>Login</h1>
        <br>

        <form>
            <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">E-mail</label>
            <input type="email" class="form-control" id="campo-email" name="campo-email" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text">Nunca compartilhe seu e-mail com ninguém.</div>
            </div>
            <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Senha</label>
            <input type="password" class="form-control" id="campo-senha" name="campo-senha">
            </div>
            <!-- <button type="submit" id="btn-login" name="btn-login" class="btn btn-primary">Entrar</button> -->
            <a href="http://localhost/development/ASP/vamove/crud/index_crud.asp"><button type="button" class="btn btn-primary">Login</button></a>

        </form>
    </div>


    

</body>
</html>