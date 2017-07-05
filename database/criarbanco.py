import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""CREATE TABLE horarios(id INTEGER PRIMARY KEY AUTOINCREMENT,
domingo CHAR(1), segunda CHAR(1), terca CHAR(1), quarta CHAR(1),
quinta CHAR(1), sexta CHAR(1), sabado CHAR(1), horario TIME,
duracao INTEGER, musica CHAR(512), nomemusica CHAR(512));""")

conn.close()

print ('banco de dados criado')
