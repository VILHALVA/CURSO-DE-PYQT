from cProfile import label
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        ### ATRIBUTOS
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"
        #
        ## Caixa de texto
        self.caixa_texto = QLineEdit(self)                        #caixa de texto
        self.caixa_texto.move(20,10)
        self.caixa_texto.resize(250,30)


        ### OBJETO
        ## Botao e uma instancia da classe QPushButton
        botao1 = QPushButton('Botao 1', self)
        botao1.move(150,200) # distancia em pixel esquerda, distacia a altura
        botao1.resize(150,80) # largura, altura
        botao1.setStyleSheet('QPushButton {background-color: #696969; font:bold; font-size:20px}')
        botao1.clicked.connect(self.botao1_click)

        ## Botao Caixa
        botao_caixa = QPushButton('Enviar Texto', self)
        botao_caixa.move(550,200) # distancia em pixel esquerda, distacia a altura
        botao_caixa.resize(150,80) # largura, altura
        botao_caixa.setStyleSheet('QPushButton {background-color: #008000; font:bold; font-size:20px}')
        botao_caixa.clicked.connect(self.mostra_texto)

        ## Botao e uma instancia da classe QPushButton
        botao2 = QPushButton('Botao 2', self)
        botao2.move(350,200) # distancia em pixel esquerda, distacia a altura
        botao2.resize(150,80) # largura, altura
        botao2.setStyleSheet('QPushButton {background-color: #0000FF ; font:bold; font-size:20px}')
        botao2.clicked.connect(self.botao2_click)

        #labels
        self.label_1 = QLabel(self)
        self.label_1.move(50,50)
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color:"red"}')
        self.label_1.resize(400,25)
        self.label_1.setText("Aperte um Botao!!!")

        self.label_caixa = QLabel(self)
        self.label_caixa.move(375,50)
        self.label_caixa.setStyleSheet('QLabel {font:bold; font-size:25px; color:"black"}')
        self.label_caixa.resize(400,30)
        self.label_caixa.setText("Digitou: ")

        ## IMGEM Label
        self.carro = QLabel(self)
        self.carro.move(50,300)
        self.carro.setPixmap(QtGui.QPixmap('carro1.png'))
        self.carro.resize(300,300)


        #METODO
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        #print('O Botao 1 foi clicado!!!!')
        self.label_1.setText("O carro 1 foi selecionado")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color:"black"}')
        self.carro.setPixmap(QtGui.QPixmap('carro1.png'))
    
    def mostra_texto(self):
        conteudo = self.caixa_texto.text()
        self.label_caixa.setText("Digitou: " + conteudo)

    def botao2_click(self):
        #print('O Botao 2 foi clicado!!!!')
        self.label_1.setText("O carro 2 foi selecionado")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color:"blue"}')
        self.carro.setPixmap(QtGui.QPixmap('carro2.png'))
    

aplicacao = QApplication(sys.argv) # para que possamos mexer nos parametros os sistema (fechar janela)
j = Janela()
sys.exit(aplicacao.exec_())