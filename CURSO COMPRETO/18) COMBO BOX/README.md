# COMBO BOX
Para adicionar uma ComboBox (caixa de seleção suspensa) em uma aplicação PyQt, você pode seguir o exemplo abaixo. ComboBoxes são utilizadas quando o usuário precisa escolher uma opção a partir de uma lista suspensa de opções disponíveis.

## Exemplo de Uso de ComboBox em PyQt
Neste exemplo, criaremos uma janela principal (`QMainWindow`) com uma ComboBox que permite ao usuário selecionar uma opção de uma lista predefinida. Vamos capturar o evento de seleção para exibir a opção selecionada.

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox

class JanelaComboBox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de ComboBox')
        self.setGeometry(100, 100, 400, 200)

        # Criando um layout vertical para a janela principal
        layout_principal = QVBoxLayout()

        # Criando uma label para exibir a seleção da ComboBox
        self.label_selecao = QLabel('Selecione uma opção:', self)
        layout_principal.addWidget(self.label_selecao)

        # Criando a ComboBox com opções
        self.combobox = QComboBox(self)
        self.combobox.addItem('Opção 1')
        self.combobox.addItem('Opção 2')
        self.combobox.addItem('Opção 3')
        self.combobox.addItem('Opção 4')
        self.combobox.currentIndexChanged.connect(self.mostrar_selecao)
        layout_principal.addWidget(self.combobox)

        # Criando um widget central para a janela principal e aplicando o layout
        widget_central = QWidget(self)
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    def mostrar_selecao(self, index):
        # Obtém o texto da opção selecionada na ComboBox
        opcao_selecionada = self.combobox.currentText()
        self.label_selecao.setText(f'Opção selecionada: {opcao_selecionada}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = JanelaComboBox()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- **`QComboBox`**: É usado para criar uma ComboBox na interface. A ComboBox permite ao usuário selecionar uma opção de uma lista suspensa de itens.

- **`.addItem('Opção')`**: Adiciona itens à ComboBox. No exemplo, adicionamos quatro opções ('Opção 1', 'Opção 2', 'Opção 3', 'Opção 4').

- **`.currentIndexChanged.connect(self.mostrar_selecao)`**: Conecta o sinal `currentIndexChanged`, que é emitido sempre que o usuário seleciona uma opção diferente na ComboBox, ao método `mostrar_selecao`. Isso atualiza dinamicamente a interface com a opção selecionada.

- **`self.combobox.currentText()`**: Obtém o texto da opção atualmente selecionada na ComboBox.

- **`.setText(f'Opção selecionada: {opcao_selecionada}')`**: Atualiza o texto da label para exibir a opção selecionada na ComboBox.

## Utilização da ComboBox
ComboBoxes são ideais para:

- **Seleção de Opções**: Permitir ao usuário escolher uma opção única de uma lista pré-definida.

- **Configurações**: Selecionar preferências, configurações ou modos de operação em aplicações.

- **Filtros e Categorização**: Segmentar dados ou conteúdos em categorias específicas.

Com este exemplo básico, você pode integrar ComboBoxes em suas aplicações PyQt para melhorar a interatividade e a usabilidade da interface com o usuário, facilitando a seleção e a escolha de opções dentro da aplicação.