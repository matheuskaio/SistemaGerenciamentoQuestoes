from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Pessoa(models.Model):

    cpf = models.CharField(max_length=15, null=False)
    nome = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    data_nascimento = models.DateField(null=False)
    rua = models.CharField(max_length=30, null=True)
    bairro = models.CharField(max_length=30, null=True)
    cidade = models.CharField(max_length=40, null=True)
    estado_uf = models.CharField(max_length=2, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Aluno(Pessoa):

    def __str__(self):
        return "Aluno: " + self.nome


    def get_absolute_url(self):
        return reverse('page-home')