from django.shortcuts import render,redirect
from .models import Aluno, Escola, Matricula
from .util.util import paginaDeMatriculaRenderizada,paginaDeAlunosRenderizada,paginaDeEscolasRenderizada

# Create your views here.
def renderizarPagina(request):
    alunos = Aluno.objects.all()
    escolas = Escola.objects.all()
    matriculas = Matricula.objects.all()
    pagina = render(request,'index.html',{"alunos":alunos, "escolas":escolas ,"matriculas":matriculas})
    return pagina


def inserirAluno(request):
    nomeDoAluno = request.POST['campo_nome_do_aluno']
    Aluno.objects.create(nome = nomeDoAluno)
    return redirect('/')

def editarAluno(request,id):
    aluno = Aluno.objects.filter(id=id).values()
    pagina = render(request,'editarAluno.html',{"aluno" : aluno[0]})
    return pagina

def salvarEdicaoAluno(request):
    id = request.POST['id']
    nome = request.POST['campo_nome_do_aluno']

    cadastro = Aluno.objects.get(id = id)
    cadastro.nome = nome
    cadastro.save()

    return redirect('/')

def excluirAluno(request,id):
    cadastro = Aluno.objects.get(id = id)
    cadastro.delete()
    return redirect('/')


def inserirEscola(request):
    nomeDaEscola = request.POST['campo_nome_da_escola']
    tipoDaEscola = request.POST['campo_tipo_da_escola']
    Escola.objects.create(nome = nomeDaEscola, tipo = tipoDaEscola)
    return redirect('/')

def excluirEscola(request,id):
    cadastro = Escola.objects.get(id = id)
    cadastro.delete()
    return redirect('/')

def editarEscola(request,id):
    escola = Escola.objects.filter(id=id)
    pagina = render(request,'editarEscola.html',{"escola":escola[0]})
    return pagina

def salvarEdicaoEscola(request):
    id = request.POST['id']
    nome = request.POST['campo_nome_da_escola']
    tipo = request.POST['campo_tipo_da_escola']

    cadastro = Escola.objects.get(id = id)
    cadastro.nome = nome
    cadastro.tipo = tipo
    cadastro.save()

    return redirect('/')


def inserirMatricula(request):
    idDoAluno = int(request.POST['aluno_id'])
    idDaEscola = int(request.POST['escola_id'])

    Matricula.objects.create(aluno_id = idDoAluno, escola_id = idDaEscola)

    return redirect('/')

def editarMatricula(request,numero_de_matricula):
    matricula = Matricula.objects.filter(numero_de_matricula = numero_de_matricula).prefetch_related('aluno_id').prefetch_related('escola_id').values()
    alunos = Aluno.objects.all()
    escolas = Escola.objects.all()
    pagina = render(request,'editarMatricula.html',{"matricula":matricula[0],"alunos":alunos, "escolas":escolas})
    return pagina

def editarMatriculaAjax(request,numero_de_matricula):
    matricula = Matricula.objects.filter(numero_de_matricula = numero_de_matricula).prefetch_related('aluno_id').prefetch_related('escola_id').values()
    alunos = Aluno.objects.all()
    escolas = Escola.objects.all()
    pagina = render(request,'ajax/editarMatriculaAjax.html',{"matricula":matricula[0],"alunos":alunos, "escolas":escolas})
    return pagina

def salvarEdicaoMatricula(request):
    numeroDeMatricula = int(request.POST['numero_de_matricula'])
    matricula = Matricula.objects.get(numero_de_matricula = numeroDeMatricula)

    idDoAluno = int(request.POST['aluno_id'])
    aluno = Aluno.objects.get(id = idDoAluno)

    idDaEscola = int(request.POST['escola_id'])
    escola = Escola.objects.get(id = idDaEscola)

    matricula.aluno = aluno
    matricula.escola = escola
    matricula.save()

    return redirect('/')

def salvarEdicaoMatriculaAjax(request):
    numeroDeMatricula = int(request.POST['numeroDeMatricula'])
    matricula = Matricula.objects.get(numero_de_matricula = numeroDeMatricula)

    idAluno = int(request.POST['idAluno'])
    aluno = Aluno.objects.get(id = idAluno)

    idEscola = int(request.POST['idEscola'])
    escola = Escola.objects.get(id = idEscola)

    matricula.aluno = aluno
    matricula.escola = escola
    matricula.save()

    return paginaDeMatriculaRenderizada(request)

def excluirMatricula(request,numero_de_matricula):
    matricula = Matricula.objects.get(numero_de_matricula = numero_de_matricula)
    matricula.delete()
    return redirect('/')



def inserirAlunoAjax(request):
    nomeDoAluno = request.POST['campo_nome_do_aluno']
    Aluno.objects.create(nome = nomeDoAluno)
    return paginaDeAlunosRenderizada(request)

def inserirEscolaAjax(request):
    nomeDaEscola = request.POST['campo_nome_da_escola']
    tipoDaEscola = request.POST['campo_tipo_da_escola']
    Escola.objects.create(nome=nomeDaEscola,tipo=tipoDaEscola)
    return paginaDeEscolasRenderizada(request)

def inserirMatriculaAjax(request):
    idDoAluno = int(request.POST['aluno'])
    idDaEscola = int(request.POST['escola'])
    Matricula.objects.create(aluno_id = idDoAluno, escola_id = idDaEscola)
    return paginaDeMatriculaRenderizada(request)


def excluirAlunoAjax(request,id):
    aluno = Aluno.objects.get(id = id)
    aluno.delete()
    return paginaDeAlunosRenderizada(request)

def excluirEscolaAjax(request,id):
    escola = Escola.objects.get(id = id)
    escola.delete()
    return paginaDeEscolasRenderizada(request)

def excluirMatriculaAjax(request,numero_de_matricula):
    matricula = Matricula.objects.get(numero_de_matricula = numero_de_matricula)
    matricula.delete()
    return paginaDeMatriculaRenderizada(request)


def editarAlunoAjax(request,id):
    idAluno = int(id)
    novoNomeDoAluno = request.POST['novoNomeAluno']
    aluno = Aluno.objects.get(id = idAluno)
    aluno.nome = novoNomeDoAluno
    aluno.save()
    return paginaDeAlunosRenderizada(request)

def editarEscolaAjax(request,id):
    idEscola = int(id)
    novoNomeEscola = request.POST['novoNomeEscola']
    novoTipoDaEscola = request.POST['novoTipoDaEscola']
    escola = Escola.objects.get(id = idEscola)
    escola.nome = novoNomeEscola
    escola.tipo = novoTipoDaEscola
    escola.save()
    return paginaDeEscolasRenderizada(request)

