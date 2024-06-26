from PyQt5 import uic, QtWidgets

def opcao_selecionada():
    cidade = tela.comboBox.currentText()
    tela.label_2.setText("Cidade: " + cidade)



app=QtWidgets.QApplication([])
tela=uic.loadUi("combobox.ui")

tela.comboBox.addItems(["Sao Paulo", "Rio de Janeiro","Curitiba","Sorocaba"])
tela.pushButton.clicked.connect(opcao_selecionada)

tela.show()
app.exec()