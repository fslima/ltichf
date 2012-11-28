
function enviar_formulario(id){
	document.form_busca.action= "/exibir/funcionario/"+id+"/";
	document.form_busca.submit()
}

function proxima_pagina(tamanho_total_lista){
	if (tamanho_total_lista > parseInt(document.form_busca.fim.value)){
		document.form_busca.inicio.value= parseInt(document.form_busca.inicio.value)+7;
		document.form_busca.fim.value= parseInt(document.form_busca.fim.value)+7;
		document.form_busca.submit()
	}
}

function pagina_anterior(){
	if (parseInt(document.form_busca.inicio.value) > 0){
		document.form_busca.inicio.value= parseInt(document.form_busca.inicio.value)-7;
		document.form_busca.fim.value= parseInt(document.form_busca.fim.value)-7;
		document.form_busca.submit()
	}
}
