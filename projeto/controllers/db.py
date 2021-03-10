import sqlite3
from controllers.socio import Socio

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def criar_tabelas():
    cursor.execute("""
    CREATE TABLE socios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        cargo TEXT NOT NULL,
        ramal TEXT NOT NULL UNIQUE
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

def cadastrar_socio():
    print("[+] CADASTRO DE SÓCIO\n")
    try:
        nome = input("Informe o nome: ")
        cargo = input("Informe o cargo: ")
        ramal = input("Informe o ramal: ")
    except Exception as error:
        print(error)
        return False
    else:
        if (nome != "") and (cargo != "") and (ramal != ""):
            socio = Socio(nome, cargo, ramal)
            try:
                cursor.execute("""
                INSERT INTO socios (nome, cargo, ramal)
             	VALUES (?,?,?)
        	    """, (socio.nome, socio.cargo, socio.ramal))
            except sqlite3.IntegrityError:
                print("[!] Nome e/ou ramal já está em uso!")
                cadastrar_socio()
            else:
                conn.commit()
				print("[+] C
                return True
        else:
            print("[!] Preencha todos os campos!")
            cadastrar_socio()


