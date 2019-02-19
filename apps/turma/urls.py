from django.urls import path, include
from .views import CadastrarTurma
urlpatterns = [
    path('new/', CadastrarTurma.as_view(), name="create-turma"),

]
