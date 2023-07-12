from django.urls import path, include
from .views import renderizarPagina,inserirAluno,editarAluno,salvarEdicaoAluno,excluirAluno,inserirEscola,editarEscola,salvarEdicaoEscola,excluirEscola,excluirMatricula,inserirMatricula,editarMatricula,salvarEdicaoMatricula

urlpatterns = [
    path('',renderizarPagina),

    path('inserir-aluno',inserirAluno),
    path('editar-aluno/<id>',editarAluno),
    path('salvar-edicao-aluno',salvarEdicaoAluno),
    path('excluir-aluno/<id>',excluirAluno),

    path('inserir-escola',inserirEscola),
    path('editar-escola/<id>',editarEscola),
    path('salvar-edicao-escola',salvarEdicaoEscola),
    path('excluir-escola/<id>',excluirEscola),

    path('inserir-matricula',inserirMatricula),
    path('editar-matricula/<numero_de_matricula>',editarMatricula),
    path('salvar-edicao-matricula',salvarEdicaoMatricula),
    path('excluir-matricula/<numero_de_matricula>',excluirMatricula)

]
