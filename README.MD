# Sistema de Gerenciamento de Tarefas

Este é um sistema de gerenciamento de tarefas desenvolvido com Django 5.1, que permite criar, listar, atualizar e excluir tarefas e categorias.

## Funcionalidades

- CRUD completo para tarefas e categorias
- Interface amigável com Bootstrap
- Sistema de mensagens para feedback ao usuário
- Paginação de resultados
- Organização de tarefas por categorias

## Requisitos

- Python 3.10+
- Django 5.1.7

## Estrutura do Projeto

O projeto segue uma estrutura organizada com os aplicativos em uma pasta separada:

```
├── apps                    # Pasta contendo os aplicativos Django
│   ├── categorias          # App para gerenciamento de categorias
│   └── tarefas             # App para gerenciamento de tarefas
├── projetoarle             # Configurações principais do projeto
├── templates               # Templates HTML compartilhados
│   ├── categorias          # Templates específicos para categorias
│   ├── partials            # Componentes reutilizáveis
│   └── tarefas             # Templates específicos para tarefas
└── manage.py               # Script de gerenciamento do Django
```

## Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/levidornelas/arle-desafio
cd arle-desafio
```

### 2. Crie e ative um ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install django
```

### 4. Banco de dados configurado

O projeto usa SQLite por padrão, com um banco de dados já previamente populado. Caso queira fazer alguma alteração, altere os modelos e rode:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário (opcional, para acesso ao admin)

```bash
python manage.py createsuperuser
```

### 6. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

Agora você pode acessar o sistema em [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Uso

### Tarefas

- **Listar tarefas**: Acesse a página inicial
- **Criar tarefa**: Clique no botão "Nova Tarefa"
- **Editar tarefa**: Clique no botão de edição ao lado da tarefa
- **Excluir tarefa**: Clique no botão de exclusão e confirme

### Categorias

- **Listar categorias**: Acesse o menu Categorias
- **Criar categoria**: Clique no botão "Nova Categoria"
- **Editar categoria**: Clique no botão de edição ao lado da categoria
- **Excluir categoria**: Clique no botão de exclusão e confirme


## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para obter detalhes.
