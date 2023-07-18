function adicionarAlunoViaAjax(url,token) {
  let nomeAluno = $("#campo_nome_do_aluno").val();

  $.ajax({
    url: url,
    type: "post",
    data: { 'campo_nome_do_aluno': nomeAluno },
    headers: { "X-CSRFToken": token },
    success: function (data) {
      $("#lista_de_alunos").html(data);
    },
  });
}
function adicionarEscolaViaAjax(url,token){
  let nomeEscola = $("#campo_nome_da_escola").val()
  let tipoEscola = $("#campo_tipo_da_escola").val()

  $.ajax({
    url: url,
    type:"post",
    data:{
      'campo_nome_da_escola': nomeEscola,
      'campo_tipo_da_escola': tipoEscola,
    },
    headers: { "X-CSRFToken": token },
    success: function (data) {
      $("#lista_de_escolas").html(data);
    },
  })
}
function adicionarMatriculaViaAjax(url,token){
  let idAluno = $("#aluno").val()
  let idEscola= $("#escola").val()

  $.ajax({
    url: url,
    type:"post",
    data:{
      'aluno': idAluno,
      'escola': idEscola,
    },
    headers: { "X-CSRFToken": token },
    success: function (data) {
      $("#lista_de_matriculas").html(data);
    },
  })
}


function excluirAlunoViaAjax(url,token,id){
  let idAluno = Number(id);

  $.ajax({
    url: url,
    type:"delete",
    data:{
      'idAluno': idAluno,
    },
    headers: { "X-CSRFToken": token },
    success: function (data) { //ver se tem como passar algo mais no data pra renderizar a lista de matriculas novamente quando excluir aluno ou escola
      $("#lista_de_alunos").html(data);
    },
  })
}
function excluirEscolaViaAjax(url,token,id){
  let idEscola = Number(id);

  $.ajax({
    url: url,
    type:"delete",
    data:{
      'idEscola': idEscola,
    },
    headers: { "X-CSRFToken": token },
    success: function (data) {
      $("#lista_de_escolas").html(data);
    },
  })
}
function excluirMatriculaAjax(url,token,id){
  let numeroDeMatricula = Number(id);

  $.ajax({
    url: url,
    type:"delete",
    data:{
      'numeroDeMatricula': numeroDeMatricula,
    },
    headers: { "X-CSRFToken": token },
    success: function (data) {
      $("#lista_de_matriculas").html(data);
    },
  })
}

function editarAlunoViaAjax(url,token,id){
  let idAluno = Number(id);
  let novoNomeAluno = window.prompt("Insira o novo nome do Aluno");
  $.ajax({
    url: url,
    type:"post",
    data:{
      'idAluno': idAluno,
      'novoNomeAluno':novoNomeAluno,
    },
    headers: { "X-CSRFToken": token },
    success: function (data) { 
      $("#lista_de_alunos").html(data);
    },
  })
}
function editarEscolaViaAjax(url,token,id){
  let idEscola = Number(id);
  let novoNomeEscola = window.prompt("Insira o novo nome da Escola");
  let novoTipoDaEscola = window.prompt("Insira o novo tipo da Escola");
  $.ajax({
    url: url,
    type:"post",
    data:{
      'idEscola': idEscola,
      'novoNomeEscola':novoNomeEscola,
      'novoTipoDaEscola':novoTipoDaEscola,
    },
    headers: { "X-CSRFToken": token },
    success: function (data) { 
      $("#lista_de_escolas").html(data);
    },
  })
}
function editarMatriculaViaAjax(url,token,id){
  let numeroDeMatricula = Number(id);

  $.ajax({
    url: url,
    type:"post",
    data:{
      'numeroDeMatricula': numeroDeMatricula,
    },
    headers: { "X-CSRFToken": token },
    success: function (data) { 
      $("#edicao_matricula").html(data);
    },
  })
}
function salvarEdicaoMatriculaViaAjax(url,token,id){
  let numeroDeMatricula = Number(id);
  let idAluno = $("#alunoEditado").val()
  let idEscola= $("#escolaEditado").val()

  $.ajax({
    url: url,
    type:"post",
    data:{
      'numeroDeMatricula': numeroDeMatricula,
      'idAluno': idAluno,
      'idEscola': idEscola,
    },
    headers: { "X-CSRFToken": token },
    success: function (data) { 
      $("#lista_de_matriculas").html(data);
      $("#edicao_matricula").html("<div></div>");
    },
  })
}