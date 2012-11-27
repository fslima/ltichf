# -*- coding:utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from models import *
from django.template import RequestContext
from forms import *

def sair(request):
	logout(request)
	return HttpResponseRedirect("/")


def adicionar(request, tpObjeto, idObjeto):
    '''
    if not request.user.has_perm('lt.add_'+str(tpObjeto)):
        erro = 'Você não possui acesso para cadastrar '+str(tpObjeto)
        return render_to_response("500.html", locals(), context_instance = RequestContext(request))
    '''
    if str(tpObjeto) == 'servidor':
        titulo = 'Servidor'
        form_post = Form_Adiciona_Servidor(request.POST, request.FILES)
        form_get = Form_Adiciona_Servidor()
    if request.method == 'POST': 
        form = form_post
        if form.is_valid():
            objeto_form = form.save()
            if objeto_form.adicionar() != 'validos':
                erro =  objeto_form.adicionar(request, idObjeto)
                return render_to_response("adiciona.html", locals(), context_instance = RequestContext(request))
            return HttpResponseRedirect("/lista/"+str(tpObjeto))
        else:
            return render_to_response("adiciona.html", locals(), context_instance = RequestContext(request))
    else: 
        form = form_get
        return render_to_response("adiciona.html", locals(), context_instance = RequestContext(request))

def exibir(request, tpObjeto, idObjeto):
    if str(tpObjeto) == 'servidor':
        titulo = 'Servidor'
        objeto = get_object_or_404(Servidor, pk = idObjeto)
        telefones = objeto.telefones.all()
        form = Form_Adiciona_Servidor(instance = objeto)
    return render_to_response('exibe.html', locals(), context_instance = RequestContext(request))

