from django.urls import path, include
from .views import renderizarPagina,inserirAluno,editarAluno,salvarEdicaoAluno,excluirAluno,inserirEscola,editarEscola,salvarEdicaoEscola,excluirEscola,excluirMatricula,inserirMatricula,editarMatricula,salvarEdicaoMatricula,inserirAlunoAjax,inserirEscolaAjax,inserirMatriculaAjax,excluirAlunoAjax,excluirEscolaAjax,excluirMatriculaAjax,editarAlunoAjax,editarEscolaAjax,editarMatriculaAjax,salvarEdicaoMatriculaAjax

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
    path('excluir-matricula/<numero_de_matricula>',excluirMatricula),


    #AJAX
    path('inserir-aluno-ajax',inserirAlunoAjax),
    path('inserir-escola-ajax',inserirEscolaAjax),
    path('inserir-matricula-ajax',inserirMatriculaAjax),

    path('excluir-aluno-ajax/<id>',excluirAlunoAjax),
    path('excluir-escola-ajax/<id>',excluirEscolaAjax),
    path('excluir-matricula-ajax/<numero_de_matricula>',excluirMatriculaAjax),

    path('editar-aluno-ajax/<id>',editarAlunoAjax),
    path('editar-escola-ajax/<id>',editarEscolaAjax),
    path('editar-matricula-ajax/<numero_de_matricula>',editarMatriculaAjax),
    path('salvar-edicao-matricula-ajax',salvarEdicaoMatriculaAjax),

]
