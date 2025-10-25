# Verificação do Ambiente Local - Trivia API

## 📋 Checklist de Software Requerido

### 1. Python 3.7+

**Status:** ✅ Instalado (Python 3.12.3)

Para verificar:
```bash
python3 --version
```

Se não estiver instalado (Ubuntu/WSL):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Virtual Environment

**Status:** ✅ Configurado com `uv`

O projeto usa `uv` para gerenciar o ambiente virtual em `.venv/`

Para verificar:
```bash
ls -la .venv/bin/
```

Para recriar o ambiente:
```bash
uv sync
```

### 3. PostgreSQL

**Status:** ⚠️ Instalado mas serviço não está rodando

**Versão:** PostgreSQL 16.10

#### Verificar instalação:
```bash
psql --version
```

#### Iniciar o PostgreSQL (WSL/Ubuntu):

**Opção 1:** Sem sudo (se já estiver configurado)
```bash
pg_ctlcluster 16 main start
```

**Opção 2:** Com sudo
```bash
sudo service postgresql start
```

**Opção 3:** Verificar se está rodando
```bash
pg_isready -h localhost
```

#### Configurar PostgreSQL para o projeto:

1. **Criar usuário postgres (se necessário):**
```bash
sudo -u postgres psql
```

Dentro do psql:
```sql
CREATE USER postgres WITH PASSWORD 'password';
ALTER USER postgres CREATEDB;
ALTER USER postgres SUPERUSER;
\q
```

2. **Criar o database:**
```bash
createdb trivia
```

3. **Popular o database:**
```bash
cd backend
psql trivia < trivia.psql
```

### 4. Dependências do Projeto

**Status:** ✅ Instaladas

Dependências gerenciadas via `uv` e `pyproject.toml`

Para reinstalar:
```bash
uv sync
```

## 🚀 Iniciar o Projeto

### Passo 1: Iniciar PostgreSQL

```bash
# Método 1 - Com sudo
sudo service postgresql start

# Método 2 - Sem sudo (se configurado)
pg_ctlcluster 16 main start

# Verificar
pg_isready -h localhost
```

### Passo 2: Configurar Database

```bash
# Criar database (se não existe)
createdb trivia

# Popular com dados
cd backend
psql trivia < trivia.psql

# Verificar
psql trivia -c "SELECT COUNT(*) FROM questions;"
```

### Passo 3: Iniciar Servidor Flask

```bash
cd backend
flask run --reload
```

O servidor estará disponível em: **http://127.0.0.1:5000**

### Passo 4: Testar API

Em outro terminal:

```bash
# Testar categorias
curl http://127.0.0.1:5000/categories

# Testar perguntas
curl http://127.0.0.1:5000/questions
```

## 🔧 Troubleshooting

### PostgreSQL não inicia

**Erro:** "sudo: a terminal is required"

**Solução:** Configure sudo para não pedir senha OU use:

```bash
# Adicionar ao /etc/sudoers (com sudo visudo)
# No final do arquivo:
fabiolima ALL=(ALL) NOPASSWD: /usr/bin/service postgresql *
```

Ou configure WSL:

```bash
# No Windows PowerShell (como Admin)
wsl -d Ubuntu -u root
echo "fabiolima ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
exit
```

### Erro de conexão ao banco

**Erro:** "FATAL: database 'trivia' does not exist"

**Solução:**
```bash
createdb trivia
psql trivia < backend/trivia.psql
```

**Erro:** "FATAL: password authentication failed"

**Solução:**
Edite `backend/models.py` para ajustar as credenciais ou:

```bash
sudo -u postgres psql
ALTER USER postgres WITH PASSWORD 'password';
```

### Porta 5000 já em uso

**Solução:**
```bash
flask run --port 5001
```

## 📝 Configuração Completa - Resumo

```bash
# 1. Verificar Python
python3 --version

# 2. Instalar dependências (se necessário)
uv sync

# 3. Iniciar PostgreSQL
sudo service postgresql start
# ou
pg_ctlcluster 16 main start

# 4. Criar e popular database
createdb trivia
cd backend
psql trivia < trivia.psql

# 5. Iniciar servidor
cd backend
flask run --reload

# 6. Testar (em outro terminal)
curl http://127.0.0.1:5000/categories
```

## ✅ Checklist Final

- [ ] Python 3.7+ instalado
- [ ] Ambiente virtual criado (`.venv/`)
- [ ] PostgreSQL instalado
- [ ] PostgreSQL rodando
- [ ] Database `trivia` criado
- [ ] Database populado
- [ ] Dependências instaladas
- [ ] Servidor Flask rodando
- [ ] API respondendo

## 📚 Documentação Adicional

- `backend/SETUP.md` - Guia completo de setup
- `backend/TEST_API.md` - Exemplos de testes
- `RESUMO_SETUP.md` - Resumo em português
- `RESUMO_IMPLEMENTACAO.md` - Status da implementação
