# CALENDÁRIO
Para adicionar um widget de calendário (calendário) em uma aplicação PyQt, utilizamos o widget `QCalendarWidget` fornecido pelo módulo `QtWidgets`. Esse widget permite ao usuário visualizar e interagir com um calendário, selecionando datas ou navegando entre meses e anos. Abaixo está um exemplo básico de como incorporar e utilizar um `QCalendarWidget` em PyQt:

## Exemplo de Calendário em PyQt
Neste exemplo, vamos criar uma janela com um `QCalendarWidget` que exibe um calendário. Vamos também adicionar um label para mostrar a data selecionada pelo usuário.

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget, QLabel

class JanelaCalendario(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Calendário')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.calendario = QCalendarWidget()
        self.calendario.clicked.connect(self.mostrar_data)
        layout.addWidget(self.calendario)

        self.label_data = QLabel('Data selecionada: ')
        layout.addWidget(self.label_data)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

    def mostrar_data(self):
        data_selecionada = self.calendario.selectedDate()
        self.label_data.setText(f'Data selecionada: {data_selecionada.toString("dd/MM/yyyy")}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = JanelaCalendario()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- `import sys`: Importa o módulo `sys` para lidar com argumentos de linha de comando.
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget, QLabel`: Importa as classes necessárias do módulo `QtWidgets` do PyQt5, incluindo `QCalendarWidget` para o calendário e `QLabel` para exibir texto.
  
- `class JanelaCalendario(QMainWindow)`: Define uma classe `JanelaCalendario` que herda de `QMainWindow`.

- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).

- `self.setWindowTitle('Exemplo de Calendário')`: Define o título da janela.

- `self.setGeometry(100, 100, 400, 300)`: Define a posição (100, 100) e o tamanho (400x300 pixels) da janela.

- `layout = QVBoxLayout()`: Cria um layout vertical para organizar os widgets na janela.

- `self.calendario = QCalendarWidget()`: Cria uma instância de `QCalendarWidget`.

- `self.calendario.clicked.connect(self.mostrar_data)`: Conecta o sinal `clicked` do calendário ao método `mostrar_data`, que será chamado quando uma data for selecionada no calendário.

- `layout.addWidget(self.calendario)`: Adiciona o widget do calendário ao layout vertical.

- `self.label_data = QLabel('Data selecionada: ')`: Cria um QLabel inicializado com um texto padrão.

- `layout.addWidget(self.label_data)`: Adiciona o widget do label ao layout vertical.

- `widget_central = QWidget()`: Cria um widget central para a janela.

- `widget_central.setLayout(layout)`: Define o layout vertical como o layout do widget central.

- `self.setCentralWidget(widget_central)`: Define o widget central da janela como o widget `widget_central`.

- `def mostrar_data(self)`: Define o método `mostrar_data`, que é chamado quando uma data é selecionada no calendário.

- `data_selecionada = self.calendario.selectedDate()`: Obtém a data selecionada do calendário.

- `self.label_data.setText(f'Data selecionada: {data_selecionada.toString("dd/MM/yyyy")}')`: Atualiza o texto do label para exibir a data selecionada no formato "dd/MM/yyyy".

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.

- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.

- `janela = JanelaCalendario()`: Cria uma instância da classe `JanelaCalendario`.

- `janela.show()`: Exibe a janela na tela.

- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

Neste exemplo, ao selecionar uma data no calendário, a data é exibida em um label logo abaixo dele. 