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

//Mesma função de focusin porém com utilidade para formulários
//         $('.ev1').focus(function(){
//             ex.text($(this).attr('title'));
//         }).keyup(function(){
//             if($(this).val() == 'rhyan'){
//                 $('.ev2').focus();
//             }
//         });

// //Mesma função de focusout porém com utilidade para formulários
//         $('.ev1').blur(function(){
//             ex.text('Saída do campo: ' + $(this).attr('name'))
//         });

//Realiza a função toda vez que o campo selecionado muda o valor dentro dele
        $('.ev1').change(function(){
            ex.text('Campo alterado: ' + $(this).val())
        });

//Realizar a função do formulario
        $('.selecionar').click(function(){
            $('.ev3').select(); //Seleciona todo o texto dentro do campo marcado
            $('form').submit(function(){
                return false; //Bloqueia a função de submit do botão
            });
        });
    });