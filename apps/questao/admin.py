from django.contrib import admin

# Register your models here.
from apps.questao.models import Questao, Alternativa

admin.site.register(Questao)
admin.site.register(Alternativa)