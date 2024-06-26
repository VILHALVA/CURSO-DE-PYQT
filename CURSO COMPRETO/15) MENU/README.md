# MENU
Para adicionar um menu em uma aplicação PyQt usando `QMenuBar`, `QMenu` e `QAction`, você pode seguir o exemplo abaixo. Um menu é uma parte essencial da interface de usuário para organizar funcionalidades e comandos de forma acessível aos usuários.

## Exemplo de Menu em PyQt
Neste exemplo, criaremos uma janela principal (`QMainWindow`) com um menu contendo três opções principais: "Arquivo", "Editar" e "Ajuda". Cada menu terá algumas ações associadas a elas.

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Exemplo de Menu')
        self.setGeometry(100, 100, 600, 400)

        # Criando ação para a opção 'Novo'
        nova_action = QAction('Novo', self)
        nova_action.triggered.connect(self.novo_arquivo)

        # Criando ação para a opção 'Abrir'
        abrir_action = QAction('Abrir', self)
        abrir_action.triggered.connect(self.abrir_arquivo)

        # Criando ação para a opção 'Salvar'
        salvar_action = QAction('Salvar', self)
        salvar_action.triggered.connect(self.salvar_arquivo)

        # Criando ação para a opção 'Sair'
        sair_action = QAction('Sair', self)
        sair_action.triggered.connect(self.close)

        # Criando o menu 'Arquivo' e adicionando ações
        menu_arquivo = self.menuBar().addMenu('Arquivo')
        menu_arquivo.addAction(nova_action)
        menu_arquivo.addAction(abrir_action)
        menu_arquivo.addAction(salvar_action)
        menu_arquivo.addSeparator()  # Adiciona uma linha separadora
        menu_arquivo.addAction(sair_action)

        # Criando o menu 'Editar' com uma ação 'Desfazer'
        menu_editar = self.menuBar().addMenu('Editar')
        desfazer_action = QAction('Desfazer', self)
        menu_editar.addAction(desfazer_action)

        # Criando o menu 'Ajuda' com uma ação 'Sobre'
        menu_ajuda = self.menuBar().addMenu('Ajuda')
        sobre_action = QAction('Sobre', self)
        menu_ajuda.addAction(sobre_action)

    def novo_arquivo(self):
        print('Ação: Novo arquivo')

    def abrir_arquivo(self):
        print('Ação: Abrir arquivo')

    def salvar_arquivo(self):
        print('Ação: Salvar arquivo')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec_())
```

## Explicação do Código
- **`QAction`**: Representa uma ação que pode ser disparada pelo usuário. Elas são conectadas a métodos da aplicação (`novo_arquivo`, `abrir_arquivo`, `salvar_arquivo`, etc.) que definem o que acontece quando a ação é ativada.

- **`self.menuBar().addMenu('Arquivo')`**: Cria um menu chamado "Arquivo" na barra de menu da janela principal (`QMainWindow`).

- **`.addAction(nova_action)`**: Adiciona a ação `nova_action` ao menu "Arquivo". O método `triggered.connect` conecta a ação ao método `novo_arquivo`, que será chamado quando a ação for ativada.

- **`.addSeparator()`**: Adiciona uma linha separadora no menu "Arquivo" para organizar visualmente as ações.

- **`.close`**: Fecha a janela principal quando a ação "Sair" é ativada.

- **`app.exec_()`**: Inicia o loop de eventos da aplicação PyQt, garantindo que a aplicação permaneça em execução até que seja fechada pelo usuário.

