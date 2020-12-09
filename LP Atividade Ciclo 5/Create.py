# -*- coding: utf-8 -*-

import sqlite3

conexao = sqlite3.connect('imc.db')
cursor = conexao.cursor()

#Criação Tabela Pessoas

sql = 'Create table tbl_Pessoas (Nome varchar(30), Endereco varchar(30), Altura decimal(5,3), Peso decimal(5,3),' \
      'ResutImc decimal(5,3)) '

cursor.execute(sql)
conexao.close()

print("Banco de Dados Criado com Sucesso!")
