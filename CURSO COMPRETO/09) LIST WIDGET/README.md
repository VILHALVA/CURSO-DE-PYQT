# LIST WIDGET
O List Widget em PyQt é um widget que exibe uma lista de itens que o usuário pode selecionar. Ele fornece uma maneira conveniente de exibir itens em uma lista, onde cada item pode ter texto e/ou ícones associados. Os List Widgets são úteis para apresentar listas de itens selecionáveis, permitindo interações como seleção única, múltipla ou arrastar e soltar.

## Exemplo de Código
Aqui está um exemplo básico que cria uma janela com um List Widget contendo alguns itens:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QVBoxLayout, QWidget

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de List Widget com PyQt')
        self.setGeometry(100, 100, 400, 300)

        # Layout principal da janela
        layout_principal = QVBoxLayout()

        # List Widget
        self.list_widget = QListWidget()
        self.list_widget.addItem('Item 1')
        self.list_widget.addItem('Item 2')
        self.list_widget.addItem('Item 3')
        self.list_widget.addItem('Item 4')
        self.list_widget.addItem('Item 5')
        self.list_widget.itemClicked.connect(self.item_clicado)  # Conecta o sinal itemClicked ao método item_clicado

        layout_principal.addWidget(self.list_widget)

        # Widget central da janela
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    def item_clicado(self, item):
        print(f'Item clicado: {item.text()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- `import sys`: Importa o módulo `sys` para lidar com argumentos de linha de comando.
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QVBoxLayout, QWidget`: Importa as classes necessárias do módulo `QtWidgets` do PyQt5.

- `class MinhaJanela(QMainWindow):`: Define uma classe `MinhaJanela` que herda de `QMainWindow`.

- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).

- `self.setWindowTitle('Exemplo de List Widget com PyQt')`: Define o título da janela.

- `self.setGeometry(100, 100, 400, 300)`: Define a posição (100, 100) e o tamanho (400x300 pixels) da janela.

- `layout_principal = QVBoxLayout()`: Cria um layout vertical para organizar os widgets na janela.

- `self.list_widget = QListWidget()`: Cria um QListWidget para exibir a lista de itens.

- `self.list_widget.addItem('Item 1')`: Adiciona itens à QListWidget usando o método `addItem`.

- `self.list_widget.itemClicked.connect(self.item_clicado)`: Conecta o sinal `itemClicked` da QListWidget ao método `item_clicado`, que será chamado quando um item da lista for clicado.

- `layout_principal.addWidget(self.list_widget)`: Adiciona o QListWidget ao layout principal.

- `widget_central = QWidget()`: Cria um widget central para a janela.

- `widget_central.setLayout(layout_principal)`: Define o layout principal como o layout do widget central.

- `self.setCentralWidget(widget_central)`: Define o widget central da janela como o widget `widget_central`.

- `def item_clicado(self, item)`: Define o método `item_clicado`, que será chamado quando um item da lista for clicado.

- `print(f'Item clicado: {item.text()}')`: Exibe o texto do item clicado no console.

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.

- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.

- `janela = MinhaJanela()`: Cria uma instância da classe `MinhaJanela`.

- `janela.show()`: Exibe a janela na tela.

- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

Este exemplo cria uma janela com um List Widget contendo cinco itens. Quando um item da lista é clicado, o texto desse item é exibido no console.