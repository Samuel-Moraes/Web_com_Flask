function mostrarUmNoConsole() {
  console.log('Samuel Moraes')
  alert('Error')
}

function comparador(event){
  event.preventDefault();
  var nome = document.getElementById('id_nome_professor').value;
  if(nome === 'a'){
    alert('a')
  }

  
}