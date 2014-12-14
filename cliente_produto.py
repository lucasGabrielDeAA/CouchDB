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
_id = 0

opcoes = '''Cliente CouchDB\n\n\n
Seleciona a opção desejada:\n
1 - Adicionar produto
2 - Editar produto
3 - Consulta de produtos
4 - Exibir produtos
5 - Remover produto
6 - Sair
'''

##Requisição realizada para verificar a existência do banco de dados.
head = requests.head(url + '/' + db_name)

clean_screen = lambda: os.system('clear')

if __name__ == '__main__':
	print 'Bem vindo'

	while True:
		clean_screen()

		##Verificando a existência do banco de dados.
		if head.status_code == 200:
			print opcoes
			opcao = input('Opção escolhida: ')

			##Adicionar produto
			if opcao == 1:
				system('clear')
				print 'Adicionar Produto\n\n'

				nome = raw_input('Nome do produto: ')
				descricao = raw_input('Descrição para o produto: ')
				preco = float(raw_input('Preço do produto: '))
				quantidade = int(raw_input('Quantidade em estoque: '))
				_id = _id+1

				##Criando um objeto produto que será utilizado para realizar a requisição do tipo PUT.
				produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

				##Realizando a requisição do tipo PUT para criação do objeto.
				put = requests.put(url + ':' + porta + put + '/' + db_name + '/_design/' + produto)

				if put.status_code == 200:
					print '\nProduto Cadastrado\n'
				else:
					print '\nImpossível cadastrar produto\n'

			##Editar produto
			elif opcao == 2:
				clean_screen()
				print 'Editar produto\n\n'

				id_produto = raw_input('Id do produto: ')

				edita_produto = requests.get(url + ':' + porta + '/' + db_name + '/' + id_produto)

				dados = json.loads(edita_produto)

				try:
					nome = raw_input('Nome do produto: ')
					descricao = raw_input('Descrição para o produto: ')
					preco = float(raw_input('Preço do produto: '))
					quantidade = int(raw_input('Quantidade em estoque: '))

					produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

					put = requests.put(url + ':' + porta + put + '/' + db_name + '/_design/' + produto)

					if put.status_code == 200:
						print '\nProduto Alterado com sucesso\n'
				except:
					print '\nId inválido!\n'

			##Consultar produto
			elif opcao == 3:
				clean_screen()
				print 'Consultar produto\n\n'

				id_produto = raw_input('Id do produto: ')

				busca_produto = requests.get(url + ':' + porta + '/' + db_name + '/' + id_produto)

				dados = json.loads(busca_produto)

				try:
					print 'Nome: ', dados['nome']
					print 'Descrição: ', dados['descricao']
					print 'Preço: ', dados['preco']
					print 'Quantidade em estoque: ', dados['quantidade']
				except:
					print '\nId inválido!\n'

			##Exibir produtos
			elif opcao == 4:
				clean_screen()
				print 'Listagem de Produtos\n\n'

				try:
					req_get = requests.get(url + ':' + porta + '/' + db_name + '_all_docs')

					for r in json.loads(req_get.content):
						print 'id do produto: ', r['id'] 
						print 'Nome: ', r['nome']
						print 'Desrição: ', r['descricao']
						print 'Preço: ', r['preco']
						print 'Quantidade em estoque: ', r['quantidade']
				except:
					print '\nO Banco de dados está vazio!\n'

			##Remover produto
			elif opcao == 5:
				clean_screen()
				print 'Remover produto\n\n'

				id_produto = raw_input('Id do produto: ')

				try:
					busca_produto = requests.get(url + ':' + porta + '/' + db_name + '/' + id_produto)
					produto = json.loads(busca_produto)

					print 'O arquivo abaixo será deletado\n\n'
					print 'Nome: ', produto['nome']
					print 'Descrição: ', produto['descricao']
					print 'Preço: ', produto['preco']
					print 'Quantidade em estoque: ', produto['quantidade']

					delete = requests.delete(url + ':' + porta + '/' + db_name + '/_design/' + produto)

					if delete.status_code == 200:
						print '\nProduto de id"%s" removido com sucesso\n' % id_produto
				except:
					print '\nId inválido!\n'

			elif opcao == 6:
				clean_screen()
				print 'Volte Sempre'
				break

			raw_input('\nPressione para continuar...')

		elif head.status_code == 404:
			print 'Banco de Dados não encontrado...\n'
			print 'Aguarde enquanto o banco de dados é criado...\n\n'
			
			for index in range(5):
				print '%s s até a conclusão...' % index + 1
				time.sleep(1)

			put_db = requests.put(url + '/' + db_name)

			print 'Banco de dados %s criado' % db_name

			print opcoes
			opcao = input('Opção escolhida: ')

			##Adicionar produto
			##Adicionar produto
			if opcao == 1:
				system('clear')
				print 'Adicionar Produto\n\n'

				nome = raw_input('Nome do produto: ')
				descricao = raw_input('Descrição para o produto: ')
				preco = float(raw_input('Preço do produto: '))
				quantidade = int(raw_input('Quantidade em estoque: '))
				_id = _id+1

				##Criando um objeto produto que será utilizado para realizar a requisição do tipo PUT.
				produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

				##Realizando a requisição do tipo PUT para criação do objeto.
				put = requests.put(url + ':' + porta + put + '/' + db_name + '/_design/' + produto)

				if put.status_code == 200:
					print '\nProduto Cadastrado\n'
				else:
					print '\nImpossível cadastrar produto\n'

			##Editar produto
			elif opcao == 2:
				clean_screen()
				print 'Editar produto\n\n'

				id_produto = raw_input('Id do produto: ')

				edita_produto = requests.get(url + ':' + porta + '/' + db_name + '/' + id_produto)

				dados = json.loads(edita_produto)

				try:
					nome = raw_input('Nome do produto: ')
					descricao = raw_input('Descrição para o produto: ')
					preco = float(raw_input('Preço do produto: '))
					quantidade = int(raw_input('Quantidade em estoque: '))

					produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

					put = requests.put(url + ':' + porta + put + '/' + db_name + '/_design/' + produto)

					if put.status_code == 200:
						print '\nProduto Alterado com sucesso\n'
				except:
					print '\nId inválido!\n'

			##Consultar produto
			elif opcao == 3:
				clean_screen()
				print 'Consultar produto\n\n'

				id_produto = raw_input('Id do produto: ')

				busca_produto = requests.get(url + ':' + porta + '/' + db_name + '/' + id_produto)

				dados = json.loads(busca_produto)

				try:
					print 'Nome: ', dados['nome']
					print 'Descrição: ', dados['descricao']
					print 'Preço: ', dados['preco']
					print 'Quantidade em estoque: ', dados['quantidade']
				except:
					print '\nId inválido!\n'

			##Exibir produtos
			elif opcao == 4:
				clean_screen()
				print 'Listagem de Produtos\n\n'

				try:
					req_get = requests.get(url + ':' + porta + '/' + db_name + '_all_docs')

					for r in json.loads(req_get.content):
						print 'id do produto: ', r['id'] 
						print 'Nome: ', r['nome']
						print 'Desrição: ', r['descricao']
						print 'Preço: ', r['preco']
						print 'Quantidade em estoque: ', r['quantidade']
				except:
					print '\nO Banco de dados está vazio!\n'

			##Remover produto
			elif opcao == 5:
				clean_screen()
				print 'Remover produto\n\n'

				id_produto = raw_input('Id do produto: ')

				try:
					busca_produto = requests.get(url + ':' + porta + '/' + db_name + '/' + id_produto)
					produto = json.loads(busca_produto)

					print 'O arquivo abaixo será deletado\n\n'
					print 'Nome: ', produto['nome']
					print 'Descrição: ', produto['descricao']
					print 'Preço: ', produto['preco']
					print 'Quantidade em estoque: ', produto['quantidade']

					delete = requests.delete(url + ':' + porta + '/' + db_name + '/_design/' + produto)

					if delete.status_code == 200:
						print '\nProduto de id"%s" removido com sucesso\n' % id_produto
				except:
					print '\nId inválido!\n'

			elif opcao == 6:
				clean_screen()
				print 'Volte Sempre'
				break

			raw_input('\nPressione para continuar...')