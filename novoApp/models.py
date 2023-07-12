from django.db import models
from matriculas.models import Matricula, Aluno, Escola

# Create your models here.
class Convenio(models.Model):
    id = models.AutoField(primary_key=True)
    matriculas = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    escolas = models.ForeignKey(Escola, on_delete=models.CASCADE)

    class Meta:
        db_table = 'convenios'
