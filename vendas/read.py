
import requests
from tkinter import *

import mysql.connector


#READ
def Ler_codigo():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="[password]",#altere para senha da sua database
        database="[database]",#altere para o nome da sua database

    )
    cursor = conexao.cursor()
    read = f'SELECT * FROM vendas;'
    cursor.execute(read)
    print(cursor.fetchall())
    cursor.close()
    conexao.close()




