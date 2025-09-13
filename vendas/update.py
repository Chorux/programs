import mysql.connector

conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="[password]",#altere para senha da sua database
        database="[database]",#altere para o nome da sua database

    )
cursor = conexao.cursor()

#update
Tabela = input("Tabela: ")
nome_produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))

update = f'UPDATE loja SET valor = {valor} WHERE Produto = "{nome_produto}"'
cursor.execute(update)
conexao.commit()
print("O produto", nome_produto, "foi atualizado com sucesso, Para o valor de: R$", valor)


cursor.close()
conexao.close()