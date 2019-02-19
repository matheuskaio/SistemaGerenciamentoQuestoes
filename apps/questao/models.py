from django.db import models

# Create your models here.

class Questao(models.Model):
    enunciado_questao = models.CharField(max_length=500, null=False)
    nivel = models.CharField(max_length=10, null=False)


class Alternativa(models.Model):
    enunciado_alternativa = models.CharField(max_length=500, null=False)
    alternativa_certa = models.BooleanField()
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)

    def criarAlternativa(self, pk_questao):
        pass