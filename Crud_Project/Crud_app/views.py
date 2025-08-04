from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
# Create your views here.

def lista_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'list.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        price = request.POST['price']
        descricao = request.POST['descricao']
        Produto.objects.create(nome = nome, price = price, descricao=descricao)
    return render (request, 'criar.html')

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    produto.delete()
        
    return redirect(lista_produto)

        
