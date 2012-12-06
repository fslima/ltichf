# -*- coding:utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from models import *
from django.template import RequestContext
from forms import *

def inicio(request):
	return HttpResponseRedirect("/exibir/funcionario/0")

def exibir(request, tpObjeto, idObjeto):
    if str(tpObjeto) == 'funcionario':
	form_busca = Form_Busca_Funcionario()
        titulo = 'Funcionário'
        testa_objeto = Funcionario.objects.filter(pk = idObjeto)
	inicio = 0
	fim = 7
	if len(testa_objeto) > 0:
		if len(Servidor.objects.filter(pk = idObjeto)) > 0:
			objeto = Servidor.objects.get(pk = idObjeto)
			funcoes = objeto.funcoes.all()
		else:
			objeto = Contratado.objects.get(pk = idObjeto)
        	form = Form_Adiciona_Servidor(instance = objeto)
    if request.method == 'POST': 
	form_busca = Form_Busca_Funcionario(request.POST)
        if form_busca.is_valid():
            inicio = int(request.POST['inicio'])
            fim = int(request.POST['fim'])
            nome_form = form_busca.cleaned_data['nome_funcionario']
            lista = Funcionario.objects.filter(nome_funcionario__icontains = form_busca.cleaned_data['nome_funcionario']).order_by('nome_funcionario')	
            if form_busca.cleaned_data['setor'] != None:
		setor_form = form_busca.cleaned_data['setor']
                lista = lista.filter(setor = form_busca.cleaned_data['setor'])
            if form_busca.cleaned_data['cargo'] != None:
		cargo_form = form_busca.cleaned_data['cargo']
                lista = lista.filter(cargo = form_busca.cleaned_data['cargo'])
            if form_busca.cleaned_data['funcoes'] != None:
		funcao_form = form_busca.cleaned_data['funcoes']
		id_funcionarios = []
		for funcionario in lista:
			id_funcionarios.append(funcionario.id)
			lista = Servidor.objects.filter(id__in = id_funcionarios)
			lista = lista.filter(funcoes = form_busca.cleaned_data['funcoes'])
            tamanho_total_lista = len(lista)
            if tamanho_total_lista < 7:
		inicio = 0
		fim = 7
            lista_paginada = lista[inicio:fim]
            if len(lista_paginada) < 7:
		linhas_vazias = (7-len(lista_paginada))*[1]
            if request.POST['formato'] == 'relatorio':
		request.POST['formato'] == ''
		return render_to_response('impressao.html', locals(), context_instance = RequestContext(request))
            else:
		return render_to_response('exibir.html', locals(), context_instance = RequestContext(request))
        else:
            return render_to_response('exibir.html', locals(), context_instance = RequestContext(request))
    else: 
        return render_to_response('exibir.html', locals(), context_instance = RequestContext(request))

