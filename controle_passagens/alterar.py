import sqlite3
import os
from prettytable import PrettyTable


def alterar_cliente(): 
        
    conn = sqlite3.connect("C:/Python/Passagens_aerea/Passagens_aerea/Banco_dados.db")
    cursor = conn.cursor()
        
    id_cliente = input('Qual a identificação do Cliente a ser ALTERADO?: ')
        
    cursor.execute('SELECT nome FROM clientes WHERE id_cliente = ?', (id_cliente))
    cliente = cursor.fetchone()
        
    if cliente:
        print()
        nome_cliente = cliente[0]
        print(f'Pode atualizar os dados de {nome_cliente} agora\n')
        novo_nome = input('Nome: ')
        novo_cpf = input('CPF: ')
        novo_telefone = input('Telefone:')
        nova_data_nascimento = input('Data de nascimento: ')
        
        dados_cliente = (novo_nome, novo_cpf,novo_telefone, nova_data_nascimento, id_cliente)
        
        cursor.execute('UPDATE clientes SET nome = ?, cpf = ?, telefone = ?, data_nascimento = ? WHERE id_cliente = ?',
                   (dados_cliente))
        
        conn.commit()
        print()
        input('Dados atualizados com sucesso. Pressione enter!')
        conn.close()
    else:
        print(f'Cliente com ID {id_cliente} não encontardo')
