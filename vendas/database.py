import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="[password]",
    database="[database]",

)
cursor = conexao.cursor()
#comandos aqui




cursor.close()
conexao.close()