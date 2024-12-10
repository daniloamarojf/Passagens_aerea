import sqlite3
import os
from prettytable import PrettyTable


def criar_clientes():
    
    conn = sqlite3.connect("C:/Python/Passagens_aerea/Passagens_aerea/Banco_dados.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf INTEGER (11),
            telefone VARCHAR(14),
            data_nascimento date
        )
    ''')
    conn.commit()
    conn.close()
