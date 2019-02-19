from django.shortcuts import render
from django.views.generic import CreateView
from apps.professor.models import Professor


class CadastrarProfessor(CreateView):
    model = Professor
    fields = ['cpf', 'nome', 'data_nascimento', 'rua', 'bairro',
              'cidade', 'estado_uf']

