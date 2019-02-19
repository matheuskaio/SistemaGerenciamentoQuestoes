from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from apps.aluno.models import Aluno


class CadastrarAluno(CreateView):
    model = Aluno
    fields = ['cpf', 'nome', 'email', 'data_nascimento', 'rua', 'bairro',
              'cidade', 'estado_uf']

    def form_valid(self, form):
        aluno = form.save(commit=False)
        username = aluno.email
        aluno.user = User.objects.create_user(username=username, password='ifrn2018')
        aluno.save()
        return super(CadastrarAluno, self).form_valid(form)