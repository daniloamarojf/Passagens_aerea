import sqlite3
import os
from prettytable import PrettyTable
from controle_passagens.tabelas import criar_clientes
from controle_passagens.funcoes import cabecalho, crud, crud_tabelas
from controle_passagens.adicionar import adicionar_cliente
from controle_passagens.alterar import alterar_cliente
from controle_passagens.remover import remover_cliente
from controle_passagens.visualizar import visualizar_cliente

criar_clientes()

os.system('cls')
while True:
    os.system('cls')
    crud_tabelas()
  
    opcao_tabelas = input('====> Qual tabela deseja administar? ')

    if opcao_tabelas == '1':
        os.system('cls')
        cabecalho('CLIENTE')
        crud()
        opcao = input('=====> Escolha a opção: ')
        
        
        if opcao == '1':
            cabecalho('ADICIONAR CLIENTE')
            adicionar_cliente()
        elif opcao == '2':
            cabecalho('ALTERAR CLIENTE')
            alterar_cliente()
        elif opcao == '3':
            cabecalho('REMOVER CLIENTE')
            remover_cliente()
        elif opcao == '4':
            cabecalho('VISUALIZAR CLIENTE')
            visualizar_cliente()
        else:
            input('Opção inválida! Pressione enter.')    
            
            

       







