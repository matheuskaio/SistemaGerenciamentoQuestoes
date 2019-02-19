from django.urls import path

from apps.aluno.views import CadastrarAluno

urlpatterns = [
    path('new/', CadastrarAluno.as_view(), name="create-aluno"),

]
