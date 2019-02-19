from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .models import Turma


class CadastrarTurma(CreateView):
    model = Turma
    fields = ['periodo', 'quanttidade_alunos', 'turno', 'professores']