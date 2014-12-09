#coding:utf-8

import json

##Classe Produto com seus respectivos atributos
class Produto:
	##Contrutor
	def __init__(self, _id, nome, descricao, preco, quantidade):
		self._id = _id
		self.nome = nome
		self.descricao = descricao
		self.preco = preco
		self.quantidade = quantidade

	def toString(self):
		return json.dumps({'id': self._id, 'nome':self.nome, 'descricao':self.descricao, 'preco':self.preco, 'quantidade':self.quantidade})