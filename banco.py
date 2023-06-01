import sqlite3

banco = sqlite3.connect('celulares.db')
cursor = banco.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS celulares
               (marca text, modelo text, valor text)''')


