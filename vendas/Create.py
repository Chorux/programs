

import mysql.connector


conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="[password]",#altere para senha da sua database
        database="[database]",#altere para o nome da sua database

    )
cursor = conexao.cursor()
    # CREATE
nome_produtor = input("Digite o nome do produto: ")
valor = input("Digite o valor do produto: ")

create = f'INSERT INTO Vendas (nome_produto, valor)' f'VALUES ("{nome_produtor}", {valor})'
cursor.execute(create)
conexao.commit()

print("O Produto ", nome_produtor, "foi cadastrado com sucesso, no valor de", valor)

cursor.close()
conexao.close()


