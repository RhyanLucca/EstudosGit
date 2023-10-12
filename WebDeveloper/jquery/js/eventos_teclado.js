$(function(){

//Each simboliza que para CADA ELEMENTO QUE TIVER ESSA CLASSE ele executará uma function
    $('.place').each(function(){
        var place = $(this).attr('title'); //Recupera o valor do atributo title
        var input = $(this); //Pega o inut que estiver com a classe place

        input
            .val(place) //Define o valor da variavel place para o input
            .css('color','#ccc')
            .focusin(function(){
                input.css('color','#000') //Altera o valor de volta para preto
                if(input.val() == place){
                    input.val('') //Zera o valor do input
                }
            }).focusout(function(){
                if(input.val() == ''){
                    input.css('color','#ccc');
                    input.val(place);
                }
            });
    });

    var ex = $('.ex1');
//Executa a funtion no momento que uma tecla é pressionada, com delay de 1 tecla (Shift Não Funciona)
    // $('.key').keypress(function(){
    //      ex.text($(this).val);
    // });
//Executa a funtion no momento que uma tecla é pressionada, com delay de 1 tecla (Shift Funciona)
    // $('.key').keydown(function(){
    //     ex.text($(this).val())
    // });

//Executa a funtion em tempo real, sem delay
    $('.key').keyup(function(){
        ex.text($(this).val())
    });
});