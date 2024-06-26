# JANELA
## Conceito de Janela em PyQt
Em PyQt, uma janela representa a interface gráfica principal de uma aplicação. É onde os widgets (elementos da interface como botões, caixas de texto, etc.) são colocados para interação com o usuário.

## Conceito
Uma janela em PyQt é criada usando a classe `QMainWindow` ou `QWidget`. A `QMainWindow` é usada geralmente como a janela principal de aplicativos mais complexos, enquanto `QWidget` pode ser usada para janelas menores ou componentes de interface dentro de uma janela maior.

## Exemplo de Código
Aqui está um exemplo simples que cria uma janela usando `QMainWindow`:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Janela com PyQt')
        self.setGeometry(100, 100, 400, 300)  # Define a posição e o tamanho da janela

        # Cria um QLabel para exibir texto na janela
        label = QLabel('Esta é uma janela PyQt!', self)
        label.move(50, 50)  # Define a posição do QLabel dentro da janela
        label.adjustSize()  # Ajusta o tamanho do QLabel conforme necessário

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- `import sys`: Importa o módulo `sys` para lidar com argumentos de linha de comando.
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel`: Importa as classes necessárias do módulo `QtWidgets` do PyQt5.
- `class MinhaJanela(QMainWindow):`: Define uma classe `MinhaJanela` que herda de `QMainWindow`.
- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).
- `self.setWindowTitle('Exemplo de Janela com PyQt')`: Define o título da janela.
- `self.setGeometry(100, 100, 400, 300)`: Define a posição (100, 100) e o tamanho (400x300 pixels) da janela.
- `label = QLabel('Esta é uma janela PyQt!', self)`: Cria um QLabel com o texto especificado, associado à janela `self`.
- `label.move(50, 50)`: Define a posição inicial do QLabel dentro da janela.
- `label.adjustSize()`: Ajusta o tamanho do QLabel conforme necessário com base no texto.

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.
- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.
- `janela = MinhaJanela()`: Cria uma instância da classe `MinhaJanela`.
- `janela.show()`: Exibe a janela na tela.
- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

