import sqlite3
import os
from prettytable import PrettyTable


def adicionar_cliente(): 
        
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea\Banco_dados.db")
    cursor = conn.cursor()
        
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
    
def adicionar_voo(): 
        
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea\Banco_dados.db")
    cursor = conn.cursor()
        
    nome = input('Nome cliente: ')
    origem = input('Origem: ')
    destino = input('Destino: ')
    data_partida = input('Data de partida: ')
    data_chegada = input('Data de chegada: ')
    duracao = input('Duração: ')
        
    dados_voo = (nome, origem, destino, data_partida, data_chegada, duracao)
        
    cursor.execute('INSERT INTO clientes (nome, origem, destino, data_partida, data_chegada, duracao) VALUES (?,?,?,?)', dados_voo)
        
    conn.commit()
    print()
    input('Voo adicionado com sucesso. Pressione enter!')
    conn.close()
    
    
def adicionar_aeroporto(): 
        
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea\Banco_dados.db")
    cursor = conn.cursor()
        
    nome_aeroporto = input('Nome Aeroporto: ')
    codigo_iata = input('Codigo IATA: ')
    cidade = input('Cidade: ')
    pais = input('País: ')
        
    dados_aeroporto = (nome_aeroporto, codigo_iata, cidade, pais)
        
    cursor.execute('INSERT INTO clientes (nome_aeroporto, codigo_iata, cidade, pais) VALUES (?,?,?,?)', dados_aeroporto)
        
    conn.commit()
    print()
    input('Aeroporto adicionado com sucesso. Pressione enter!')
    conn.close()