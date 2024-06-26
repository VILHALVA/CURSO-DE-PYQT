# CHECK BOX
Para adicionar checkboxes (caixas de seleção) em uma aplicação PyQt usando `QCheckBox`, você pode seguir o exemplo abaixo. As checkboxes são úteis quando você precisa que o usuário selecione uma ou mais opções entre várias disponíveis.

## Exemplo de Checkboxes em PyQt
Neste exemplo, criaremos uma janela principal (`QMainWindow`) com duas checkboxes, onde cada uma representa uma opção diferente. Vamos mostrar como capturar o estado dessas checkboxes quando o usuário interagir com elas.

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QCheckBox

class JanelaCheckBox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Checkboxes')
        self.setGeometry(100, 100, 400, 200)

        # Criando um layout vertical para a janela principal
        layout_principal = QVBoxLayout()

        # Criando uma label para exibir o estado das checkboxes
        self.label_status = QLabel('Status das Checkboxes:', self)
        layout_principal.addWidget(self.label_status)

        # Criando a primeira checkbox
        self.checkbox1 = QCheckBox('Opção 1', self)
        self.checkbox1.stateChanged.connect(self.mostrar_status)
        layout_principal.addWidget(self.checkbox1)

        # Criando a segunda checkbox
        self.checkbox2 = QCheckBox('Opção 2', self)
        self.checkbox2.stateChanged.connect(self.mostrar_status)
        layout_principal.addWidget(self.checkbox2)

        # Criando um widget central para a janela principal e aplicando o layout
        widget_central = QWidget(self)
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    def mostrar_status(self):
        # Obtém o estado atual das checkboxes
        status1 = 'Selecionada' if self.checkbox1.isChecked() else 'Não selecionada'
        status2 = 'Selecionada' if self.checkbox2.isChecked() else 'Não selecionada'

        # Atualiza a label com o estado das checkboxes
        self.label_status.setText(f'Status das Checkboxes:\nOpção 1: {status1}\nOpção 2: {status2}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = JanelaCheckBox()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- **`QCheckBox`**: É usado para criar uma checkbox na interface. Cada `QCheckBox` representa uma opção que o usuário pode selecionar ou desmarcar.

- **`.stateChanged.connect(self.mostrar_status)`**: Conecta o sinal `stateChanged`, que é emitido quando o estado da checkbox muda, ao método `mostrar_status`. Isso permite que atualizemos dinamicamente a interface sempre que o usuário selecionar ou desmarcar uma checkbox.

- **`self.checkbox1.isChecked()`**: Verifica se a checkbox `checkbox1` está marcada (`True`) ou desmarcada (`False`).

- **`self.label_status.setText(...)`**: Atualiza o texto da label para exibir o estado atual das checkboxes sempre que uma mudança ocorre.

## Utilização das Checkboxes
As checkboxes são comumente utilizadas em interfaces para permitir que o usuário escolha entre várias opções independentes. Elas são ideais para configurações de aplicativos, seleção de preferências, ou qualquer cenário onde o usuário precisa fazer escolhas múltiplas.

