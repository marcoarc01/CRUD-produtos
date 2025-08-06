# CRUD de Produtos

Projeto prático desenvolvido para fins de aprendizado, utilizando Django

## Funcionalidades

- Sistema de autenticação de usuários (login e cadastro)
- Cada usuário pode:
  - Visualizar sua própria lista de produtos
  - Criar novos produtos
  - Editar produtos existentes
  - Excluir produtos

## Tecnologias Utilizadas

- Python
- Django
- HTML

## Detalhes do Projeto

- O sistema de login foi implementado utilizando o método `authenticate` do Django
- Os usuários são gerenciados a partir do modelo `User`, fornecido por `django.contrib.auth.models`
- Todas as operações de CRUD (Create, Read, Update, Delete) são associadas ao usuário autenticado
