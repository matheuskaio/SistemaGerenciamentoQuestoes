from django.db import models

# Create your models here.


class Instituicao(models.Model):
    # O CODIGO É A PROPRIA PK
    nome = models.CharField(max_length=100, null=False)
    cnpj = models.CharField(max_length=18, null=False)
    rua = models.CharField(max_length=30, null=False)
    bairro = models.CharField(max_length=30, null=False)
    cidade = models.CharField(max_length=40, null=False)
    estado_uf = models.CharField(max_length=2, null=False)

    def __str__(self):
        return "Instituição: " + self.nome
