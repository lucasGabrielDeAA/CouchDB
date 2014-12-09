#coding:utf-8

import json
import requests
from os import system
from produto import Produto
import time

#Caminho do banco de dados CouchDB
url = 'http://127.0.0.1:5984'
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
r = requests.head(url + '/' + db_name)

clean_screen = lambda: os.system('clear')

if __name__ == '__main__':
	print 'Bem vindo'

	while True:
		clean_screen()

		##Verificando a existência do banco de dados.
		if r.status_code == 200
			print opcoes
			opcao = input('Opção escolhida: ')

			##Adicionar produto
			if opcao == 1:
				system('clear')
				print 'Adicionar Produto\n\n'

				nome = raw_input('Nome do produto: ')
				descricao = raw_input('Descrição para o produto: ')
				preco = int(raw_input('Preço do produto: '))
				quantidade = int(raw_input('Quantidade em estoque: '))
				_id++

				##Criando um objeto produto que será utilizado para realizar a requisição do tipo PUT.
				produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

				##Realizando a requisição do tipo PUT para criação do objeto.
				request = requests.put(url + put + '/' + db_name + '/_design/' + produto)

			##Editar produto
			elif opcao == 2:
				clean_screen()
				print 'Editar produto\n\n'

			##Consultar produto
			elif opcao == 3:
				clean_screen()
				print 'Consultar produto\n\n'

			##Exibir produtos
			elif opcao == 4:
				clean_screen()
				print 'Listagem de Produtos\n\n'

			##Remover produto
			elif opcao == 5:
				clean_screen()
				print 'Remover produto\n\n'


			elif opcao == 6:
				clean_screen()
				print 'Volte Sempre'
				break

			raw_input('\nPressione para continuar...')

		elif r.status_code == 404
			print 'Aguarde enquanto o banco de dados é criado...\n\n'
			request = requests.put(put + '/' + db_name)

			for index in range(5):
				print '%s s até a conclusão' % index
				time.sleep(index)

			print 'Banco de dados %s criado' % db_name

			##Adicionar produto
			if opcao == 1:
				clean_screen()
				print 'Adicionar Produto\n\n'
				nome = raw_input('Nome do produto: ')
				descricao = raw_input('Descrição para o produto: ')
				preco = int(raw_input('Preço do produto: '))
				quantidade = int(raw_input('Quantidade em estoque: '))
				_id++

				##Criando um objeto produto que será utilizado para realizar a requisição do tipo PUT.
				produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

				request = requests.put(url + put + '/' + db_name + '/_design/' + produto)

			##Editar produto
			elif opcao == 2:
				clean_screen()

			##Consultar produto
			elif opcao == 3:
				clean_screen()

			##Exibir produtos
			elif opcao == 4:
				clean_screen()
				print 'Listagem de Produtos'

			##Remover produto
			elif opcao == 5:
				clean_screen()

			elif opcao == 6:
				clean_screen()
				print 'Volte Sempre'
				break

			raw_input('\nPressione para continuar...')