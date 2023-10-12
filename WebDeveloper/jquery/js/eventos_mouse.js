$(function(){

//Evento disparado com Click
        var ex = $('.ex1');

    $('.ev1').click(function(){ //Comando executado quando o elemento é clicado
        $(this).css({"background":"#ccc"});
        ex.text("Você clicou!"); //Comando que altera textos
    });

//Evento disparado com doubleClick
    $('.ev2').dblclick(function(){
        $(this).css({"background":"#ccc"});
        ex.text("Você deu dois cliques!"); //Comando que altera textos
    })

//Evento disparado em foco ou desfoque do elemento
    $('.ev3').focusin(function(){
        $(this).css({"background":"#ccc"});
        ex.text("Você deu foco no input!");
    }).focusout(function(){
        $(this).css({"background":"#000"});
        ex.text("Você tirou o foco do input!");
    });

//Evento dispadaro no HOVER
    $('.ev4').hover(function(){
        $(this).css({"background":"#ccc"});
        ex.text("Você Passou o mouse!");
    });

//Evento disparado ao apertar ou soltar o botão do mouse
    $('.ev5').mousedown(function(){
        $(this).css({"background":"#ccc"});
        ex.text("Você Apertou o Botão do Mouse!");
    }).mouseup(function(){
        $(this).css({"background":"#000"});
        ex.text("Você Soltou o Botão do Mouse!");
    });

//Evento disparado ao entrar e sair do botão 
//Erro nativo: Os filhos do elemento não executam a função do elemento pai e isso pode causar erros
    var a = 0;
    $('.ev6').mouseenter(function(){
        a += 1;
        ex.text("Entradas do mouse: " + a)
    }).mouseout(function(){
        ex.text("Saídas do mouse");
    })

//Evento disparado com mouseOver
//Erro nativo: executa mais a function tanto para o elemento pai quanto para os elementos filhos, o que pode ser um problema
    var b = 0;
    $('.ev7').mouseover(function(){
        b +=1
        ex.text("Mouse Over: " + b)
    }).mouseleave(function(){
        ex.text("Mouse Leave")
    });

//Evento disparado ao mover o mouse dentro de um elemento
    $('.ev8').mousemove(function(move){
        var localX = move.pageX;
        var localY = move.pageY;

        ex.text("Movimento X: " +localX+ "Movimento Y: " + localY)
    });

});