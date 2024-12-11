import sqlite3
import os
from prettytable import PrettyTable


def visualizar_cliente():
        
    conn = sqlite3.connect("C:/Python/Passagens_aerea/Passagens_aerea/Banco_dados.db")
    cursor = conn.cursor()
        
    id_cliente = input('Qual a identificação do Cliente que deseja visualizar? ')    
        
    cursor.execute('SELECT * FROM clientes WHERE id_cliente = ?', (id_cliente,))   # pORQUE ESSA VÍRGULA?
    resultados = cursor.fetchall()
        
    tabela = PrettyTable()
        
    colunas = [descricao [0] for descricao in cursor.description]
        
    tabela.field_names = colunas
        
    for row in resultados:
        tabela.add_row(row)
            
    print(tabela)
    input('Pressione Enter')
    conn.close()
        
    
        
    