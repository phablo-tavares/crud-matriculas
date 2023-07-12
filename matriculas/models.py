from django.db import models

class Aluno(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=255)
	
	def __str__(self):
		return self.nome
	
	class Meta:
		db_table = 'alunos'



class Escola(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=255)
	tipo = models.CharField(max_length=255)

	def __str__(self):
		return self.nome
	
	class Meta:
		db_table = 'escolas'


class Matricula(models.Model):
    numero_de_matricula = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    class Meta:
        db_table = 'matriculas'

    def __str__(self):
        return str(self.numero_de_matricula)