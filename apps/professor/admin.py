from django.contrib import admin

# Register your models here.
from apps.professor.models import Professor

admin.site.register(Professor)