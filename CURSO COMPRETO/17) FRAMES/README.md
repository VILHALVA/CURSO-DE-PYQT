# FRAMES
Em PyQt, frames são widgets usados para agrupar e organizar outros widgets dentro de uma interface gráfica. Eles ajudam a estruturar e segmentar visualmente diferentes partes da janela principal, facilitando o layout e a organização dos elementos da GUI.

## Exemplo de Uso de Frames em PyQt
Vamos criar um exemplo simples onde utilizamos frames (`QFrame`) para agrupar diferentes tipos de widgets dentro de uma janela principal (`QMainWindow`).

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame


class JanelaFrames(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Frames')
        self.setGeometry(100, 100, 500, 300)

        # Criando um layout vertical para a janela principal
        layout_principal = QVBoxLayout()

        # Criando um frame para os widgets superiores
        frame_superior = QFrame(self)
        frame_superior.setFrameShape(QFrame.StyledPanel)  # Define o estilo do frame
        layout_superior = QVBoxLayout(frame_superior)

        label_nome = QLabel('Nome:', frame_superior)
        layout_superior.addWidget(label_nome)

        linha_nome = QLineEdit(frame_superior)
        layout_superior.addWidget(linha_nome)

        frame_superior.setLayout(layout_superior)
        layout_principal.addWidget(frame_superior)

        # Criando um frame para os widgets inferiores
        frame_inferior = QFrame(self)
        frame_inferior.setFrameShape(QFrame.StyledPanel)  # Define o estilo do frame
        layout_inferior = QHBoxLayout(frame_inferior)

        botao_ok = QPushButton('OK', frame_inferior)
        layout_inferior.addWidget(botao_ok)

        botao_cancelar = QPushButton('Cancelar', frame_inferior)
        layout_inferior.addWidget(botao_cancelar)

        frame_inferior.setLayout(layout_inferior)
        layout_principal.addWidget(frame_inferior)

        # Criando um widget central para a janela principal e aplicando o layout
        widget_central = QWidget(self)
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = JanelaFrames()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- **`QFrame`**: É usado para criar um frame na interface gráfica. Um `QFrame` pode ter um estilo visual definido (`setFrameShape`) como `QFrame.StyledPanel`, `QFrame.Box`, `QFrame.Panel`, entre outros, que determina sua aparência na interface.

- **`setFrameShape(QFrame.StyledPanel)`**: Define o estilo do frame como um painel estilizado, que pode ser visualmente distinto dependendo do estilo do sistema operacional.

- **`QVBoxLayout` e `QHBoxLayout`**: São layouts verticais e horizontais, respectivamente, usados para organizar widgets dentro dos frames. Eles permitem adicionar widgets de forma sequencial e controlar o espaçamento entre eles.

- **`layout.addWidget(widget)`**: Adiciona widgets ao layout do frame (`layout_superior` e `layout_inferior` neste exemplo).

- **`frame_superior.setLayout(layout_superior)` e `frame_inferior.setLayout(layout_inferior)`**: Define o layout criado para cada frame.

- **`self.setCentralWidget(widget_central)`**: Define o widget central da janela principal como `widget_central`, que contém todos os frames e widgets organizados.

## Utilização de Frames
Os frames são úteis para:

- **Organização Visual**: Agrupar widgets relacionados para uma melhor organização visual da interface gráfica.
  
- **Separação de Componentes**: Segmentar diferentes partes da interface para facilitar a manutenção e a compreensão do layout.

- **Estilo e Design**: Aplicar estilos diferentes a partes específicas da GUI, como bordas, sombreamento ou cores de fundo distintas.

