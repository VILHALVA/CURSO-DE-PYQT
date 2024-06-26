# INTRODUÇÃO E INSTALAÇÃO DO MÓDULO
O PyQt é uma biblioteca Python que permite criar interfaces gráficas de usuário (GUIs) de forma rápida e eficiente. Ele é baseado na biblioteca Qt, que é uma das ferramentas mais utilizadas para desenvolvimento de GUIs em várias plataformas.

## Conceito
PyQt é uma biblioteca Python que fornece bindings para a biblioteca Qt. Ele permite criar aplicações com interfaces gráficas ricas e interativas, utilizando Python como linguagem de programação principal.

## Instalação
Para começar a utilizar o PyQt, você precisa instalar o módulo PyQt5. Aqui está como você pode fazer isso:

1. **Instalação via pip:**
   
   Abra o terminal ou prompt de comando e execute o seguinte comando para instalar o PyQt5:

   ```bash
   pip install PyQt5
   ```

   Isso irá baixar e instalar o PyQt5 e suas dependências necessárias.

2. **Verificação da Instalação:**

   Após a instalação, você pode verificar se o PyQt5 foi instalado corretamente executando um simples script que cria uma janela com um label:

   ```python
   from PyQt5.QtWidgets import QApplication, QLabel

   # Criação de uma instância de QApplication
   app = QApplication([])

   # Criação de um QLabel
   label = QLabel('Hello, PyQt!')

   # Exibição do QLabel
   label.show()

   # Execução do loop de eventos da aplicação
   app.exec_()
   ```

   - **Explicação do Código:**

     - `from PyQt5.QtWidgets import QApplication, QLabel`: Importa as classes `QApplication` e `QLabel` do módulo `QtWidgets` do PyQt5.
     - `app = QApplication([])`: Cria uma instância de `QApplication`, que gerencia a aplicação GUI.
     - `label = QLabel('Hello, PyQt!')`: Cria um objeto `QLabel` com o texto 'Hello, PyQt!'.
     - `label.show()`: Exibe o QLabel na tela.
     - `app.exec_()`: Inicia o loop de eventos da aplicação, permitindo que a interface gráfica seja interativa.

Este é um exemplo simples para verificar se o PyQt5 está funcionando corretamente após a instalação.

