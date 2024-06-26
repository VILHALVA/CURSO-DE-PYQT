# LABEL
Labels (rótulos) em PyQt são widgets usados para exibir texto ou imagens não interativas na interface gráfica de usuário (GUI). Eles são úteis para fornecer informações estáticas aos usuários ou para identificar outros widgets na interface.

## Conceito
Em PyQt, labels são criados usando a classe `QLabel` do módulo `QtWidgets`. Eles podem exibir texto, imagens ou ambos, e podem ser configurados com diferentes estilos de fonte, alinhamentos e tamanhos.

## Exemplo de Código
Aqui está um exemplo simples que cria uma janela com um label usando `QLabel`:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Label com PyQt')
        self.setGeometry(100, 100, 400, 300)

        # Cria um QLabel na janela
        label = QLabel('Este é um Label PyQt!', self)
        label.setGeometry(50, 50, 300, 100)  # Define posição e tamanho do label
        label.setAlignment(Qt.AlignCenter)  # Alinha o texto centralmente

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
- `self.setWindowTitle('Exemplo de Label com PyQt')`: Define o título da janela.
- `self.setGeometry(100, 100, 400, 300)`: Define a posição (100, 100) e o tamanho (400x300 pixels) da janela.
- `label = QLabel('Este é um Label PyQt!', self)`: Cria um QLabel com o texto 'Este é um Label PyQt!', associado à janela `self`.
- `label.setGeometry(50, 50, 300, 100)`: Define a posição (50, 50) e o tamanho (300x100 pixels) do label dentro da janela.
- `label.setAlignment(Qt.AlignCenter)`: Alinha o texto centralmente dentro do QLabel.

- `if __name__ == '__main__':`: Verifica se o script está sendo executado diretamente.
- `app = QApplication(sys.argv)`: Cria uma instância de `QApplication`, necessária para gerenciar a aplicação GUI.
- `janela = MinhaJanela()`: Cria uma instância da classe `MinhaJanela`.
- `janela.show()`: Exibe a janela na tela.
- `sys.exit(app.exec_())`: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

