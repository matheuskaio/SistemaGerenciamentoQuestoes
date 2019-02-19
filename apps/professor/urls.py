from django.urls import path

from apps.professor.views import CadastrarProfessor

urlpatterns = [
    path('new/', CadastrarProfessor.as_view(), name="create-professor"),

]
