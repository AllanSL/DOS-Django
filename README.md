# 📝 Lista de Tarefas - Projeto de Desenvolvimento Orientado a Serviços



Este é um projeto desenvolvido no contexto da disciplina **Desenvolvimento Orientado a Serviços**, ministrada pelo professor **Paulo Ricardo da Silva Pontes** no **IFTO - Instituto Federal do Tocantins - Campus Araguaína**.

## 🚀 Descrição do Projeto

O objetivo deste projeto é desenvolver uma aplicação de lista de tarefas utilizando o framework **Django**. A aplicação permite que usuários cadastrem, visualizem, editem e excluam tarefas e usuários, com uma interface amigável e responsiva utilizando **Tailwind CSS**. O projeto segue a arquitetura de **Programação Orientada a Serviços**, priorizando a separação clara entre a lógica de negócio e a interface.

## ✅ Funcionalidades

- **Listagem de Tarefas**: Visualização de todas as tarefas cadastradas, incluindo título, descrição, data e usuário responsável.
- **Cadastro de Tarefas**: Permite adicionar novas tarefas, especificando título, descrição, data e usuário.
- **Edição de Tarefas**: Possibilita alterar informações das tarefas existentes.
- **Exclusão de Tarefas**: Remove uma tarefa do sistema com confirmação do usuário.
- **Listagem de Usuários**: Exibe todos os usuários cadastrados no sistema.
- **Cadastro de Usuários**: Permite adicionar novos usuários.
- **Edição de Usuários**: Possibilita atualizar informações de um usuário.
- **Exclusão de Usuários**: Permite remover um usuário do sistema.
- **Tela Inicial**: Interface principal onde o usuário pode escolher entre gerenciar tarefas ou usuários.

## 🗂️ Estrutura do Projeto

A estrutura básica do projeto é a seguinte:

```
POS/
├── .vscode/
├── todo/
│   ├── todo/
│   ├── tarefas/
│   ├── venv/
│   ├── db.sqlite3
│   └── manage.py
```

### 📁 Pastas e Arquivos Importantes

- `tarefas/`: Contém os arquivos relacionados ao app de tarefas, como modelos (`models.py`), views (`views.py`), templates (`listarTarefas.html`), entre outros.
- `todo/`: Diretório principal do projeto, contendo configurações do Django (`settings.py`, `urls.py`).
- `venv/`: Ambiente virtual Python para gerenciamento das dependências do projeto.
- `db.sqlite3`: Banco de dados SQLite utilizado na aplicação.

## 🛠️ Tecnologias Utilizadas

- **Django 5.x**: Framework para desenvolvimento web.
- **SQLite**: Banco de dados relacional utilizado no desenvolvimento.
- **Tailwind CSS**: Framework CSS para estilização da interface.

## 📝 Como Rodar o Projeto

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone o repositório**:

   ```bash
   git clone <url-do-repositorio>
   ```

2. **Navegue até a pasta do projeto**:

   ```bash
   cd POS/todo
   ```

3. **Ative o ambiente virtual**:

   ```bash
   source venv/bin/activate  # No Linux/macOS
   .\venv\Scripts\activate   # No Windows
   ```

4. **Verifique se o Django está instalado**:

   ```bash
   python -m django --version
   ```

   Se não estiver instalado, instale com:

   ```bash
   pip install django
   ```

5. **Execute as migrações**:

   ```bash
   python manage.py migrate
   ```

6. **Inicie o servidor**:

   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação no navegador**:

   - **Tela Inicial**: `http://127.0.0.1:8000/`

## 📚 Informações sobre a Disciplina

- **Matéria**: Desenvolvimento Orientado a Serviços
- **Professor**: Paulo Ricardo da Silva Pontes
- **Instituição**: IFTO - Instituto Federal do Tocantins - Campus Araguaína

