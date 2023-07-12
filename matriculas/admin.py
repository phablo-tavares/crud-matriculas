from django.contrib import admin
from .models import Aluno,Escola,Matricula

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Escola)
admin.site.register(Matricula)