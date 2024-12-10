import sqlite3
import os
from prettytable import PrettyTable

def cabecalho(nome_cabecalho):
    print (f':::::::::: { nome_cabecalho } ::::::::::\n\n')
    return()


def crud():
        
    print('1 - Adicionar\n')
    print('2 - Alterar dados\n')  
    print('3 - Remover \n')  
    print('4 - Visualizar \n')
        
  

        
    
'''    opcao = input('===> Escolha a opção: ')
    
    if opcao == '1':
        os.system('cls')
        
        conn = sqlite3.connect("BancoDados/meu_banco_de_dados.db")
        cursor = conn.cursor()
        
        print(':::::::::: ADICINAR CLIENTE ::::::::::\n\n')
        nome = input('Nome cliente: ')
        cpf = input('CPF: ')
        telefone = input('Telefone: ')
        data_nascimento = input('Data de nascimento: ')
        
        dados_cliente = (nome, cpf, telefone, data_nascimento)
        
        cursor.execute('INSERT INTO clientes (nome, cpf, telefone, data_nascimento) VALUES (?,?,?,?)', dados_cliente)
        
        conn.commit()
        print()
        input('Cliente adicionado com sucesso. Pressione enter!')
        conn.close()
'''