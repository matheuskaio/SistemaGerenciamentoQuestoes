from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from apps.questao.models import Questao, Alternativa


class CadastrarQuestao(CreateView):
    model = Questao
    fields = ['enunciado_questao', 'nivel']

    def form_valid(self, form):
        questao = form.save(commit=False)
        codigo = questao.pk
        Alternativa.criarAlternativa()