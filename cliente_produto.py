#coding:utf-8

import json
import requests
import os
from os import system
import time

#Caminho do banco de dados CouchDB
url = 'http://127.0.0.1'
porta = '5984'
db_name = 'produto'
delete = '/delete'
put = '/put'
post = '/post'

opcoes = '''Cliente CouchDB\n\n\n
Seleciona a opção desejada:\n
1 - Adicionar produto
2 - Editar produto
3 - Consulta de produtos
4 - Exibir produtos
5 - Remover produto
6 - Sair
'''

def gera_id():
	gera = requests.get(url + ':' + porta + '/_uuids')
	resp = json.loads(gera.content)

	return resp['uuids']


def add_produto():
	##Verificando a existência do banco de dados.
	verifica_banco()

	mensagem = []

	nome = raw_input('Nome do produto: ')
	descricao = raw_input('Descrição para o produto: ')
	preco = float(raw_input('Preço do produto: '))
	quantidade = int(raw_input('Quantidade em estoque: '))
	_id = gera_id()

	##Criando um objeto produto que será utilizado para realizar a requisição do tipo PUT.
	produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

	##Realizando a requisição do tipo PUT para criação do objeto.
	put = requests.put(url + ':' + porta + put + '/' + db_name + '/' + _id + '/' + produto)

	if put.status_code == 200:
		mensagem.append('Produto Cadastrado')
	else:
		mensagem.append('Impossível cadastrar produto')

	return mensagem

def edita_produto():
	##Verificando a existência do banco de dados.
	verifica_banco()

	mensagem = []

	id_produto = raw_input('Id do produto: ')

	edita_produto = requests.get(url + ':' + porta + '/' + db_name + '/' + id_produto)
	dados = json.loads(edita_produto)

	if edita_produto.status_code == 200:
		mensagem.append('Dados do produto\n\n')
		mensagem.append('Nome: ' + dados['nome'])
		mensagem.append('Descrição: ' + dados['descricao'])
		mensagem.append('Preço: ' + dados['preco'])
		mensagem.append('Quantidade em estoque: ' + dados['quantidade'])

		nome = raw_input('Nome do produto: ')
		descricao = raw_input('Descrição para o produto: ')
		preco = float(raw_input('Preço do produto: '))
		quantidade = int(raw_input('Quantidade em estoque: '))

		produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

		put = requests.put(url + ':' + porta + put + '/' + db_name + '/_design/' + produto)

		if put.status_code == 200:
			mensagem.append('Produto alterado com sucesso')
		else:
			mensagem.append('Produto não alterado')
	else:
		mensagem.append('Id inválido!')

	return mensagem

def busca_produto():
	##Verificando a existência do banco de dados.
	verifica_banco()

	mensagem = []

	id_produto = raw_input('Id do produto: ')

	busca_produto = requests.get(url + ':' + porta + '/' + db_name + '/' + id_produto)

	dados = json.loads(busca_produto)

	if busca_produto.status_code == 200:
		mensagem.append('Nome: ' + dados['nome'])
		mensagem.append('Descrição: ' + dados['descricao'])
		mensagem.append('Preço: ' + dados['preco'])
		mensagem.append('Quantidade em estoque: ' + dados['quantidade'])
	else:
		mensagem.append('Id inválido!')

	return mensagem

def exibe_produtos():
	##Verificando a existência do banco de dados.
	verifica_banco()

	mensagem = []

	req_get = requests.get(url + ':' + porta + '/' + db_name + '_all_docs')

	if req_get.status_code == 200:
		for r in json.loads(req_get.content):
			mensagem.append('id do produto: ' + r['id'])
			mensagem.append('Nome: ' + r['nome'])
			mensagem.append('Desrição: ' + r['descricao'])
			mensagem.append('Preço: ' + r['preco'])
			mensagem.append('Quantidade em estoque: ' + r['quantidade'])
			mensagem.append('\n\n')
	else:
		mensagem.append('O Banco de dados está vazio!')

	return mensagem

def deleta_produto():
	##Verificando a existência do banco de dados.
	verifica_banco()
	
	mensagem = []

	id_produto = raw_input('Id do produto: ')

	busca_produtos = requests.get(url + ':' + porta + '/' + db_name + '/' + id_produto)
	
	produto = json.loads(busca_produtos)

	if busca_produtos.status_code == 201:
		mensagem.append('O arquivo abaixo será deletado\n\n')
		mensagem.append('Nome: ' + produto['nome'])
		mensagem.append('Descrição: ' + produto['descricao'])
		mensagem.append('Preço: ' + produto['preco'])
		mensagem.append('Quantidade em estoque: ' + produto['quantidade'])

		delete = requests.delete(url + ':' + porta + '/' + db_name + '/_design/' + produto)

		if delete.status_code == 200:
			mensagem.append('\nProduto de id"%s" removido com sucesso\n' % id_produto)
		else:
			mensagem.append('\nProduto de id"%s" não removido\n' % id_produto)
	else:
		mensagem.append('\nId inválido!\n')

	return mensagem

def verifica_banco():
	mensagem = []

	##Requisição realizada para verificar a existência do banco de dados.
	head = requests.head(url + '/' + db_name)

	if head.status_code == 404:
		mensagem.append('Banco de dados não encontrado...\n')
		mensagem.append('Aguarde esquanto o banco é criado...\n\n')

		for index in range(5, 0, -1):
				mensagem.append('%s s até a conclusão...' % index)
				time.sleep(1)

		mensagem.append('\n\n\n')

		put_db = requests.put(url + ':' + porta + '/' + db_name)

		mensagem.append('Banco de dados %s criado' % db_name)

	return mensagem

##if __name__ == '__main__':

	while True:
		print opcoes
		opcao = input('Opção escolhida: ')

		##Adicionar produto
		if opcao == 1:
			for i in add_produto():
				print i

		##Editar produto
		elif opcao == 2:
			for i in edita_produto():
				print i

		##Consultar produto
		elif opcao == 3:
			for i in busca_produto():
				print i

		##Exibir produtos
		elif opcao == 4:
			for i in exibe_produtos():
				print i

		##Remover produto
		elif opcao == 5:
			for i in deleta_produto():
				print i

		elif opcao == 6:
			break

		raw_input('\nPressione para continuar...')