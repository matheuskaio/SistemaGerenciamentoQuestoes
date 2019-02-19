from django.urls import path

from apps.questao.views import CadastrarQuestao

urlpatterns = [
    path('new/', CadastrarQuestao.as_view(), name="create-questao"),

]