from django.urls import path
from .views import lista_produto, criar_produto, excluir_produto, atualizar_produto

urlpatterns = [
    path('', lista_produto, name='lista_produto'),
    path('criar/', criar_produto, name='criar_produto'),
    path('excluir/<int:pk>/', excluir_produto, name='excluir_produto'),
    path('atualizar/<int:pk>/', atualizar_produto, name='atualizar_produto'),
]