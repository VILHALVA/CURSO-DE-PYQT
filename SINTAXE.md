# SINTAXE
## 1. LABELS:
Os labels são usados para exibir texto estático na interface.

### CÓDIGO:
```python
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

app = QApplication(sys.argv)

# Cria uma janela principal
window = QWidget()
window.setWindowTitle('Exemplo de Label com PyQt')

# Cria um layout e um widget de label
layout = QVBoxLayout()
label = QLabel('Este é um Label')

# Adiciona o label ao layout
layout.addWidget(label)

# Define o layout da janela principal
window.setLayout(layout)

# Mostra a janela
window.show()

# Executa o loop da aplicação
sys.exit(app.exec_())
```

### EXPLICAÇÃO:
- `QLabel`: Cria um label.
- `setText`: Define o texto exibido pelo label.
- `QVBoxLayout`: Um layout vertical que organiza widgets verticalmente.
- `addWidget`: Adiciona o widget ao layout.

## 2. BOTÕES:
Os botões permitem ao usuário executar ações quando clicados.

### CÓDIGO:
```python
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

def on_click():
    print("Botão clicado!")

app = QApplication(sys.argv)

# Cria uma janela principal
window = QWidget()
window.setWindowTitle('Exemplo de Botão com PyQt')

# Cria um layout e um widget de botão
layout = QVBoxLayout()
button = QPushButton('Clique Aqui')
button.clicked.connect(on_click)

# Adiciona o botão ao layout
layout.addWidget(button)

# Define o layout da janela principal
window.setLayout(layout)

# Mostra a janela
window.show()

# Executa o loop da aplicação
sys.exit(app.exec_())
```

### EXPLICAÇÃO:
- `QPushButton`: Cria um botão.
- `setText`: Define o texto exibido no botão.
- `clicked.connect`: Conecta o clique do botão a uma função.

## 3. CAIXAS DE ENTRADA DE TEXTO (ENTRY):
As caixas de entrada de texto permitem ao usuário inserir texto.

### CÓDIGO:
```python
import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QWidget

def get_text():
    texto = entry.text()
    print(f"Você digitou: {texto}")

app = QApplication(sys.argv)

# Cria uma janela principal
window = QWidget()
window.setWindowTitle('Exemplo de Entrada de Texto com PyQt')

# Cria um layout, uma caixa de entrada de texto e um botão
layout = QVBoxLayout()
entry = QLineEdit()
entry.setPlaceholderText('Digite algo aqui')
button = QPushButton('Enviar')
button.clicked.connect(get_text)

# Adiciona a entrada de texto e o botão ao layout
layout.addWidget(entry)
layout.addWidget(button)

# Define o layout da janela principal
window.setLayout(layout)

# Mostra a janela
window.show()

# Executa o loop da aplicação
sys.exit(app.exec_())
```

### EXPLICAÇÃO:
- `QLineEdit`: Cria uma caixa de entrada de texto.
- `setPlaceholderText`: Define o texto de espaço reservado que aparece na caixa de entrada.

## 4. CAIXAS DE SELEÇÃO (CHECKBUTTONS):
As caixas de seleção permitem ao usuário selecionar ou desmarcar opções.

### CÓDIGO:
```python
import sys
from PyQt5.QtWidgets import QApplication, QCheckBox, QPushButton, QVBoxLayout, QWidget

def check_status():
    status = 'checked' if checkbox.isChecked() else 'unchecked'
    print(f"Checkbox está: {status}")

app = QApplication(sys.argv)

# Cria uma janela principal
window = QWidget()
window.setWindowTitle('Exemplo de Checkbox com PyQt')

# Cria um layout e uma caixa de seleção
layout = QVBoxLayout()
checkbox = QCheckBox('Aceito os termos e condições')
button = QPushButton('Verificar')
button.clicked.connect(check_status)

# Adiciona a caixa de seleção e o botão ao layout
layout.addWidget(checkbox)
layout.addWidget(button)

# Define o layout da janela principal
window.setLayout(layout)

# Mostra a janela
window.show()

# Executa o loop da aplicação
sys.exit(app.exec_())
```

### EXPLICAÇÃO:
- `QCheckBox`: Cria uma caixa de seleção.
- `isChecked`: Verifica se a caixa de seleção está marcada.

## 5. RADIO BUTTONS:
Os radio buttons permitem ao usuário selecionar apenas uma opção de um grupo de opções.

### CÓDIGO:
```python
import sys
from PyQt5.QtWidgets import QApplication, QRadioButton, QPushButton, QVBoxLayout, QWidget

def check_selection():
    selecao = radio1.text() if radio1.isChecked() else radio2.text()
    print(f"Você selecionou: {selecao}")

app = QApplication(sys.argv)

# Cria uma janela principal
window = QWidget()
window.setWindowTitle('Exemplo de Radio Button com PyQt')

# Cria um layout e radio buttons
layout = QVBoxLayout()
radio1 = QRadioButton('Opção 1')
radio2 = QRadioButton('Opção 2')
button = QPushButton('Verificar Seleção')
button.clicked.connect(check_selection)

# Adiciona os radio buttons e o botão ao layout
layout.addWidget(radio1)
layout.addWidget(radio2)
layout.addWidget(button)

# Define o layout da janela principal
window.setLayout(layout)

# Mostra a janela
window.show()

# Executa o loop da aplicação
sys.exit(app.exec_())
```

### EXPLICAÇÃO:
- `QRadioButton`: Cria um radio button.
- `isChecked`: Verifica se o radio button está selecionado.
- `text`: Obtém o texto do radio button.

## 6. SLIDERS:
Os sliders permitem ao usuário selecionar um valor de um intervalo.

### CÓDIGO:
```python
import sys
from PyQt5.QtWidgets import QApplication, QSlider, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

def slider_changed(value):
    print(f"Valor do slider: {value}")

app = QApplication(sys.argv)

# Cria uma janela principal
window = QWidget()
window.setWindowTitle('Exemplo de Slider com PyQt')

# Cria um layout e um slider
layout = QVBoxLayout()
slider = QSlider(Qt.Horizontal)
slider.setRange(0, 100)
slider.valueChanged.connect(slider_changed)

# Adiciona o slider ao layout
layout.addWidget(slider)

# Define o layout da janela principal
window.setLayout(layout)

# Mostra a janela
window.show()

# Executa o loop da aplicação
sys.exit(app.exec_())
```

### EXPLICAÇÃO:
- `QSlider`: Cria um slider.
- `setRange`: Define o valor mínimo e máximo do slider.
- `valueChanged.connect`: Conecta a mudança de valor do slider a uma função.

## 7. COMBOBOXES:
As comboboxes permitem ao usuário selecionar um valor de uma lista suspensa.

### CÓDIGO:
```python
import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QPushButton, QVBoxLayout, QWidget

def get_selection():
    selecao = combobox.currentText()
    print(f"Você selecionou: {selecao}")

app = QApplication(sys.argv)

# Cria uma janela principal
window = QWidget()
window.setWindowTitle('Exemplo de ComboBox com PyQt')

# Cria um layout e uma combobox
layout = QVBoxLayout()
combobox = QComboBox()
combobox.addItems(['Opção 1', 'Opção 2', 'Opção 3'])
button = QPushButton('Verificar Seleção')
button.clicked.connect(get_selection)

# Adiciona a combobox e o botão ao layout
layout.addWidget(combobox)
layout.addWidget(button)

# Define o layout da janela principal
window.setLayout(layout)

# Mostra a janela
window.show()

# Executa o loop da aplicação
sys.exit(app.exec_())
```

### EXPLICAÇÃO:
- `QComboBox`: Cria uma combobox.
- `addItems`: Adiciona uma lista de opções à combobox.
- `currentText`: Obtém o texto da opção selecionada.

## 8. FRAMES:
Os frames são usados para agrupar outros widgets.

### CÓDIGO:
```python
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QFrame, QWidget

app = QApplication(sys.argv)

# Cria uma janela principal
window = QWidget()
window.setWindowTitle('Exemplo de Frame com PyQt')

# Cria um layout e um frame
layout = QVBoxLayout()
frame = QFrame()
frame_layout = QVBoxLayout()
frame.setLayout(frame_layout)

# Adiciona widgets ao frame
label = QLabel('Label no Frame')
button = QPushButton('Botão no Frame')
frame_layout.addWidget(label)
frame_layout.addWidget(button)

# Adiciona o frame ao layout principal
layout.addWidget(frame)

# Define o layout da janela principal
window.setLayout(layout)

# Mostra a janela
window.show()

# Executa o loop da aplicação
sys.exit(app.exec_())
```

### EXPLICAÇÃO:
- `QFrame`: Cria um frame.
- `setLayout`: Define o layout do frame.
- Widgets adicionados ao frame são posicionados dentro dele.