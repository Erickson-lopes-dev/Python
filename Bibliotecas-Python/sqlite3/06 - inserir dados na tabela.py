import sqlite3

ligacao = sqlite3.connect('banco.db')
cursor = ligacao.cursor()

sql = 'INSERT INTO cliente'

cursor.execute(sql)
