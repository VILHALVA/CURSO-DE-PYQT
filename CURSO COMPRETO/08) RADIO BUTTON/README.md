# RADIO BUTTON
Os radio buttons, ou botões de opção, em PyQt são widgets que permitem ao usuário selecionar exatamente uma opção de um grupo de opções mutuamente exclusivas. Eles são úteis para apresentar escolhas onde apenas uma opção pode ser selecionada por vez.

## Conceito
Em PyQt, os radio buttons são criados usando a classe `QRadioButton` do módulo `QtWidgets`. Eles são organizados em grupos usando `QButtonGroup` para garantir que apenas um botão de opção possa ser selecionado por vez dentro do grupo.

## Exemplo de Código
Aqui está um exemplo simples que cria uma janela com radio buttons usando `QRadioButton`:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Radio Button com PyQt')
        self.setGeometry(100, 100, 400, 200)

        # Layout principal da janela
        layout_principal = QVBoxLayout()

        # Label para exibir a seleção
        self.label_selecao = QLabel('Nenhuma opção selecionada')
        layout_principal.addWidget(self.label_selecao)

        # Grupo de radio buttons
        grupo_botoes = QHBoxLayout()

        # Radio buttons
        self.radio1 = QRadioButton('Opção 1')
        self.radio1.setChecked(False)  # Define se está selecionado ou não
        self.radio1.toggled.connect(lambda: self.atualizar_label(self.radio1))

        self.radio2 = QRadioButton('Opção 2')
        self.radio2.setChecked(False)  # Define se está selecionado ou não
        self.radio2.toggled.connect(lambda: self.atualizar_label(self.radio2))

        grupo_botoes.addWidget(self.radio1)
        grupo_botoes.addWidget(self.radio2)

        # Adiciona o grupo de radio buttons ao layout principal
        layout_principal.addLayout(grupo_botoes)

        # Widget central da janela
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    def atualizar_label(self, botao):
        if botao.isChecked():
            self.label_selecao.setText(f'Opção selecionada: {botao.text()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- `import sys`: Importa o módulo `sys` para lidar com argumentos de linha de comando.
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout`: Importa as classes necessárias do módulo `QtWidgets` do PyQt5.
- `class MinhaJanela(QMainWindow):`: Define uma classe `MinhaJanela` que herda de `QMainWindow`.
- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).
- `self.setWindowTitle('Exemplo de Radio Button com PyQt')`: Define o título da janela.
- `self.setGeometry(100, 100, 400, 200)`: Define a posição (100, 100) e o tamanho (400x200 pixels) da janela.

- `layout_principal = QVBoxLayout()`: Cria um layout vertical para organizar os widgets na janela.

- `self.label_selecao = QLabel('Nenhuma opção selecionada')`: Cria um QLabel inicializado com um texto padrão.
- `layout_principal.addWidget(self.label_selecao)`: Adiciona o QLabel ao layout principal.

- `grupo_botoes = QHBoxLayout()`: Cria um layout horizontal para os radio buttons.

- `self.radio1 = QRadioButton('Opção 1')`: Cria o primeiro QRadioButton com o texto 'Opção 1'.
- `self.radio1.setChecked(False)`: Define se o radio button está selecionado ou não inicialmente.
- `self.radio1.toggled.connect(lambda: self.atualizar_label(self.radio1))`: Conecta o sinal `toggled` do radio button ao método `atualizar_label`.

- `self.radio2 = QRadioButton('Opção 2')`: Cria o segundo QRadioButton com o texto 'Opção 2'.
- `self.radio2.setChecked(False)`: Define se o radio button está selecionado ou não inicialmente.
- `self.radio2.toggled.connect(lambda: self.atualizar_label(self.radio2))`: Conecta o sinal `toggled` do radio button ao método `atualizar_label`.

- `grupo_botoes.addWidget(self.radio1)`: Adiciona o primeiro radio button ao layout horizontal.
- `grupo_botoes.addWidget(self.radio2)`: Adiciona o segundo radio button ao layout horizontal.

- `layout_principal.addLayout(grupo_botoes)`: Adiciona o layout horizontal (grupo de radio buttons) ao layout vertical principal.

- `widget_central = QWidget()`: Cria um widget central para a janela.
- `widget_central.setLayout(layout_principal)`: Define o layout principal como o layout do widget central.
- `self.setCentralWidget(widget_central)`: Define o widget central da janela como o widget `widget_central`.

- `def atualizar_label(self, botao)`: Define o método `atualizar_label` que atualiza o texto do QLabel quando um radio button é selecionado.
- `if botao.isChecked()`: Verifica se o botão foi selecionado.
- `self.label_selecao.setText(f'Opção selecionada: {botao.text()}')`: Define o texto do QLabel para mostrar qual opção foi selecionada.

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.
- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.
- `janela = MinhaJanela()`: Cria uma instância da classe `MinhaJanela`.
- `janela.show()`: Exibe a janela na tela.
- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

Este exemplo cria uma janela com dois radio buttons onde apenas um pode ser selecionado por vez. Quando um radio button é selecionado, o texto correspondente é exibido em um QLabel na janela. 