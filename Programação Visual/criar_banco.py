import sqlite3

conn = sqlite3.connect('agendamentos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    professor TEXT NOT NULL,
    materia TEXT NOT NULL,
    data_hora TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
