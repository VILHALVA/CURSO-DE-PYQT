# BOTÕES
Os botões em PyQt são widgets usados para permitir interações do usuário, como acionar ações, enviar dados ou realizar operações específicas quando clicados. Eles são fundamentais para tornar uma interface gráfica interativa e funcional.

## Conceito
Em PyQt, os botões são criados usando a classe `QPushButton` do módulo `QtWidgets`. Eles podem exibir texto, ícones ou ambos e podem ser conectados a funções para executar tarefas específicas quando clicados.

## Exemplo de Código
Aqui está um exemplo simples que cria uma janela com um botão usando `QPushButton`:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Botão com PyQt')
        self.setGeometry(100, 100, 400, 300)

        # Cria um botão na janela
        botao = QPushButton('Clique Aqui', self)
        botao.setGeometry(150, 150, 100, 50)  # Define posição e tamanho do botão

        # Conecta o clique do botão a uma função
        botao.clicked.connect(self.mostrar_mensagem)

    def mostrar_mensagem(self):
        QMessageBox.information(self, 'Mensagem', 'Botão foi clicado!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- `import sys`: Importa o módulo `sys` para lidar com argumentos de linha de comando.
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox`: Importa as classes necessárias do módulo `QtWidgets` do PyQt5.
- `class MinhaJanela(QMainWindow):`: Define uma classe `MinhaJanela` que herda de `QMainWindow`.
- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).
- `self.setWindowTitle('Exemplo de Botão com PyQt')`: Define o título da janela.
- `self.setGeometry(100, 100, 400, 300)`: Define a posição (100, 100) e o tamanho (400x300 pixels) da janela.
- `botao = QPushButton('Clique Aqui', self)`: Cria um QPushButton com o texto 'Clique Aqui', associado à janela `self`.
- `botao.setGeometry(150, 150, 100, 50)`: Define a posição (150, 150) e o tamanho (100x50 pixels) do botão dentro da janela.
- `botao.clicked.connect(self.mostrar_mensagem)`: Conecta o sinal `clicked` do botão à função `mostrar_mensagem`.

- `def mostrar_mensagem(self)`: Define a função `mostrar_mensagem` que exibe uma caixa de mensagem quando o botão é clicado.
- `QMessageBox.information(self, 'Mensagem', 'Botão foi clicado!')`: Exibe uma caixa de mensagem informativa com o título 'Mensagem' e o texto 'Botão foi clicado!'.

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.
- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.
- `janela = MinhaJanela()`: Cria uma instância da classe `MinhaJanela`.
- `janela.show()`: Exibe a janela na tela.
- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

Este exemplo cria uma janela com um botão que, quando clicado, exibe uma mensagem informativa. Você pode expandir este código adicionando mais botões e conectando-os a diferentes funções para realizar diversas operações na sua aplicação PyQt.