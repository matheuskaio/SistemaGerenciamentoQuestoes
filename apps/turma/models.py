from django.db import models

# Create your models here.
from apps.professor.models import Professor


class Turma(models.Model):
    # O CODIGO É A PROPRIA PK
    periodo = models.CharField(max_length=1, null=False)
    quanttidade_alunos = models.CharField(max_length=3, null=False)
    turno = models.CharField(max_length=20, null=False)
    professores = models.ManyToManyField(Professor, blank=False)
