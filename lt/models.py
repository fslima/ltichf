# -*- coding:utf-8 -*-

from django.db import models

class Telefone(models.Model):
    def __unicode__(self):
        return self.num_externo

    ddd = models.CharField(max_length = 2)
    num_externo = models.CharField(max_length = 8, unique = True)
    ramal = models.CharField(max_length = 4, unique = True)

class Cargo(models.Model):
    def __unicode__(self):
        return self.desc_cargo

    desc_cargo = models.CharField(max_length = 50, unique = True)

class Funcao(models.Model):
    def __unicode__(self):
        return self.desc_funcao

    desc_funcao = models.CharField(max_length = 50, unique = True)

class Setor(models.Model):
    def __unicode__(self):
        return self.desc_setor

    desc_setor = models.CharField(max_length = 50, unique = True)
    sigla = models.CharField(max_length = 6, unique = True)
    sala = models.CharField(max_length = 4)
    bloco = models.CharField(max_length = 1)


class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length = 50, unique = True)
    foto = models.ImageField(upload_to ='fotos', blank = 'True')
    setor = models.ForeignKey(Setor, related_name = 'setor_funcionario')
    cargo = models.ForeignKey(Cargo, related_name = 'cargo_funcionario')
    email = models.EmailField(max_length = 50, blank = 'True')
    telefones = models.ManyToManyField(Telefone, related_name = 'telefones_funcionario')

class Servidor(Funcionario, models.Model):
    def __unicode__(self):
        return self.nome_funcionario

    funcoes = models.ManyToManyField(Funcao, related_name = 'funcoes_funcionario', blank = 'True')

class Empresa(models.Model):
    def __unicode__(self):
        return self.nome_empresa

    nome_empresa = models.CharField(max_length = 50, unique = True)

class Contratado(Funcionario, models.Model):
    def __unicode__(self):
        return self.nome_funcionario

    empresa = models.ForeignKey(Empresa, related_name = 'empresa_contratado')
    data_fim_contrato = models.DateField(null = True, help_text = 'Formato dd/mm/aaaa')

