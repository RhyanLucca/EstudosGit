<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>

    <style>

        *{
            margin: 0;
            padding: 0;
            text-decoration: none; 
            font-family: sans-serif;
        }

        .debug{
            border: 1px solid red;
        }


        .login-frame{
            border: 1px solid grey; 
            border-radius: 0.5rem;
            width: 50%; 
            margin: 100px auto; 
            padding: 3%;
            height: 300px;
        }

        .input-div{
            margin: 2rem 0 2rem 0;
        }

        .label{
            font-size: larger;
        }

        .login-input{
            width: 100%;
            font-size: 1rem;
        }

    </style>

</head>
<body>
    
    <div class="login-frame">

        <form action="http://localhost/Development/Testes/index.asp#">

            <h1><span style="color: red;">RTS</span>YSTEMS</h1>

            <div class="input-div">
                <label class="label" for="emailInput">E-mail</label><br>
                <input class="login-input" type="text" name="emailInput" id="emailInput" placeholder="Insira seu E-mail">
            </div>
            <div class="input-div">
                <label class="label" for="pswdInput">Senha</label><br>
                <input class="login-input" type="password" name="pswdInput" id="pswdInput" placeholder="Insira sua Senha">
            </div>

            <input type="submit" value="Entrar">

        </form>
    </div>

</body>
</html>