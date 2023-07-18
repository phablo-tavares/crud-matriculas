from django.shortcuts import render,redirect
from ..models import Aluno, Escola, Matricula


def paginaDeAlunosRenderizada(request):
    alunos = Aluno.objects.all()
    return render(request,'ajax/listaDeAlunos.html',{'alunos':alunos})

def paginaDeEscolasRenderizada(request):
    escolas = Escola.objects.all()
    return render(request,'ajax/listaDeEscolas.html',{'escolas':escolas})

def paginaDeMatriculaRenderizada(request):
    matriculas = Matricula.objects.all()
    return render(request,'ajax/listaDeMatriculas.html',{'matriculas':matriculas})