from PyQt5 import uic,QtWidgets


def pegar_data():
    data = str(primeira_tela.calendarWidget.selectedDate())
    data_formatada = data[19:30]
    primeira_tela.label.setText("Data selecionada: " + data_formatada)



app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("tela_calendario.ui")

primeira_tela.calendarWidget.selectionChanged.connect(pegar_data)
primeira_tela.show()
app.exec()