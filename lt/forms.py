# -* coding:utf-8 -*-

from django import forms
from models import *

class Form_Adiciona_Servidor(forms.ModelForm):
		
	class Meta:
		model = Servidor
		fields = ('nome_funcionario', 'foto', 'cargo', 'setor', 'funcoes', 'telefones')
