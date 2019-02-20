from django.db import models
from django.urls import reverse

from apps.aluno import models


class Professor(models.Pessoa):

    def __str__(self):
        return "Professor: " + self.nome


    def get_absolute_url(self):
        return reverse('page-home')