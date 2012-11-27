# -* coding:utf-8 -*-

from django import forms
from models import *

class Form_Adiciona_Servidor(forms.ModelForm):
		
	class Meta:
		model = Servidor
		fields = ('nome_funcionario', 'foto', 'cargo', 'setor', 'funcoes', 'telefones')

class Form_Busca_Funcionario(forms.Form):
	nome_funcionario = forms.CharField(label = 'Nome', required = False)
	cargo = forms.ModelChoiceField(queryset=Cargo.objects.all().order_by('desc_cargo'), required = False)
	setor = forms.ModelChoiceField(queryset=Setor.objects.all().order_by('desc_setor'), required = False)
	funcoes = forms.ModelChoiceField(queryset=Funcao.objects.all().order_by('desc_funcao'), label = 'Função', required = False)

		
	fields = ('nome_funcionario', 'cargo', 'funcoes', 'setor')
