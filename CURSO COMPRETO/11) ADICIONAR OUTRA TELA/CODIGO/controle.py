from PyQt5 import uic,QtWidgets

def chama_segunda_tela():
    segunda_tela.show()
    segunda_tela.label.setText("Vilhalva!!!")

app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
segunda_tela=uic.loadUi("segunda_tela.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)

primeira_tela.show()
app.exec()