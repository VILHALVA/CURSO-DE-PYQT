from PyQt5 import uic,QtWidgets

def menu_verde():
    tela.label_2.setText("Verde")
    tela.label_2.setStyleSheet("color: green")

def menu_azul():
    tela.label_2.setText("Azul")
    tela.label_2.setStyleSheet("color: blue")

def menu_verde():
    tela.label_2.setText("Verde")
    tela.label_2.setStyleSheet("color: green")

def menu_vermelho():
    tela.label_2.setText("Vermelho")
    tela.label_2.setStyleSheet("color: red")

app=QtWidgets.QApplication([])
tela=uic.loadUi("menu.ui")

tela.actionVerde.triggered.connect(menu_verde)
tela.actionAzul.triggered.connect(menu_azul)
tela.actionVermelho.triggered.connect(menu_vermelho)
tela.show()
app.exec()