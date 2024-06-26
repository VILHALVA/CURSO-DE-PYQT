from PyQt5 import uic, QtWidgets


def frame1():
    tela.frame_2.close()

def frame2():
    tela.frame_2.show()

app=QtWidgets.QApplication([])
tela=uic.loadUi("frame.ui")

tela.pushButton_2.clicked.connect(frame1)
tela.pushButton_3.clicked.connect(frame2)
tela.show()
app.exec()