# Setup do Ambiente de Desenvolvimento - Backend

Este guia explica como configurar o ambiente de desenvolvimento para o backend do projeto Trivia API.

## Pré-requisitos

- Python 3.10, 3.11 ou 3.12
- PostgreSQL instalado e rodando
- `uv` instalado (gerenciador de pacotes Python moderno)

## Passo a Passo

### 1. Instalar o PostgreSQL (se necessário)

No Ubuntu/WSL:

```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

Iniciar o serviço:

```bash
sudo service postgresql start
```

### 2. Configurar o PostgreSQL

O projeto está configurado para usar:
- Database: `trivia`
- Usuário: `postgres`
- Senha: `password` (definida em `models.py`)

Se necessário, criar o usuário e configurar a senha:

```bash
sudo -u postgres psql
CREATE USER postgres WITH PASSWORD 'password';
ALTER USER postgres CREATEDB;
\q
```

### 3. Instalar dependências com uv

No diretório raiz do projeto (onde está o `pyproject.toml`):

```bash
uv sync
```

Isso criará um ambiente virtual em `.venv` e instalará todas as dependências.

### 4. Criar o database

```bash
createdb trivia
```

### 5. Popular o database

```bash
cd backend
psql trivia < trivia.psql
```

### 6. Configurar variáveis de ambiente (opcional)

Você pode criar um arquivo `.env` no diretório `backend/`:

```bash
FLASK_APP=flaskr
FLASK_ENV=development
DATABASE_URL=postgresql://postgres:password@localhost:5432/trivia
```

### 7. Executar o servidor

```bash
# Ativar o ambiente virtual
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Executar o servidor
cd backend
flask run --reload
```

O servidor estará disponível em: `http://127.0.0.1:5000`

## Alternativa: Usar o script de setup automatizado

Execute o script de setup:

```bash
cd backend
./setup_dev.sh
```

**Nota:** Este script requer privilégios `sudo` para iniciar o PostgreSQL.

## Rodar os testes

Para criar o banco de testes e executar os testes:

```bash
dropdb trivia_test 2>/dev/null || true
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## Estrutura do Projeto

```
backend/
├── flaskr/
│   └── __init__.py        # Aplicação Flask
├── models.py              # Modelos SQLAlchemy
├── test_flaskr.py         # Testes unitários
├── trivia.psql            # Dump SQL do database
└── requirements.txt       # Dependências Python
```

## Troubleshooting

### Erro de conexão com PostgreSQL

Se você receber erro de conexão, verifique:

1. Se o PostgreSQL está rodando: `sudo service postgresql status`
2. Se as credenciais em `models.py` estão corretas
3. Se o database existe: `psql -l | grep trivia`

### Problemas com o uv

Se o `uv` não estiver instalado:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Ou usando pip:

```bash
pip install uv
```

### Resetar o database

```bash
dropdb trivia
createdb trivia
psql trivia < trivia.psql
```
