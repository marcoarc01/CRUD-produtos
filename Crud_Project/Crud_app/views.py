from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Produto
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_diretorio
from django.contrib.auth import logout



# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username, email=email).first()
        
        if user:
            return HttpResponse('usuario ja cadastrado')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        
        user.save()
        
        return render(request, 'login.html')
    

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(request, username=username, password = senha)
        
        if user is not None:
            login_diretorio(request, user)
            return redirect(lista_produto)
        else:
            return HttpResponse('usuario ou senha invalidos')


def sair_conta(request):
    logout(request)
    return render(request, 'login.html')

def lista_produto(request):
    if request.user.is_authenticated:
        produtos = Produto.objects.filter(user = request.user)
        return render(request, 'list.html', {'produtos': produtos})
    
    return HttpResponse('voce nao esta logado')

def criar_produto(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nome = request.POST['nome']
            price = request.POST['price']
            descricao = request.POST['descricao']
            Produto.objects.create(nome = nome, price = price, descricao=descricao, user=request.user)
        return render (request, 'criar.html')

def excluir_produto(request, pk):
    if request.user.is_authenticated:  
        produto = get_object_or_404(Produto, pk=pk)
        if produto.user != request.user:
            return HttpResponse('voce nao possui esse produto')
        
        produto.delete()
        
        return redirect(lista_produto)
    return HttpResponse('voce nao esta logado')

        
def atualizar_produto(request, pk):
    if request.user.is_authenticated:  

        produto = get_object_or_404(Produto, pk=pk)
        
        if produto.user != request.user:
            return HttpResponse('voce nao possui esse produto')
        
        if request.method == 'POST':

            produto.nome = request.POST['nome']
            produto.price = request.POST['price']
            produto.descricao = request.POST['descricao']
            produto.save()
            return redirect(lista_produto)
    
        return render(request, 'atualizar.html')