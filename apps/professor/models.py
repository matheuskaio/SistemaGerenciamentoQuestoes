from django.db import models

from apps.aluno import models


class Professor(models.Pessoa):

    def __str__(self):
        return "Professor: " + self.nome