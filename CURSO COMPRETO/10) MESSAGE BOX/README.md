# MESSAGE BOX
As Message Boxes em PyQt são utilizadas para exibir mensagens temporárias ao usuário, como avisos, confirmações ou mensagens informativas. Elas permitem interações básicas com o usuário através de botões, como "OK", "Cancelar", "Sim", "Não", entre outros. As Message Boxes são úteis para comunicar informações importantes ou solicitar ações específicas do usuário durante a execução de uma aplicação.

## Exemplo de Código
Aqui está um exemplo simples que cria uma janela com um botão que, ao ser clicado, exibe uma Message Box com uma mensagem informativa:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Message Box com PyQt')
        self.setGeometry(100, 100, 400, 200)

        # Layout principal da janela
        layout_principal = QVBoxLayout()

        # Botão para exibir a Message Box
        botao_exibir = QPushButton('Exibir Message Box')
        botao_exibir.clicked.connect(self.exibir_message_box)

        layout_principal.addWidget(botao_exibir)

        # Widget central da janela
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    def exibir_message_box(self):
        # Cria uma instância de QMessageBox
        mensagem_box = QMessageBox()
        mensagem_box.setWindowTitle('Message Box PyQt')
        mensagem_box.setText('Exemplo de Message Box com PyQt.')
        mensagem_box.setIcon(QMessageBox.Information)
        mensagem_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mensagem_box.setDefaultButton(QMessageBox.Ok)

        # Exibe a Message Box e espera pela resposta do usuário
        resposta = mensagem_box.exec()

        if resposta == QMessageBox.Ok:
            print('Usuário clicou em OK.')
        elif resposta == QMessageBox.Cancel:
            print('Usuário clicou em Cancelar.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- `import sys`: Importa o módulo `sys` para lidar com argumentos de linha de comando.
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget`: Importa as classes necessárias do módulo `QtWidgets` do PyQt5.

- `class MinhaJanela(QMainWindow):`: Define uma classe `MinhaJanela` que herda de `QMainWindow`.

- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).

- `self.setWindowTitle('Exemplo de Message Box com PyQt')`: Define o título da janela.

- `self.setGeometry(100, 100, 400, 200)`: Define a posição (100, 100) e o tamanho (400x200 pixels) da janela.

- `layout_principal = QVBoxLayout()`: Cria um layout vertical para organizar os widgets na janela.

- `botao_exibir = QPushButton('Exibir Message Box')`: Cria um QPushButton com o texto 'Exibir Message Box'.

- `botao_exibir.clicked.connect(self.exibir_message_box)`: Conecta o sinal `clicked` do botão ao método `exibir_message_box`, que será chamado quando o botão for clicado.

- `layout_principal.addWidget(botao_exibir)`: Adiciona o QPushButton ao layout vertical principal.

- `widget_central = QWidget()`: Cria um widget central para a janela.

- `widget_central.setLayout(layout_principal)`: Define o layout principal como o layout do widget central.

- `self.setCentralWidget(widget_central)`: Define o widget central da janela como o widget `widget_central`.

- `def exibir_message_box(self):`: Define o método `exibir_message_box`, que cria e exibe a Message Box quando o botão é clicado.

- `mensagem_box = QMessageBox()`: Cria uma instância de `QMessageBox`.

- `mensagem_box.setWindowTitle('Message Box PyQt')`: Define o título da Message Box.

- `mensagem_box.setText('Exemplo de Message Box com PyQt.')`: Define o texto exibido na Message Box.

- `mensagem_box.setIcon(QMessageBox.Information)`: Define o ícone exibido na Message Box como informativo.

- `mensagem_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)`: Define os botões padrão da Message Box como OK e Cancelar.

- `mensagem_box.setDefaultButton(QMessageBox.Ok)`: Define o botão padrão (botão que é pressionado ao pressionar Enter) como OK.

- `resposta = mensagem_box.exec()`: Exibe a Message Box e aguarda a resposta do usuário.

- `if resposta == QMessageBox.Ok:`: Verifica se o usuário clicou no botão OK.

- `print('Usuário clicou em OK.')`: Exibe uma mensagem no console se o usuário clicou em OK.

- `elif resposta == QMessageBox.Cancel:`: Verifica se o usuário clicou no botão Cancelar.

- `print('Usuário clicou em Cancelar.')`: Exibe uma mensagem no console se o usuário clicou em Cancelar.

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.

- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.

- `janela = MinhaJanela()`: Cria uma instância da classe `MinhaJanela`.

- `janela.show()`: Exibe a janela na tela.

- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

Este exemplo cria uma janela com um botão "Exibir Message Box". Quando o botão é clicado, uma Message Box é exibida com um texto informativo e botões OK e Cancelar. Dependendo do botão clicado pelo usuário, uma mensagem correspondente é exibida no console.