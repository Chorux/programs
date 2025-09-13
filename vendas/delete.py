import mysql.connector

conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="[password]",#altere para senha da sua database
        database="[database]",#altere para o nome da sua database

    )
cursor = conexao.cursor()

nome_produto = input("Digite o nome do produto: ")

delete = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(delete)
conexao.commit()
print("o produto {} foi deletado".format(nome_produto))


cursor.close()
conexao.close()