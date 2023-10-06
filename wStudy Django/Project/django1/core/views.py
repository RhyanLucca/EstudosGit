from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Produto

# Create your views here.

def index(request):
    #print(dir(request))
    #print(f"Método: {request.method}")
    #print(f"Headers: {request.headers}")
    #print(f"User Agent: {request.headers['User-Agent']}")
    #print(f"User: {request.user}")
    #print(dir(request.user))
    #print(f"User: {request.user.username}")
    #print(f"User: {request.user.email}")
    # print(dir(request.user))
    # print(request.user)

    if str(request.user) == "AnonymousUser":
        teste = "Usuário não logado"
    else:
        teste = "Usuário Logado"

    produtos = Produto.objects.all()

    context = {
        'curso' : 'Programação web com Django Framework',
        'outros' : 'Django é massa!',
        'logado' : teste,
        'produtos' : produtos
    }

    return render(request, 'index.html', context,)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        "produto": prod
    }
    return render(request, "produto.html", context)