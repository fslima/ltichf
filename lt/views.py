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
		objeto = Funcionario.objects.get(pk = idObjeto)
        	telefones = objeto.telefones.all()
		funcoes = objeto.funcoes.all()
        	form = Form_Adiciona_Servidor(instance = objeto)
    if request.method == 'POST': 
	form_busca = Form_Busca_Funcionario(request.POST)
        if form_busca.is_valid():
            inicio = int(request.POST['inicio'])
            fim = int(request.POST['fim'])
            lista = Funcionario.objects.filter(nome_funcionario__icontains = form_busca.cleaned_data['nome_funcionario']).order_by('nome_funcionario')	
            if form_busca.cleaned_data['setor'] != None:
                lista = lista.filter(setor = form_busca.cleaned_data['setor'])
            if form_busca.cleaned_data['cargo'] != None:
                lista = lista.filter(cargo = form_busca.cleaned_data['cargo'])
            if form_busca.cleaned_data['funcoes'] != None:
                lista = lista.filter(funcoes = form_busca.cleaned_data['funcoes'])
            tamanho_total_lista = len(lista)
            lista = lista[inicio:fim]
            if len(lista) < 7:
		linhas_vazias = (7-len(lista))*[1]
            return render_to_response('exibir.html', locals(), context_instance = RequestContext(request))
        else:
            return render_to_response('exibir.html', locals(), context_instance = RequestContext(request))
    else: 
        return render_to_response('exibir.html', locals(), context_instance = RequestContext(request))

