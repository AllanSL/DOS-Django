# 📝 Lista de Tarefas - Projeto de Desenvolvimento Orientado a Serviços

![Django](https://img.shields.io/badge/Django-5.x-blue?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

Este é um projeto desenvolvido no contexto da disciplina **Desenvolvimento Orientado a Serviços**, ministrada pelo professor **Paulo Ricardo da Silva Pontes** no **IFTO - Instituto Federal do Tocantins - Campus Araguaína**.

## 🚀 Descrição do Projeto

O objetivo deste projeto é desenvolver uma aplicação simples de lista de tarefas utilizando o framework **Django**. A aplicação permite que um usuário visualize as tarefas cadastradas no sistema, com informações como título, descrição e data de criação. O projeto segue a arquitetura de **Programação Orientada a Serviços**, com foco na criação de uma API para gestão de tarefas.

## ✅ Funcionalidades

- **Listagem de Tarefas**: Visualização das tarefas cadastradas com título, descrição e data de criação.
- **Cadastro de Tarefas**: Através do Django Admin, é possível criar e gerenciar tarefas.
- **Administração de Usuários e Tarefas**: Utilização do painel administrativo do Django para criar, editar e excluir usuários e tarefas.

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

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute as migrações**:
   ```bash
   python manage.py migrate
   ```

6. **Inicie o servidor**:
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação no navegador** em `http://127.0.0.1:8000/tarefas/listartarefas/`.

## 📚 Informações sobre a Disciplina

- **Matéria**: Desenvolvimento Orientado a Serviços
- **Professor**: Paulo Ricardo da Silva Pontes
- **Instituição**: IFTO - Instituto Federal do Tocantins - Campus Araguaína