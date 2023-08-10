
var alturaTela = 0
var larguraTela = 0

//tamanho da janela
function ajustaTamanhoPalcoJogo(){
    alturaTela  = window.innerHeight
    larguraTela = window.innerWidth
    
    console.log(alturaTela, larguraTela)
}

ajustaTamanhoPalcoJogo()

function posicaoRandomica(){

    var posicaoX = Math.floor(Math.random() * larguraTela)
    var posicaoY = Math.floor(Math.random() * alturaTela) 

    console.log(posicaoX, posicaoY)

    //Criar o elemento html

    var mosquito = document.createElement("img")
    mosquito.src = 'imagens/mosquito.png'

    document.body.appendChild(mosquito)
}