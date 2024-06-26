from PyQt5 import uic, QtWidgets

def salvar():
    nome =tela.lineEdit.text()
    idade = tela.lineEdit_2.text()
    tel = tela.lineEdit_3.text()
    dados = "Nome: " + nome + " Idade: " + idade + " Telefone: " + tel 

    arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]
    #print(arquivo)
    with open (arquivo + '.txt', 'w') as a:
        a.write(dados)


app=QtWidgets.QApplication([])
tela = uic.loadUi("menu_salvar.ui")

tela.actionSalvar.triggered.connect(salvar)

tela.show()
app.exec()