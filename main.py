import sqlite3
import os
from prettytable import PrettyTable
from controle_passagens.tabelas import criar_clientes
from controle_passagens.funcoes import cabecalho, crud
from controle_passagens.adicionar import adicionar_cliente



criar_clientes()

while True:
    crud()
    opcao = input('=====> Escolha a opção: ')
    
    if opcao == '1':
        cabecalho('CLIENTE')
        adicionar_cliente()
        

       







