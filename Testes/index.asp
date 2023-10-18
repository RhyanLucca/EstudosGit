<!--#include file="functions.asp"-->
<!-- #include file="connection.asp" -->

<%

call open_connection
Response.CharSet = "UTF-8"
%>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

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

        .full-right{
            justify-content: space-between;
        }

/* Start Nav Div */

        .nav{
            background-color: #000000;
            display: flex;
            height: 70px;
            color: #fff;
            list-style-type:none;
            min-width: 100%;
            position: fixed;
        }

        .nav a{
            color: #fff;
        }

        .nav-logo{
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 2rem;
            margin-left: 5px;
        }

        .nav-list{
            list-style-type:none;
            display: flex;
            align-items: center;
            margin-left: 20px;
            /* width: 100%; */
        }

        .nav-tab{
            margin-left: 1rem;
            padding: 1.5rem;
            font-size: 1.3rem;
        }

        .nav-tab:hover{
            background-color: #fff;
            color: #000;
            border-radius: 0.5;
        }

        hr{
            margin: 5px 0 5px 0px;
        }

        .body-area {
            padding: 10px;
        }


/* Start Filter Div */

        .filter-body{
            
            border: 1px solid black;
            padding: 10px;
            width: 80%;
            margin: 10px auto;
            margin-top: 100px;
            border-radius: 0.5rem;
            box-shadow: 3px 3px 3px black;
            justify-content: space-around;
            flex-wrap: wrap;
        }

        .submitFormFilter{
            display: flex;
        }

        .filter{
            margin: 0px 15px 0px 15px;
        }

        .filter-select{
            width: 200px;
        }

/* End Filter Div */

        .publications-container{
            display: flex;
            /* float: left; */
            flex-wrap: wrap;
            justify-content: space-around;
            /* align-items: left; */
        }

        .publication-body{
            cursor: pointer;
            min-width: 300px;
            width: 350px;
            max-width: 450px;
            margin: 1%;
            padding: 1%;
            min-height: 240px;
            max-height: 240px;
            border: 1px solid black;
            border-radius: 0.5rem;
            box-shadow: 3px 3px 3px black;
            
        }

        .publication-title{
            min-height: 30%;
            max-height: 30%;
            
            padding: 1%;
        }

        .publication-description{
            min-height: 45%;
            max-height: 45%;
            min-height: 110px;
            max-height: 110px;
            padding: 1%;
            align-items: center;
        }

        .publication-bonus{
            min-height: 5%;
            max-height: 5%;
            padding: 1%;
            display: flex;
            justify-content: space-between;
        }

    </style>

</head>
<body>
    
    <div class="nav">
        <div class="nav-logo">
            <a href="#" class="#"><span style="color: red;">RTS</span>YSTEMS</a>
        </div>
        <ul class="nav-list">
            <li><a href="#" class="nav-tab">Home</a></li>
            <li><a href="#" class="nav-tab">Contato</a></li>
            <li><a href="#" class="nav-tab">Sobre</a></li>
            <li><a href="#" class="nav-tab">Login</a></li>
        </ul>
    </div>

    <div class="body-area">
        
        <div class="filter-body">

            <form action="" class="submitFormFilter">
                
                <div class="filter">
                    <label for="">Cidade:</label>
                    <br>
                    <select name="" id="" class="filter-select">
                        <option value="">Todos</option>
                        <option value="">São Paulo</option>
                        <option value="">Osasco</option>
                        <option value="">Carapicuíba</option>
                    </select>
                </div>

                <div class="filter">
                    <label for="">Horário:</label>
                    <br>
                    <select name="" id="" class="filter-select">
                        <option value="">Todos</option>
                        <option value="">Manhã</option>
                        <option value="">Tarde</option>
                        <option value="">Noite</option>
                    </select>
                </div>
                
                <div class="filter">
                    <label for="">Valor R$:</label>
                    <br>
                    <input type="text" class="filter-select">
                </div>

                <div class="filter">
                    <label for="">Benefícios:</label>
                    <br>
                    <select name="" id="" class="filter-select">
                        <option value="">Refeição no local</option>
                        <option value="">Lanche</option>
                        <option value="">Fretado</option>
                    </select>
                </div>

            </form>

        </div>
        
        <h1 style="font-size: 3rem;">Eventos Disponíveis</h1>
        
        <hr> 

        <div class="publications-container">

            <% 

            Set rset1 = Server.CreateObject("ADODB.Recordset")

            rset1.open "SELECT * FROM tabeventos", conexao1

            'Set rset1 = conDB.execute(strSQL)

            Do Until rset1.EOF

            %>
            
            <div class='publication-body' data-id='<%=rset1("cadID")%>'>
                
                <div class="publication-title">
                    <h1><%=rset1("cadNome")%></h1>
                    <br>
                    <h4>18:00 às 02:00h</h4>
                </div>
                <hr>
                <div class="publication-description">
                    <p><%=rset1("cadDescricao")%></p>
                </div>
                <hr>
                <div class="publication-bonus">
                    <h4>R$: <%=rset1("cadPagamento")%></h4>
                    <h4 class="full-right">Número de vagas: <%=rset1("cadNumVagas")%></h4>
                </div>

            </div>

            <%
                rset1.MoveNext 
            Loop
            %>

        </div>

    </div>

</body>
</html>


<%

call end_connection

%>