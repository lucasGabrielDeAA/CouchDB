#coding:utf-8

import json
import requests
from os import system
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
				preco = int(raw_input('Preço do produto: '))
				quantidade = int(raw_input('Quantidade em estoque: '))
				_id = _id+1

				##Criando um objeto produto que será utilizado para realizar a requisição do tipo PUT.
				produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

				##Realizando a requisição do tipo PUT para criação do objeto.
				put = requests.put(url + put + '/' + db_name + '/_design/' + produto)

				if put.status_code == 200:
					print 'Produto Cadastrado'
				else:
					print 'Impossível cadastrar produto'

			##Editar produto
			elif opcao == 2:
				clean_screen()
				print 'Editar produto\n\n'

				id_produto = raw_input('Id do produto: ')

				edita_produto = requests.get(url + '/' + db_name + '/' + id_produto)

				dados = json.loads(edita_produto)

				try:
					nome = raw_input('Nome do produto: ')
					descricao = raw_input('Descrição para o produto: ')
					preco = int(raw_input('Preço do produto: '))
					quantidade = int(raw_input('Quantidade em estoque: '))

					produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

					put = requests.put(url + put + '/' + db_name + '/_design/' + produto)

					if put.status_code == 200:
						print 'Produto Alterado com sucesso'
				except:
					print 'Id inválido!'

			##Consultar produto
			elif opcao == 3:
				clean_screen()
				print 'Consultar produto\n\n'

				id_produto = raw_input('Id do produto: ')

				busca_produto = requests.get(url + '/' + db_name + '/' + id_produto)

				dados = json.loads(busca_produto)

				try:
					print 'Nome: ', dados['nome']
					print 'Descrição: ', dados['descricao']
					print 'Preço: ', dados['preco']
					print 'Quantidade em estoque: ', dados['quantidade']
				except:
					print 'Id inválido!'

			##Exibir produtos
			elif opcao == 4:
				clean_screen()
				print 'Listagem de Produtos\n\n'

				r = requests.get(url + '/' + db_name + '_all_docs')

				for ids in json.loads(r.content).get('_id'):
					r = requests.get(url + '/' + db_name + '/' + str(ids))

					arquivo = open('arquivo.xml', 'w+')
					arquivo.write(r.content)
					arquivo.close()

					print 'id do produto: ', str(ids) 
					print 'Nome: ', str(etree.parse('arquivo.xml').getroot().find('nome').attrib['value'])
					print 'Desrição: ', str(etree.parse('arquivo.xml').getroot().find('descricao').attrib['value'])
					print 'Preço: ', str(etree.parse('arquivo.xml').getRoot().find('preco').attrib['value'])
					print 'Quantidade em estoque: ', str(etree.parse('arquivo.xml').getRoot().find('quantidade').attrib['value'])

					os.remove('arquivo.xml')

			##Remover produto
			elif opcao == 5:
				clean_screen()
				print 'Remover produto\n\n'

				id_produto = raw_input('Id do produto: ')

				try:
					busca_produto = requests.get(url + '/' + db_name + '/' + id_produto)
					produto = json.loads(busca_produto)

					print 'O arquivo abaixo será deletado\n\n'
					print 'Nome: ', produto['nome']
					print 'Descrição: ', produto['descricao']
					print 'Preço: ', produto['preco']
					print 'Quantidade em estoque: ', produto['quantidade']

					delete = requests.delete(url + '/' + db_name + '/_design/' + produto)

					if delete.status_code == 200:
						print 'Produto de id"%s" removido com sucesso' % id_produto
				except:
					print 'Id inválido!'

			elif opcao == 6:
				clean_screen()
				print 'Volte Sempre'
				break

			raw_input('\nPressione para continuar...')

		elif head.status_code == 404:
			print 'Banco de Dados não encontrado...\n'
			print 'Aguarde enquanto o banco de dados é criado...\n\n'
			
			for index in range(5):
				print '%s s até a conclusão...' % index
				time.sleep(1)

			put_db = requests.put(put + '/' + db_name)

			print 'Banco de dados %s criado' % db_name

			##Adicionar produto
			if opcao == 1:
				system('clear')
				print 'Adicionar Produto\n\n'

				nome = raw_input('Nome do produto: ')
				descricao = raw_input('Descrição para o produto: ')
				preco = int(raw_input('Preço do produto: '))
				quantidade = int(raw_input('Quantidade em estoque: '))
				_id = _id+1

				##Criando um objeto produto que será utilizado para realizar a requisição do tipo PUT.
				produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

				##Realizando a requisição do tipo PUT para criação do objeto.
				put = requests.put(url + put + '/' + db_name + '/_design/' + produto)

				if put.status_code == 200:
					print 'Produto Cadastrado'
				else:
					print 'Impossível cadastrar produto'

			##Editar produto
			elif opcao == 2:
				clean_screen()
				print 'Editar produto\n\n'

				id_produto = raw_input('Id do produto: ')

				edita_produto = requests.get(url + '/' + db_name + '/' + id_produto)

				dados = json.loads(edita_produto)

				try:
					nome = raw_input('Nome do produto: ')
					descricao = raw_input('Descrição para o produto: ')
					preco = int(raw_input('Preço do produto: '))
					quantidade = int(raw_input('Quantidade em estoque: '))

					produto = json.dumps({'id':_id, 'nome':nome, 'descricao': descricao, 'preco': preco, 'quantidade':quantidade})

					put = requests.put(url + put + '/' + db_name + '/_design/' + produto)

					if put.status_code == 200:
						print 'Produto Alterado com sucesso'
				except:
					print 'Id inválido!'

			##Consultar produto
			elif opcao == 3:
				clean_screen()
				print 'Consultar produto\n\n'

				id_produto = raw_input('Id do produto: ')

				busca_produto = requests.get(url + '/' + db_name + '/' + id_produto)

				dados = json.loads(busca_produto)

				try:
					print 'Nome: ', dados['nome']
					print 'Descrição: ', dados['descricao']
					print 'Preço: ', dados['preco']
					print 'Quantidade em estoque: ', dados['quantidade']
				except:
					print 'Id inválido!'

			##Exibir produtos
			elif opcao == 4:
				clean_screen()
				print 'Listagem de Produtos\n\n'

				r = requests.get(url + '/' + db_name + '_all_docs')

				for ids in json.loads(r.content).get('_id'):
					r = requests.get(url + '/' + db_name + '/' + str(ids))

					arquivo = open('arquivo.xml', 'w+')
					arquivo.write(r.content)
					arquivo.close()

					print 'id do produto: ', str(ids) 
					print 'Nome: ', str(etree.parse('arquivo.xml').getroot().find('nome').attrib['value'])
					print 'Desrição: ', str(etree.parse('arquivo.xml').getroot().find('descricao').attrib['value'])
					print 'Preço: ', str(etree.parse('arquivo.xml').getRoot().find('preco').attrib['value'])
					print 'Quantidade em estoque: ', str(etree.parse('arquivo.xml').getRoot().find('quantidade').attrib['value'])

					os.remove('arquivo.xml')

			##Remover produto
			elif opcao == 5:
				clean_screen()
				print 'Remover produto\n\n'

				id_produto = raw_input('Id do produto: ')

				try:
					busca_produto = requests.get(url + '/' + db_name + '/' + id_produto)
					produto = json.loads(busca_produto)

					print 'O arquivo abaixo será deletado\n\n'
					print 'Nome: ', produto['nome']
					print 'Descrição: ', produto['descricao']
					print 'Preço: ', produto['preco']
					print 'Quantidade em estoque: ', produto['quantidade']

					delete = requests.delete(url + '/' + db_name + '/_design/' + produto)

					if delete.status_code == 200:
						print 'Produto de id"%s" removido com sucesso' % id_produto
				except:
					print 'Id inválido!'

			elif opcao == 6:
				clean_screen()
				print 'Volte Sempre'
				break

			raw_input('\nPressione para continuar...')