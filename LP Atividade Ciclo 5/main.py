# -*- coding: utf-8 -*-

import sys
import sqlite3
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

Calculator = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Cálculo do IMC - Índice de Massa Corporal')
layout = QVBoxLayout()
button1 = QPushButton('Calcular')
button2 = QPushButton('Reniciar')
button3 = QPushButton('Sair')
button4 = QPushButton('Salvar Dados')
button5 = QPushButton('Mostrar Dados')
nome = QLineEdit()
endereco = QLineEdit()
altura = QLineEdit()
peso = QLineEdit()
label1 = QLabel('Nome do Paciente')
label2 = QLabel('Endereço Completo')
label3 = QLabel('Altura(Cm)')
label4 = QLabel('Peso(Kg)')
label5 = QLabel('Resultado')
imc = QLineEdit()

# Setando o Tamanho da Janela

window.setMinimumSize(450, 300)

# Configuração dos Labels

label1.setFont(QFont('Times', 12))
label1.setAlignment(Qt.AlignCenter)
label2.setFont(QFont('Times', 12))
label2.setAlignment(Qt.AlignCenter)
label3.setFont(QFont('Times', 12))
label3.setAlignment(Qt.AlignCenter)
label4.setFont(QFont('Times', 12))
label4.setAlignment(Qt.AlignCenter)
label5.setFont(QFont('Times', 12))
label5.setAlignment(Qt.AlignCenter)

# Configuração dos QLineEdits

nome.setFont(QFont('Times', 12))
endereco.setFont(QFont('Times', 12))
altura.setFont(QFont('Times', 12))
peso.setFont(QFont('Times', 12))
imc.setFont(QFont('Times', 12))

# Configuração dos Buttons

button1.setFont(QFont('Times', 12))
button2.setFont(QFont('Times', 12))
button3.setFont(QFont('Times', 12))
button4.setFont(QFont('Times', 12))
button5.setFont(QFont('Times', 12))

# Setando o Posicionamento dos Labels,QLineEdits e Buttons

layout.addWidget(label1)
layout.addWidget(nome)
layout.addWidget(label2)
layout.addWidget(endereco)
layout.addWidget(label3)
layout.addWidget(altura)
layout.addWidget(label4)
layout.addWidget(peso)
layout.addWidget(label5)
layout.addWidget(imc)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
layout.addWidget(button5)

# Desativa os Botões Reniciar,Salvar Dados e Mostrar Dados

button2.setEnabled(False)
button4.setEnabled(False)
button5.setEnabled(False)


# Calcular IMC

def CalcularIMC():
    h = float(altura.text())
    p = float(peso.text())
    r = (p / (h * h))
    f = str(r)
    imc.setText(f)

    button2.setEnabled(True)
    button4.setEnabled(True)
    button5.setEnabled(True)


# Limpar Campos

def Reniciar():
    nome.clear()
    endereco.clear()
    altura.clear()
    peso.clear()
    imc.clear()

    button2.setEnabled(False)
    button4.setEnabled(False)
    button5.setEnabled(False)


# Sai da aplicação

def Sair():
    sys.exit(Calculator.exec_())


# Inserção de Dados

def Inserir():
    conexao = sqlite3.connect('imc.db')
    cursor = conexao.cursor()

    sql = 'insert into tbl_Pessoas values (?,?,?,?,?)'

    recset = [(nome.text(), endereco.text(), altura.text(), peso.text(), imc.text())]

    for rec in recset:
        cursor.execute(sql, rec)

    conexao.commit()

    conexao.close()


# Mostrar Dados

def MostrarDados():
    button5 = QMessageBox.question(window, 'Mensagem', "Por Favor Verifique o Terminal para Mais Informações!",
                                   QMessageBox.Ok, )

    if button5 == QMessageBox.Ok:
        print('Banco de Dados:')

    conexao = sqlite3.connect('imc.db')
    cursor = conexao.cursor()

    cursor.execute('select * from tbl_Pessoas')
    mostrar = cursor.fetchall()
    print("\n".join(str(e) for e in mostrar))

    conexao.close()
    window.show()


button1.clicked.connect(CalcularIMC)
button2.clicked.connect(Reniciar)
button3.clicked.connect(Sair)
button4.clicked.connect(Inserir)
button5.clicked.connect(MostrarDados)

window.setLayout(layout)
window.show()
Calculator.exec()
