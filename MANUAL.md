# MANUAL
## INSTALAÇÃO DO PYQT:
### PASSO 1: INSTALAR PYTHON:
Certifique-se de ter o Python instalado. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/). Durante a instalação, marque a opção para adicionar Python ao PATH.

### PASSO 2: INSTALAR O PYQT:
Você pode instalar o PyQt usando o pip. Abra um terminal ou prompt de comando e execute o seguinte comando:

```sh
pip install PyQt5
```

## CONFIGURAÇÃO:
### PASSO 1: VERIFICAR A INSTALAÇÃO:
Para verificar se a instalação foi bem-sucedida, você pode executar o seguinte comando no terminal:

```sh
python -c "from PyQt5.QtWidgets import QApplication, QLabel; app = QApplication([]); label = QLabel('Hello, PyQt!'); label.show(); app.exec_()"
```

Se uma janela com a mensagem "Hello, PyQt!" aparecer, a instalação está correta.

## CRIANDO O PRIMEIRO PROJETO COM PYQT:
### PASSO 1: CRIAR UM ARQUIVO PYTHON:
Crie um novo arquivo Python chamado `hello_pyqt.py`.

### PASSO 2: ESCREVER O CÓDIGO:
Abra o `hello_pyqt.py` em seu editor de texto ou IDE favorito e adicione o seguinte código:

```python
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

# Inicializa a aplicação
app = QApplication(sys.argv)

# Cria uma janela principal
window = QWidget()
window.setWindowTitle('Meu Primeiro Aplicativo PyQt')

# Cria um layout e um widget de label
layout = QVBoxLayout()
label = QLabel('Olá, PyQt!')

# Adiciona o label ao layout
layout.addWidget(label)

# Define o layout da janela principal
window.setLayout(layout)

# Mostra a janela
window.show()

# Executa o loop da aplicação
sys.exit(app.exec_())
```

### PASSO 3: EXECUTAR O PROJETO:
Salve o arquivo e execute-o no terminal ou prompt de comando com o seguinte comando:

```sh
python hello_pyqt.py
```

Uma janela deve aparecer com a mensagem "Olá, PyQt!".

## ESTRUTURA DO PROJETO:
Para projetos maiores, você pode querer organizar seu código em uma estrutura de diretórios. Aqui está um exemplo básico de estrutura de diretórios para um projeto PyQt:

```
meu_projeto_pyqt/
│
├── main.py           # Ponto de entrada do aplicativo
├── gui/
│   ├── __init__.py   # Arquivo de inicialização do módulo
│   ├── main_window.py# Arquivo que define a janela principal
│
├── resources/        # Diretório para recursos como imagens, arquivos de estilo, etc.
```

### EXEMPLO DE `main_window.py`:
```python
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplicativo PyQt Estruturado')

        layout = QVBoxLayout()
        label = QLabel('Bem-vindo ao PyQt!')

        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
```

### EXEMPLO DE `main.py`
```python
import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

Com essa estrutura, seu código ficará mais organizado e fácil de manter conforme seu projeto cresce.