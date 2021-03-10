import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE socios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        ramal TEXT NOT NULL
);
""")



cursor.execute("""
CREATE TABLE salas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        numero INTEGER NOT NULL UNIQUE,
		vagas INTEGER NOT NULL
);
""")

cursor.execute("""
CREATE TABLE agenda (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        numero_sala INTEGER NOT NULL,
		socio TEXT NOT NULL,
        dia TEXT NOT NULL,
        hora_inicio TEXT NOT NULL,
		hora_final TEXT NOT NULL
);
""")

