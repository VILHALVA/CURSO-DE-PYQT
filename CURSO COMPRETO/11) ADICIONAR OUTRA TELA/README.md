# ADICIONAR OUTRA TELA
Para adicionar outra tela em uma aplicação PyQt, geralmente utilizamos múltiplas instâncias de `QMainWindow` ou `QDialog`, dependendo da complexidade e da necessidade de interação entre as telas. Vou mostrar um exemplo simples de como criar duas janelas distintas e alternar entre elas:

## Exemplo de Adição de Outra Tela em PyQt
Neste exemplo, vamos criar duas janelas (`JanelaPrincipal` e `SegundaJanela`) e um botão na `JanelaPrincipal` para alternar entre elas.

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class SegundaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Segunda Janela')
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        # Exemplo de conteúdo na segunda janela
        texto_label = QLabel('Esta é a Segunda Janela')
        layout.addWidget(texto_label)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Janela Principal')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        botao_nova_janela = QPushButton('Abrir Segunda Janela')
        botao_nova_janela.clicked.connect(self.abrir_segunda_janela)
        layout.addWidget(botao_nova_janela)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

    def abrir_segunda_janela(self):
        self.segunda_janela = SegundaJanela()
        self.segunda_janela.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela_principal = JanelaPrincipal()
    janela_principal.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- `import sys`: Importa o módulo `sys` para lidar com argumentos de linha de comando.
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget`: Importa as classes necessárias do módulo `QtWidgets` do PyQt5.

- `class SegundaJanela(QMainWindow)`: Define uma classe `SegundaJanela` que herda de `QMainWindow`. Esta é nossa segunda tela.

- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).

- `self.setWindowTitle('Segunda Janela')`: Define o título da segunda janela.

- `self.setGeometry(200, 200, 400, 200)`: Define a posição (200, 200) e o tamanho (400x200 pixels) da segunda janela.

- `layout = QVBoxLayout()`: Cria um layout vertical para organizar os widgets na segunda janela.

- `texto_label = QLabel('Esta é a Segunda Janela')`: Cria um QLabel com texto na segunda janela.

- `layout.addWidget(texto_label)`: Adiciona o QLabel ao layout vertical.

- `widget_central = QWidget()`: Cria um widget central para a segunda janela.

- `widget_central.setLayout(layout)`: Define o layout vertical como o layout do widget central.

- `self.setCentralWidget(widget_central)`: Define o widget central da segunda janela como o widget `widget_central`.

- `class JanelaPrincipal(QMainWindow)`: Define uma classe `JanelaPrincipal` que herda de `QMainWindow`. Esta é nossa janela principal.

- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).

- `self.setWindowTitle('Janela Principal')`: Define o título da janela principal.

- `self.setGeometry(100, 100, 400, 200)`: Define a posição (100, 100) e o tamanho (400x200 pixels) da janela principal.

- `layout = QVBoxLayout()`: Cria um layout vertical para organizar os widgets na janela principal.

- `botao_nova_janela = QPushButton('Abrir Segunda Janela')`: Cria um QPushButton com o texto 'Abrir Segunda Janela'.

- `botao_nova_janela.clicked.connect(self.abrir_segunda_janela)`: Conecta o sinal `clicked` do botão ao método `abrir_segunda_janela`, que será chamado quando o botão for clicado.

- `layout.addWidget(botao_nova_janela)`: Adiciona o QPushButton ao layout vertical.

- `widget_central = QWidget()`: Cria um widget central para a janela principal.

- `widget_central.setLayout(layout)`: Define o layout vertical como o layout do widget central.

- `self.setCentralWidget(widget_central)`: Define o widget central da janela principal como o widget `widget_central`.

- `def abrir_segunda_janela(self)`: Define o método `abrir_segunda_janela`, que cria e exibe a segunda janela quando o botão é clicado.

- `self.segunda_janela = SegundaJanela()`: Cria uma instância da classe `SegundaJanela`.

- `self.segunda_janela.show()`: Exibe a segunda janela.

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.

- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.

- `janela_principal = JanelaPrincipal()`: Cria uma instância da classe `JanelaPrincipal`.

- `janela_principal.show()`: Exibe a janela principal na tela.

- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

Este exemplo mostra como criar uma segunda janela (`SegundaJanela`) e alternar entre ela e a janela principal (`JanelaPrincipal`) ao clicar em um botão na janela principal.