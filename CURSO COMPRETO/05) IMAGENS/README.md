# IMAGENS
Em PyQt, imagens são elementos gráficos que podem ser exibidos dentro de janelas ou outros widgets para complementar a interface gráfica de usuário (GUI). Elas são utilizadas para enriquecer a experiência visual dos usuários e podem ser carregadas a partir de arquivos ou recursos internos.

## Conceito
Para exibir imagens em PyQt, normalmente utiliza-se a classe `QLabel` para criar um widget de rótulo e, em seguida, carrega-se a imagem usando a classe `QPixmap` para representar e manipular imagens no formato suportado pelo Qt.

## Exemplo de Código
Aqui está um exemplo simples que carrega e exibe uma imagem em uma janela usando PyQt:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Imagem com PyQt')
        self.setGeometry(100, 100, 400, 300)

        # Carrega a imagem usando QPixmap
        pixmap = QPixmap('python.png')

        # Cria um QLabel na janela para exibir a imagem
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setGeometry(50, 50, pixmap.width(), pixmap.height())  # Define posição e tamanho do label

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- `import sys`: Importa o módulo `sys` para lidar com argumentos de linha de comando.
- `from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel`: Importa as classes necessárias do módulo `QtWidgets` do PyQt5.
- `from PyQt5.QtGui import QPixmap`: Importa a classe `QPixmap` do módulo `QtGui` do PyQt5, que é usada para manipular imagens.
- `class MinhaJanela(QMainWindow):`: Define uma classe `MinhaJanela` que herda de `QMainWindow`.
- `super().__init__()`: Chama o construtor da classe pai (`QMainWindow`).
- `self.setWindowTitle('Exemplo de Imagem com PyQt')`: Define o título da janela.
- `self.setGeometry(100, 100, 400, 300)`: Define a posição (100, 100) e o tamanho (400x300 pixels) da janela.

- `pixmap = QPixmap('python.png')`: Cria um objeto `QPixmap` carregando uma imagem do arquivo 'python.png' localizado no diretório atual do script. Certifique-se de ajustar o caminho e o nome do arquivo conforme necessário para o seu caso.
- `label = QLabel(self)`: Cria um QLabel associado à janela `self`.
- `label.setPixmap(pixmap)`: Define a imagem carregada (`pixmap`) para ser exibida no QLabel.
- `label.setGeometry(50, 50, pixmap.width(), pixmap.height())`: Define a posição (50, 50) e o tamanho (largura e altura) do QLabel com base nas dimensões da imagem carregada.

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.
- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.
- `janela = MinhaJanela()`: Cria uma instância da classe `MinhaJanela`.
- `janela.show()`: Exibe a janela na tela.
- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

Este exemplo carrega e exibe uma imagem 'python.png' em uma janela PyQt usando `QPixmap` e `QLabel`. 