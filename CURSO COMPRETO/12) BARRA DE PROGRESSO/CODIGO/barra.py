from PyQt5 import uic, QtWidgets

valor =0

def incrementa_valor():
    global valor
    valor = valor + 10
    barra.progressBar.setValue(valor)
    #print(valor)

def zerar_valor():
    #print("funcao 2")
    global valor
    valor = 0
    barra.progressBar.setValue(valor)

app=QtWidgets.QApplication([])
barra=uic.loadUi("barra_progresso.ui")
barra.pushButton.clicked.connect(incrementa_valor)
barra.pushButton_2.clicked.connect(zerar_valor)

barra.show()
app.exec()