# CAIXA DE TEXTO
As caixas de texto em PyQt são widgets que permitem aos usuários inserir e editar texto. Elas são essenciais para capturar dados de entrada do usuário, como nomes, senhas, descrições, entre outros, em interfaces gráficas de usuário (GUI).

## Conceito
Em PyQt, as caixas de texto são criadas usando a classe `QLineEdit` do módulo `QtWidgets`. Elas podem ser simples, para entrada de texto único, ou multilinhas (`QTextEdit`), para entrada de texto extenso.

## Exemplo de Código
Aqui está um exemplo simples que cria uma janela com uma caixa de texto usando `QLineEdit`:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Caixa de Texto com PyQt')
        self.setGeometry(100, 100, 400, 200)

        # Cria uma caixa de texto
        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.setGeometry(50, 50, 300, 30)  # Define posição e tamanho da caixa de texto

        # Cria um botão para capturar o texto
        botao = QPushButton('Capturar Texto', self)
        botao.setGeometry(150, 100, 100, 30)  # Define posição e tamanho do botão
        botao.clicked.connect(self.exibir_texto)

    def exibir_texto(self):
        texto = self.caixa_texto.text()
        print(f'Texto digitado: {texto}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- `import sys`: Importa o módulo `sys` para lidar com argumentos de linha de comando.
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget`: Importa as classes necessárias do módulo `QtWidgets` do PyQt5.
- `class MinhaJanela(QMainWindow):`: Define uma classe `MinhaJanela` que herda de `QMainWindow`.
- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).
- `self.setWindowTitle('Exemplo de Caixa de Texto com PyQt')`: Define o título da janela.
- `self.setGeometry(100, 100, 400, 200)`: Define a posição (100, 100) e o tamanho (400x200 pixels) da janela.

- `self.caixa_texto = QLineEdit(self)`: Cria um QLineEdit associado à janela `self`.
- `self.caixa_texto.setGeometry(50, 50, 300, 30)`: Define a posição (50, 50) e o tamanho (300x30 pixels) da caixa de texto dentro da janela.

- `botao = QPushButton('Capturar Texto', self)`: Cria um QPushButton com o texto 'Capturar Texto', associado à janela `self`.
- `botao.setGeometry(150, 100, 100, 30)`: Define a posição (150, 100) e o tamanho (100x30 pixels) do botão dentro da janela.
- `botao.clicked.connect(self.exibir_texto)`: Conecta o sinal `clicked` do botão à função `exibir_texto`.

- `def exibir_texto(self)`: Define a função `exibir_texto` que captura o texto da caixa de texto quando o botão é clicado.
- `texto = self.caixa_texto.text()`: Obtém o texto atual da caixa de texto usando o método `text()`.

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.
- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.
- `janela = MinhaJanela()`: Cria uma instância da classe `MinhaJanela`.
- `janela.show()`: Exibe a janela na tela.
- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

Este exemplo cria uma janela com uma caixa de texto onde o usuário pode digitar texto. Ao clicar no botão 'Capturar Texto', o texto digitado é exibido no console. 