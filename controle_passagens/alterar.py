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
        opcao_alterar = input(f'Deseja realmente alter o cliente: {nome_cliente} ? (1 - Sim/ 2 - Não): ')
        
        if opcao_alterar == '1':
            novo_nome = input('Nome: ')
            novo_cpf = input('CPF: ')
            novo_telefone = input('Telefone:')
            nova_data_nascimento = input('Data de nascimento: ')
        
            dados_cliente = (novo_nome, novo_cpf,novo_telefone, nova_data_nascimento, id_cliente)
        
            cursor.execute('UPDATE clientes SET nome = ?, cpf = ?, telefone = ?, data_nascimento = ? WHERE id_cliente = ?',
                (dados_cliente))
        
            conn.commit()
            print()
            input('Deseja continuar alterando Clientes? Pressione enter!')
            conn.close()    
        elif opcao_alterar == '2':
            input('Cliente NÃO atualizado. Pressione enter!')
        else:
            input('Opção inválida!')
        
    else:
        input(f'Cliente com ID {id_cliente} não encontardo. Pressione enter!')
