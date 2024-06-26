from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

def exibir_mensagem():
    dado_lido = caixa_mensagem.lineEdit.text()
    print(dado_lido)
    caixa_mensagem.lineEdit.setText("")

    if dado_lido == "":
        QMessageBox.about(caixa_mensagem, "Alerta","Nenhum nome digitado")
    else:
        QMessageBox.about(caixa_mensagem, "Alerta","Ola: "+dado_lido)

app=QtWidgets.QApplication([])
caixa_mensagem=uic.loadUi("caixa_mensagem.ui")
caixa_mensagem.pushButton.clicked.connect(exibir_mensagem)

caixa_mensagem.show()
app.exec()