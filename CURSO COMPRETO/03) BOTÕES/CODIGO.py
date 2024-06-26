import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        ### ATRIBUTOS
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        ### OBJETO
        ## Botao e uma instancia da classe QPushButton
        botao1 = QPushButton('Botao 1', self)
        botao1.move(150,200) # distancia em pixel esquerda, distacia a altura
        botao1.resize(150,80) # largura, altura
        botao1.setStyleSheet('QPushButton {background-color: #0FB328; font:bold; font-size:20px}')
        botao1.clicked.connect(self.botao1_click)

        ## Botao e uma instancia da classe QPushButton
        botao2 = QPushButton('Botao 2', self)
        botao2.move(350,200) # distancia em pixel esquerda, distacia a altura
        botao2.resize(150,80) # largura, altura
        botao2.setStyleSheet('QPushButton {background-color: #0FB328; font:bold; font-size:20px}')
        botao2.clicked.connect(self.botao2_click)

        #METODO
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        print('O Botao 1 foi clicado!!!!')
    
    def botao2_click(self):
        print('O Botao 2 foi clicado!!!!')

aplicacao = QApplication(sys.argv) # para que possamos mexer nos parametros os sistema (fechar janela)
j = Janela()
sys.exit(aplicacao.exec_())