from PyQt5 import uic, QtWidgets

def funcao_principal():
    if formulario.radioButton.isChecked():
        #print("opcao 1 selecionada")
        opcao = "opcao 1 selecionada"
    elif formulario.radioButton_2.isChecked():
        #print("opcao 2 selecionada")
        opcao = "opcao 2 selecionada"
    elif formulario.radioButton_3.isChecked():
        #print("opcao 3 selecionada")
        opcao = "opcao 3 selecionada"
    elif formulario.radioButton_4.isChecked():
        #print("opcao 4 selecionada")
        opcao = "opcao 4 selecionada"
    else:
        #print("")
        opcao = ""

    formulario.label_2.setText(opcao)

app=QtWidgets.QApplication([])
formulario=uic.loadUi("janela.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()