# LAYOUT RESPONSIVO
Em PyQt, para criar layouts responsivos que se ajustem dinamicamente ao redimensionamento da janela, geralmente utilizamos os layouts gerenciadores fornecidos pelo Qt, como `QHBoxLayout`, `QVBoxLayout`, `QGridLayout`, e `QFormLayout`. Esses layouts ajudam a organizar e posicionar os widgets de forma flexível, garantindo que eles se ajustem conforme a janela é redimensionada.

## Exemplo de Layout Responsivo com QGridLayout
Vamos modificar nosso exemplo anterior para usar `QGridLayout`, que é útil para organizar widgets em linhas e colunas.

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QCalendarWidget, QLabel

class JanelaCalendario(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Calendário')
        self.setGeometry(100, 100, 400, 300)

        layout = QGridLayout()

        self.calendario = QCalendarWidget()
        self.calendario.clicked.connect(self.mostrar_data)
        layout.addWidget(self.calendario, 0, 0, 1, 2)  # Coloca o calendário na primeira linha, ocupando 2 colunas

        self.label_data = QLabel('Data selecionada: ')
        layout.addWidget(self.label_data, 1, 0, 1, 2)  # Coloca o label na segunda linha, ocupando 2 colunas

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
- **`QGridLayout`**: Substituímos o `QVBoxLayout` pelo `QGridLayout`. O `QGridLayout` organiza os widgets em uma grade de linhas e colunas.
  
- **`layout.addWidget(self.calendario, 0, 0, 1, 2)`**: Adicionamos o calendário na posição (linha 0, coluna 0) e especificamos que ele ocupará 1 linha e 2 colunas.
  
- **`layout.addWidget(self.label_data, 1, 0, 1, 2)`**: Adicionamos o label na posição (linha 1, coluna 0) e também especificamos que ele ocupará 1 linha e 2 colunas. Isso ajuda a manter uma estrutura de layout mais consistente e responsiva.

## Dicas para Layouts Responsivos
1. **Uso de Layouts Combinados**: Às vezes, pode ser necessário combinar layouts, como `QHBoxLayout` dentro de `QVBoxLayout`, para criar estruturas mais complexas.

2. **Widgets de Preenchimento**: Utilize widgets como `QSpacerItem` para adicionar espaçamento flexível entre widgets ou bordas de janela.

3. **Ajuste Dinâmico**: Conecte sinais como `resizeEvent` para responder ao redimensionamento da janela e ajustar dinamicamente os tamanhos e posições dos widgets.

4. **Política de Tamanho**: Defina políticas de tamanho (`sizePolicy`) para os widgets de modo que eles se comportem corretamente ao redimensionar a janela.

5. **Teste em Diferentes Resoluções**: Verifique se o layout se adapta bem em diferentes tamanhos de tela e resoluções, garantindo uma experiência de usuário consistente.

Utilizando essas técnicas, você pode criar interfaces gráficas mais dinâmicas e adaptáveis em suas aplicações PyQt, proporcionando uma melhor experiência ao usuário independentemente do dispositivo ou tamanho da janela.