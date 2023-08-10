
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

    var posicaoX = Math.floor(Math.random() * larguraTela) -55
    var posicaoY = Math.floor(Math.random() * alturaTela) -55

    posicaoX = posicaoX < 0 ? 0 : posicaoX
    posicaoY = posicaoY < 0 ? 0 : posicaoY

    console.log(posicaoX, posicaoY)

    //Criar o elemento html

    var mosquito = document.createElement("img")
    mosquito.src = 'imagens/mosquito.png'
    mosquito.className ="mosquito1"
    mosquito.style.left = posicaoX + "px"
    mosquito.style.top = posicaoY + "px"
    mosquito.style.position = "absolute"


    document.body.appendChild(mosquito)
}