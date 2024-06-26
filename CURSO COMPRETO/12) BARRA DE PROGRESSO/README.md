# BARRA DE PROGRESSO
Para implementar uma barra de progresso em uma aplicação PyQt, podemos usar o widget `QProgressBar` fornecido pelo módulo `QtWidgets`. A barra de progresso é útil para indicar visualmente o progresso de uma operação em andamento para o usuário. Abaixo está um exemplo simples de como adicionar e utilizar uma barra de progresso em PyQt:

## Exemplo de Barra de Progresso em PyQt
Neste exemplo, vamos criar uma janela com uma barra de progresso e um botão que simula o progresso de uma tarefa.

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QTimer

class JanelaProgresso(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Barra de Progresso')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.barra_progresso = QProgressBar()
        self.barra_progresso.setRange(0, 100)  # Define o intervalo da barra de progresso
        self.barra_progresso.setValue(0)       # Define o valor inicial da barra de progresso
        layout.addWidget(self.barra_progresso)

        self.botao_iniciar = QPushButton('Iniciar Progresso')
        self.botao_iniciar.clicked.connect(self.iniciar_progresso)
        layout.addWidget(self.botao_iniciar)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar_progresso)
        self.progresso = 0

    def iniciar_progresso(self):
        self.progresso = 0
        self.timer.start(100)  # Inicia o timer para atualizar o progresso a cada 100ms

    def atualizar_progresso(self):
        self.progresso += 1
        self.barra_progresso.setValue(self.progresso)

        if self.progresso >= 100:
            self.timer.stop()
            self.botao_iniciar.setText('Progresso Concluído')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = JanelaProgresso()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- `import sys`: Importa o módulo `sys` para lidar com argumentos de linha de comando.
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QProgressBar`: Importa as classes necessárias do módulo `QtWidgets` do PyQt5, incluindo `QProgressBar` para a barra de progresso.
- `from PyQt5.QtCore import QTimer`: Importa `QTimer` do módulo `QtCore` do PyQt5 para atualizar o progresso automaticamente.

- `class JanelaProgresso(QMainWindow)`: Define uma classe `JanelaProgresso` que herda de `QMainWindow`.

- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).

- `self.setWindowTitle('Exemplo de Barra de Progresso')`: Define o título da janela.

- `self.setGeometry(100, 100, 400, 200)`: Define a posição (100, 100) e o tamanho (400x200 pixels) da janela.

- `layout = QVBoxLayout()`: Cria um layout vertical para organizar os widgets na janela.

- `self.barra_progresso = QProgressBar()`: Cria uma instância de `QProgressBar`.

- `self.barra_progresso.setRange(0, 100)`: Define o intervalo da barra de progresso de 0 a 100.

- `self.barra_progresso.setValue(0)`: Define o valor inicial da barra de progresso como 0.

- `layout.addWidget(self.barra_progresso)`: Adiciona a barra de progresso ao layout vertical.

- `self.botao_iniciar = QPushButton('Iniciar Progresso')`: Cria um QPushButton com o texto 'Iniciar Progresso'.

- `self.botao_iniciar.clicked.connect(self.iniciar_progresso)`: Conecta o sinal `clicked` do botão ao método `iniciar_progresso`, que será chamado quando o botão for clicado.

- `layout.addWidget(self.botao_iniciar)`: Adiciona o botão ao layout vertical.

- `widget_central = QWidget()`: Cria um widget central para a janela.

- `widget_central.setLayout(layout)`: Define o layout vertical como o layout do widget central.

- `self.setCentralWidget(widget_central)`: Define o widget central da janela como o widget `widget_central`.

- `self.timer = QTimer(self)`: Cria uma instância de `QTimer` para atualizar o progresso.

- `self.timer.timeout.connect(self.atualizar_progresso)`: Conecta o sinal `timeout` do timer ao método `atualizar_progresso`, que será chamado a cada intervalo de tempo.

- `self.progresso = 0`: Inicializa a variável `progresso` com 0.

- `def iniciar_progresso(self)`: Define o método `iniciar_progresso`, que é chamado quando o botão é clicado para iniciar o progresso.

- `self.progresso = 0`: Reseta o progresso para 0.

- `self.timer.start(100)`: Inicia o timer para atualizar o progresso a cada 100 milissegundos.

- `def atualizar_progresso(self)`: Define o método `atualizar_progresso`, que é chamado periodicamente pelo timer para atualizar a barra de progresso.

- `self.progresso += 1`: Incrementa o progresso.

- `self.barra_progresso.setValue(self.progresso)`: Atualiza o valor da barra de progresso com o valor atual de `progresso`.

- `if self.progresso >= 100:`: Verifica se o progresso atingiu 100%.

- `self.timer.stop()`: Para o timer.

- `self.botao_iniciar.setText('Progresso Concluído')`: Altera o texto do botão para indicar que o progresso foi concluído.

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.

- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.

- `janela = JanelaProgresso()`: Cria uma instância da classe `JanelaProgresso`.

- `janela.show()`: Exibe a janela na tela.

- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

Este exemplo cria uma janela com uma barra de progresso e um botão. Ao clicar no botão "Iniciar Progresso", a barra de progresso começa a preencher até atingir 100%. 