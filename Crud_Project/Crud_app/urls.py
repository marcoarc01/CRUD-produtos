from django.urls import path
from .views import lista_produto, criar_produto, excluir_produto, atualizar_produto, cadastro, login, sair_conta

urlpatterns = [
    path('lista/', lista_produto, name='lista_produto'),
    path('criar/', criar_produto, name='criar_produto'),
    path('excluir/<int:pk>/', excluir_produto, name='excluir_produto'),
    path('atualizar/<int:pk>/', atualizar_produto, name='atualizar_produto'),
    path('', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('', sair_conta, name='sair'),
]