from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView
from apps.professor.models import Professor


class CadastrarProfessor(CreateView):
    model = Professor
    fields = ['cpf', 'nome', 'email', 'data_nascimento', 'rua', 'bairro',
              'cidade', 'estado_uf']

    def form_valid(self, form):
        professor = form.save(commit=False)
        username = professor.email
        professor.user = User.objects.create_user(username=username, password='ifrn2018')
        professor.save()
        return super(CadastrarProfessor, self).form_valid(form)